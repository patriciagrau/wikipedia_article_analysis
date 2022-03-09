import re
import argparse

def change_to_tabs(file, name, path):
    f = open(file)
    with open(f'{path}{name}', 'w') as g:
        for line in f:
            if line.startswith('#'):
                g.write(line)
            else:
                newline = re.sub('\s+', '\t', line)
                g.write(newline + '\n')
    f.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Changing spaces for tabs.')
    parser.add_argument('file', type=str, help='file to fix')
    parser.add_argument('name', type=str, help='name for the new file')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the file')
    args = parser.parse_args()

    change_to_tabs(args.file, args.name, args.path)