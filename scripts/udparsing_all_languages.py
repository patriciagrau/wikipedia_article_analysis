"""
Parses Wikipedia articles with UDPipe2.

Parses the articles in Wikipedia written in most languages
in all the languages available in UD, with UDPipe2.

"""
import os
import re
import requests
import json
import tempfile
import argparse
from bs4 import BeautifulSoup

def get_ud_models():
    """
    Loading the name of models available in UDPipe 2
    Returns:
      - models: a dictionary containing a language as the key
        and the models as the values. 
        
    models = {'lang_1' : ['model1', 'model2',...], 
              'lang_2' : ['model3', 'model4',...], ...}
    """
    r = requests.get('http://lindat.mff.cuni.cz/services/udpipe/api/models')
    data = json.loads(r.text)
    
    models = {}
    for i in data['models'].keys():
        if i.startswith('norwegian') or i.startswith('ancient-greek'):
            lang = '_'.join(i.split('-')[0:2])
        elif i.startswith('old-church'):
            lang = '_'.join(i.split('-')[0:3])  
        else:
            lang = i.split('-')[0]
        if lang in models:
            models[lang].append(i)
        else:
            models[lang] = [i]
    
    return models

def get_wiki_lang_codes():
    """
    Retrieves the language codes in Wikipedia
    
    Returns:
      - languages: a dictionary containing
        the language code as the key and the
        language as the value.
    """
    url_languages = 'https://meta.wikimedia.org/wiki/List_of_Wikipedias'
    with tempfile.TemporaryFile(mode='w+t') as tmp:
        tmp.write(requests.get(url_languages).text)
        tmp.seek(0)
        languages = {}
        n = 0
        l = []
        for i, alltext in enumerate(tmp.readlines()):
            # Looking at the raw html file, I am interested in the
            # lines between 165 and 8484
            if i < 165 or i > 8484:
                continue
            if alltext.startswith('<td>'):
                texto = alltext.strip('\t')
                cleantext = BeautifulSoup(texto, "html.parser").text
                cleantext = cleantext.strip()
                if len(cleantext) != 0:
                    if str(n).endswith('1'):
                        l.append(cleantext.lower())
                    elif str(n).endswith('2'):
                        if l[0] == 'norwegian bokmål':
                            l[0] = 'norwegian bokmaal'
                        elif l[0] == 'northern sami':
                            l[0] = 'north sami'
                        languages[cleantext] = l[0] # {code : lang, code : lang, ...}
        #                 languages[l[0]] = cleantext # {lang : code, lang : code, ...}
                    else:
                        l = []
                    n += 1
    return languages

def get_articles():
    """
    Get articles in Wikipedia written in most languages.
    
    Returns:
      - articles: a dictionary containing the article name as
        the key, the number of languages available for that 
        article, and the link. 
    
    articles = {'Article name' : (num_lang_available, 'wiki/link'), 
                'Article name' : (num_lang_available, 'wiki/link'), ...}
    """
    r = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_articles_written_in_the_greatest_number_of_languages')
    
    articles = {}
    for element in r.text.split('\n'):
        if element.startswith('<p>') or element.startswith('</p>'):
            if len(element.split(' ')) > 1:
                link = element.split(' ')[1][7:-1]
            text = BeautifulSoup(element, "html.parser").text
            if ':' in text:
                name, other = text.split(':')
                for e in other.split(' '):
                    if e.isnumeric():
                        articles[name] = (int(e), link)
            else:
                words = text.split(' ')
                name = words[0]
                for e in words:
                    if e.isnumeric():
                        articles[name] = (int(e), link)
    return articles

