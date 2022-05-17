"""
Organises the structures of a language in descending
order. If the option -one is given, it does it for 
one file. Otherwise, it does it for all the files in
a specified directory.

"""

import argparse
import os

def frequency_structures_per_lang(filepath, outfilepath):
    """
    Creates a file with the frequency of the structures
    from the separated structures file in descending order.

    Args:
      - filepath: the file with the structures
        (in lang_structures/separated_lang_
        structures)
      - outfilepath: path where we save the 
        created file.
    """
    
    d = {}
    f = open(filepath)

    n = 0
    for line in f.readlines():
        if n == 0:
            root = [line[:-1]]
            dependents = []
            n += 1
        elif line.strip() == '':
            root.extend(sorted(dependents))
            if tuple(root) in d:
                d[tuple(root)] += 1
            else:
                d[tuple(root)] = 1
            n = 0        
        else:
            dependents.append(line[:-1])
            n += 1
    f.close()

    my_keys = sorted(d, key=d.get, reverse=True)

    with open(outfilepath, 'w') as g:
        for key in my_keys:
            newsep = [x.replace('\t', '-') for x in key]
            root = newsep[0][:-5]
            newkey = root + '(' + ', '.join(newsep[1:]) + ')'
            g.write(newkey + ': ' + str(d[key]) + '\n')

def frequency_structures_per_lang_all(dirpath, outfilepath):
    """
    Creates files with the frequency of the structures
    from the separated structures files in descending order.

    Args:
      - dirpath: the directly containing the files with the 
        structures(lang_structures/separated_lang_
        structures)
      - outfilepath: path where we save the 
        created files.
    """
    
    list_of_files = os.listdir(dirpath)
    
    for filepath in list_of_files:
        d = {}
        lang = filepath[:-15]
        f = open(f'{dirpath}{filepath}')

        n = 0
        for line in f.readlines():
            if n == 0:
                root = [line[:-1]]
                dependents = []
                n += 1
            elif line.strip() == '':
                root.extend(sorted(dependents))
                if tuple(root) in d:
                    d[tuple(root)] += 1
                else:
                    d[tuple(root)] = 1
                n = 0        
            else:
                dependents.append(line[:-1])
                n += 1
        f.close()

        my_keys = sorted(d, key=d.get, reverse=True)

        with open(f'{outfilepath}{lang}_structures_frequency.txt', 'w') as g:
            for key in my_keys:
                newsep = [x.replace('\t', '-') for x in key]
                root = newsep[0][:-5]
                newkey = root + '(' + ', '.join(newsep[1:]) + ')'
                g.write(newkey + ': ' + str(d[key]) + '\n')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Returns the frequency of the structures from the separated structures file(s).')
    parser.add_argument('filepath', type=str, help='path of the file(s) to analyse.')
    parser.add_argument('newfilepath', type=str, help='path to save new file(s).')
    parser.add_argument('--fileordir', default= 'dir',type=str, help='frequency of one file (file) or one directory (dir)')

    args = parser.parse_args()

    if args.fileordir == 'dir':
        frequency_structures_per_lang_all(args.filepath, args.newfilepath)
    elif args.fileordir == 'file':
        frequency_structures_per_lang(args.filepath, args.newfilepath)
    else:
        print('Please enter file for a file or dir for a directory.')