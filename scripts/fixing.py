# trying to fix what is wrong with the web scraping
import os
import re
import requests
import json
import argparse
from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fixing parser.')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    parser.add_argument('url', type=str, help='url to parse')
    args = parser.parse_args()

    prev = requests.get(args.url).text

    htmlParse = BeautifulSoup(prev, 'html.parser')
    
    # model = 'french-gsd-ud-2.6-200830'
    model = 'english-ewt-ud-2.6-200830'

    regex = re.compile('.*')
    infobox = re.compile('^infobox*')
    references = re.compile('^references*')
    navigationmenu = re.compile('^navbox*')
    toclev = re.compile('^toclevel*')
    vectormenu = re.compile('.*vector-user.*')
    # n = 0
    for div in htmlParse.find_all(regex, {'class': [infobox, references, navigationmenu, toclev, vectormenu]}): 
    # for div in htmlParse.find_all(regex, {'class': infobox}): 
        # n += 1
        div.decompose()

    # print(n)


    api_url = 'https://lindat.mff.cuni.cz/services/udpipe/api/process'

    with open(f'{args.path}fixing.txt', 'w') as g:

        for tag in htmlParse.find_all(["span", "p", "title"]) :
            # I want to get span the body (p), the titles, and the hN which have class="mw-headline"    
            if tag.name == "span":
                if "class" in tag.attrs and "mw-headline" in tag.attrs["class"]:
                    
                    cleantext = tag.get_text()
                    cleantext = re.sub(r'\[\d+\]', '', cleantext) # remove references [digit]
                    cleantext = re.sub(r'\[[a-z]\]', '', cleantext) # remove references [letter]
                    cleantext = re.sub(r'\[n. \d+\]', '', cleantext) # remove references [n. digit]
                    cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
                    
                    if len(cleantext) != 0 and cleantext!='\n':
                        myobj = {'data' : cleantext, 'model' : model, 'tokenizer' : '', 'tagger' : '', 'parser' : ''}
                        x = requests.post(api_url, data = myobj)
                        g.write(json.loads(x.text)['result'])
                    # print(tag.get_text())
                    # g.write(tag.get_text())
                    # print(tag.parent.attrs["class"])
                    # g.write(tag.parent.name)
                    # g.write('\n')
                    # print()
                    # break
            else:
                cleantext = tag.get_text()
                cleantext = re.sub(r'\[\d+\]', '', cleantext) # remove references [digit]
                cleantext = re.sub(r'\[[a-z]\]', '', cleantext) # remove references [letter]
                cleantext = re.sub(r'\[n. \d+\]', '', cleantext) # remove references [n. digit]
                cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
                # cleantext = re.sub(r'\[(.*?)\]', '', cleantext) # remove [anything in square brackets]
                # cleantext = cleantext.replace(u'\u200b', '') # remove the zero-width-space character
                
                if len(cleantext) != 0 and cleantext!='\n':
                    myobj = {'data' : cleantext, 'model' : model, 'tokenizer' : '', 'tagger' : '', 'parser' : ''}
                    x = requests.post(api_url, data = myobj)
                    g.write(json.loads(x.text)['result'])
                # print(tag.get_text())
                # g.write(tag.get_text())
                # print(tag.parent.attrs["class"])
                # g.write(tag.parent.text)
                # g.write('\n')
                # print()
                # break

