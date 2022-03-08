"""
Creates empty conllu file.

Creates empty conllu file to fill in with POS 
tags, dependencies, etc., for gold standard.
"""
import re
import argparse
import requests
import json
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

def clean_text(tag):
    """
    Cleans text
    Args:
      - text: tag from beautifulsoup.
    Returns:
      - out: text without tags.
    """
    cleantext = tag.get_text()
    # cleantext = re.sub(r'\[(.*?)\]', '', cleantext) # remove [anything in square brackets]
    cleantext = re.sub(r'\[\d+\]', '', cleantext) # remove references [digit]
    cleantext = re.sub(r'\[[a-z]\]', '', cleantext) # remove references [letter]
    cleantext = re.sub(r'\[n. \d+\]', '', cleantext) # remove references [n. digit]
    cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
    
    return cleantext

def empty(url, name, model, path = './'):
    
    prev = requests.get(url).text

    htmlParse = BeautifulSoup(prev, 'html.parser')

    regex = re.compile('.*')
    infobox = re.compile('^infobox*')
    references = re.compile('^references*')
    navigationmenu = re.compile('^navbox*')
    toclev = re.compile('^toclevel*')
    vectormenu = re.compile('.*vector-user.*')
    
    for div in htmlParse.find_all(regex, {'class': [infobox, references, navigationmenu, toclev, vectormenu]}): 
        div.decompose()
    
    for div in htmlParse.find_all("span", id="coordinates"):
        div.decompose()

    text = ''

    for tag in htmlParse.find_all(["span", "p", "title"]) :
        # I want to get span the body (p), the titles, and the hN which have class="mw-headline"    
        if tag.name == "span":
            if "class" in tag.attrs and "mw-headline" in tag.attrs["class"]:
                text += clean_text(tag) + 2*'\n'
        elif tag.name == "title":
            text += clean_text(tag) + 2*'\n'
        else:
            text += clean_text(tag) + '\n'

    with open(f'{path}empty_{name}_{model}.conllu', 'w') as g:
        api_url = 'https://lindat.mff.cuni.cz/services/udpipe/api/process'
        myobj = {'data' : text, 'model' : model,'tokenizer' : ''}
        x = requests.post(api_url, data = myobj)  
        g.write(json.loads(x.text)['result']) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates empty conllu file.')
    parser.add_argument('url', type=str, help='url to parse')
    parser.add_argument('name', type=str, help='name for the created file')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    parser.add_argument('lang', type=str, help='language of the url. Options: afrikaans, ancient_greek, arabic, armenian, basque, belarusian, bulgarian, catalan, chinese, classical_chinese, coptic, croatian, czech, danish, dutch, english, estonian, finnish, french, galician, german, gothic, greek, hebrew, hindi, hungarian, indonesian, irish, italian, japanese, korean, latin, latvian, lithuanian, maltese, marathi, naija, north_sami, norwegian_bokmaal, norwegian_nynorsk, norwegian_nynorsklia, old_church_slavonic, old_french, old_russian, persian, polish, portuguese, romanian, russian, sanskrit, scottish_gaelic, serbian, slovak, slovenian, spanish, swedish, tamil, telugu, turkish, ukrainian, urdu, uyghur, vietnamese, welsh, wolof, kazakh, norwegian_ud')
    #parser.add_argument('--model', default=, help='model to parse from UDPipe2')

    args = parser.parse_args()
    models = get_ud_models()
    
    if args.lang.lower() not in models:
        print('Please input a language available in UDPipe. For more information, write --help.')
    else:
        empty(args.url, args.name, args.lang.lower(), args.path)