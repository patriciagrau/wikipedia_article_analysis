"""
Saves content of url in html file.
"""

import argparse
import requests

def save_htmlfile(url, name, path):
    """
    Saves content of url in html file.
    Args:
      - url: url to parse.
      - name: desired name for the file.
      - path: path.
    """
    with open(f'{path}{name}.html', 'w') as f:
        f.write(requests.get(url).text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Saves content of url in html file.')
    parser.add_argument('url', type=str, help='url to parse')
    parser.add_argument('name', type=str, help='desired name for the created file')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')

    args = parser.parse_args()
    
    save_htmlfile(args.url, args.name, args.path)