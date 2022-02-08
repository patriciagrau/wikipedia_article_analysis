"""
Parses a URL with UDPipe2.

Creates a file with the html version of the url, 
the text to be parsed from the URL and another file with the text
parsed with a model from UDPipe2.

"""
import re
import argparse
import requests
import json
from bs4 import BeautifulSoup

# Loading models available in UDPipe 2
r = requests.get('http://lindat.mff.cuni.cz/services/udpipe/api/models')
data = json.loads(r.text)
models = {}
for i in data['models'].keys():
    lang = i.split('-')[0]
    if lang in models:
        models[lang].append(i)
    else:
        models[lang] = [i]

def save_htmlfile(url, name, path):
    with open(f'{path}{name}.html', 'w') as f:
        f.write(requests.get(url).text)

def save_cleantext(readfile, writefile):
    """
    Saves "clean" text from url.
    Args:
      - readfile: html file created.
      - writefile: file where we save the clean text.
    """
    starters = ['<p>', '</p><p>', '<title>', '<h']
    f = open(readfile)
    with open(writefile, 'w') as g:
        for alltext in f.readlines():
            texto = alltext.strip('\t')
            if texto.startswith(tuple(starters)):
                cleantext = BeautifulSoup(texto, "html.parser").text
                cleantext = re.sub(r'\[\d+\]', '', cleantext) # remove references [digit]
                cleantext = cleantext.strip()
                cleantext = cleantext.replace(u'\u200b', '') # remove this character
                if len(cleantext) != 0:
                    g.write(cleantext + '\n')
    f.close()

def parsing(url, file, lang, name, path, model = models[lang][0]):
    """
    Parses clean file and saves to file.
    Args:
      - file: containing the clean text to parse.
      - lang: language of the file.
    Param:
      - model: the specific model from UDPipe2 that
        we want to use. If unspecified, it's the 1st
        model from the models dictionary.
    """
    api_url = 'https://lindat.mff.cuni.cz/services/udpipe/api/process'
    with open(f'{path}{name}.conllu', 'w') as g:
        g.write(f'# {url}\n\n')
        
    with open(file, 'r') as f:
        for line in f:
            myobj = {'data' : line, 'model' : model,'tokenizer' : '', 'tagger' : '', 'parser' : ''}
            x = requests.post(api_url, data = myobj)                
            # to use 'a', the text can't exist before! Otherwise, it will append information
            with open(f'{path}{name}.conllu', 'a') as g:
                g.write(json.loads(x.text)['result'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parses a URL with UDPipe2.')
    parser.add_argument('url', type=str, help='url to parse')
    parser.add_argument('name', type=str, help='name for the created files')
    parser.add_argument('lang', type=str, help='language of the url. Options: afrikaans, ancient_greek, arabic, armenian, basque, belarusian, bulgarian, catalan, chinese, classical_chinese, coptic, croatian, czech, danish, dutch, english, estonian, finnish, french, galician, german, gothic, greek, hebrew, hindi, hungarian, indonesian, irish, italian, japanese, korean, latin, latvian, lithuanian, maltese, marathi, naija, north_sami, norwegian, old_church_slavonic, old_french, old_russian, persian, polish, portuguese, romanian, russian, sanskrit, scottish_gaelic, serbian, slovak, slovenian, spanish, swedish, tamil, telugu, turkish, ukrainian, urdu, uyghur, vietnamese, welsh, wolof, kazakh')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    #parser.add_argument('--model', default=, help='model to parse from UDPipe2')

    args = parser.parse_args()

    save_htmlfile(args.url, args.name, args.path)
    save_cleantext(f'{args.path}{args.name}.html', f'{args.path}{args.name}.txt')
    parsing(args.url, f'{args.path}{args.name}.txt', args.lang, args.name, args.path)
    
