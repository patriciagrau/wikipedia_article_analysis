"""
Parses a URL with UDPipe2.

Creates a file with the text parsed with a model from
the UDPipe2 API. It does not create any other files.

"""
import re
import argparse
import requests
import json
from bs4 import BeautifulSoup
import tempfile

def get_ud_models():
    """
    Loading the name of models available in UDPipe 2
    Returns:
      - models: a dictionary containing a language as the key
        and the models as the values. 
        
    models = {'lang_1' : ['model1', 'model2',...], 
              'lang_2' : ['model3', 'model4',...], 
              ...}
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
        
def udparsing(url, lang, name, path):
    """
    Reads url and creates conllu file of the parsed text.
    
    Args:
      - url: url to parse.
      - lang: language of the file.
      - name: desired name for the file.
      - path: path.
    """
    model = models[lang][0]
    with tempfile.TemporaryFile(mode='w+t') as tmp:
        tmp.write(requests.get(url).text)
        tmp.seek(0)
        starters = ['<p>', '</p><p>', '<title>', '<h']
        api_url = 'https://lindat.mff.cuni.cz/services/udpipe/api/process'
        with open(f'{path}{name}.conllu', 'w') as g:
            g.write(f'# {url}\n\n')
            for alltext in tmp.readlines():
                texto = alltext.strip('\t')
                if texto.startswith(tuple(starters)):
                    cleantext = BeautifulSoup(texto, "html.parser").text
                    cleantext = re.sub(r'\[\d+\]', '', cleantext) # remove references [digit]
                    cleantext = re.sub(r'\[[a-z]\]', '', cleantext) # remove references [letter]
                    cleantext = re.sub(r'\[n. \d+\]', '', cleantext) # remove references [n. digit]
                    cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
                    if len(cleantext) != 0:
                        myobj = {'data' : cleantext, 'model' : model,'tokenizer' : '', 'tagger' : '', 'parser' : ''}
                        x = requests.post(api_url, data = myobj)
                        g.write(json.loads(x.text)['result'])
                        
                        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parses a URL with UDPipe2.')
    parser.add_argument('url', type=str, help='url to parse')
    parser.add_argument('name', type=str, help='name for the created files')
    parser.add_argument('lang', type=str, help='language of the url. Options: afrikaans, ancient_greek, arabic, armenian, basque, belarusian, bulgarian, catalan, chinese, classical_chinese, coptic, croatian, czech, danish, dutch, english, estonian, finnish, french, galician, german, gothic, greek, hebrew, hindi, hungarian, indonesian, irish, italian, japanese, korean, latin, latvian, lithuanian, maltese, marathi, naija, north_sami, norwegian_bokmaal, norwegian_nynorsk, norwegian_nynorsklia, old_church_slavonic, old_french, old_russian, persian, polish, portuguese, romanian, russian, sanskrit, scottish_gaelic, serbian, slovak, slovenian, spanish, swedish, tamil, telugu, turkish, ukrainian, urdu, uyghur, vietnamese, welsh, wolof, kazakh, norwegian_ud')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    #parser.add_argument('--model', default=, help='model to parse from UDPipe2')

    args = parser.parse_args()
    
    models = get_ud_models()
    
    if args.lang.lower() not in models:
        print('Please input a language available in UDPipe. For more information, write --help.')
    else:
        udparsing(args.url, args.lang.lower(), args.name, args.path)
    