def clean_text_api(tag, model):
    """
    Cleans text and calls UDPipe API
    Args:
      - text: tag from beautifulsoup.
      - model: language to use
    Returns:
      - out: result from API
    """
    api_url = 'https://lindat.mff.cuni.cz/services/udpipe/api/process'

    cleantext = tag.get_text()
    cleantext = re.sub(r'\[(.*?)\]', '', cleantext) # remove [anything in square brackets]
    cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
    
    if len(cleantext) != 0 and cleantext!='\n':
        myobj = {'data' : cleantext, 'model' : model, 'tokenizer' : '', 'tagger' : '', 'parser' : ''}
        out = requests.post(api_url, data = myobj)
        return out
    else:
        return None

def udparsing(url, lang, name, path, getting_lang = False):
    """
    Reads url and creates conllu file of the parsed text.
    
    Args:
      - url: url to parse.
      - lang: language of the file.
      - name: desired name for the file.
      - path: path.
    Param:
      - getting_lang: bool to specify whether we are
        retrieving the languages available in the 
        article.
    Returns:
      - lang_in_article: if getting_lang = True,
        returns a list of the Wikipedia link in 
        all other available languages.
    """
    prev = requests.get(url).text
    htmlParse = BeautifulSoup(prev, 'html.parser')
    
    # Ignore all tags with classes containing "infobox", "references", "navbox", "toclevel" or "vector-user"
    regex = re.compile('.*')
    infobox = re.compile('^infobox*')
    references = re.compile('^references*')
    navigationmenu = re.compile('^navbox*')
    toclev = re.compile('^toclevel*')
    vectormenu = re.compile('.*vector-user.*')

    for div in htmlParse.find_all(regex, {'class': [infobox, references, navigationmenu, toclev, vectormenu]}): 
        div.decompose()
    
    model = models[lang][0]
    lang_in_article = []
    
    # Get the wikipedia links in other languages
    if getting_lang:
        for ultag in htmlParse.find_all('ul', {'class': 'vector-menu-content-list'}):
            for litag in ultag.find_all('li', {'class': re.compile("^interlanguage-link interwiki")}):
                litag = str(litag)
                for element in litag.split(' '):
                    if element.startswith('href='):
                        lang_in_article.append(element[6:-1])

    with open(f'{path}{name}.conllu', 'w') as g:

        for tag in htmlParse.find_all(["span", "p", "title"]) :
            # I want to get span the body (p), the titles, and the hN which have class="mw-headline"       
            if tag.name == "span":
                if "class" in tag.attrs and "mw-headline" in tag.attrs["class"]:
                    x = clean_text_api(tag, model)
                    if x:
                        g.write(json.loads(x.text)['result'])
            else:
                x = clean_text_api(tag, model)
                if x:
                    g.write(json.loads(x.text)['result'])
    
    if getting_lang:
        return lang_in_article

def parse_all(link, lang_codes, models, path):
    """
    Parses wiki url in all available languages,
    starting with English.
    
    Args:
      - link: link (from articles).
      - lang_codes: language codes for wikipedia
      - models: models available in UDPipe.
      - path: path where we save the articles
    """
    dir_name = link.split('/')[1]
    new_path = f'{path}data/{dir_name}/'
    os.mkdir(new_path)
    print(f'--------------------Created the folder {dir_name}--------------------')

    eng_link = f'http://en.wikipedia.org/{link}'
    
    lang_in_article = udparsing(eng_link, 'english', f'{dir_name}-english', new_path, getting_lang = True)
    print(f'----------Parsed {dir_name} in english----------')
    
    for url in lang_in_article:
        code = url.split('//')[1].split('.')[0]
        lang = '_'.join(lang_codes[code].split(' '))
        if lang in models: # only parse url if lang in UDPipe models
            udparsing(url, lang, f'{dir_name}-{lang}', new_path)
            print(f'----------Parsed {dir_name} in {lang}----------')
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parses some Wikipedia articles with UDPipe2.')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    args = parser.parse_args()
    
    models = get_ud_models()
    lang_codes = get_wiki_lang_codes()
    articles = get_articles()

    os.mkdir(f'{args.path}/data')
    print('--------------------Created the folder data--------------------')

    for article_name, tup in articles.items():
        _, link = tup
        parse_all(link, lang_codes, models, args.path)
        