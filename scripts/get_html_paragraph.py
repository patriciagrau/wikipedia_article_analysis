import argparse
import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Saves content of url in html file.')
    parser.add_argument('url', type=str, help='url to parse')
    # parser.add_argument('name', type=str, help='desired name for the created file')
    # parser.add_argument('--path', default= './',type=str, help='folder where we save the files')

    args = parser.parse_args()

    html = urllib.request.urlopen(args.url)

    htmlParse = BeautifulSoup(html, 'html.parser')

    for para in htmlParse.find_all(["p", "title", "h2"]):
        print(para.get_text())