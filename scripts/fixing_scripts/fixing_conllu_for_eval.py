import argparse

def fixing_conllu(filename, newname, path):
    with open(f'{path}{newname}', 'w') as g:
        with open(filename) as f:
            for line in f:
                if line[0].isdigit():
                    if line[-2] == '\t':
                        line = line[0:-2] + line[-1:]
                    oldline = line.split('\t')
                    newline = [oldline[0], oldline[1], '_', oldline[3], '_', '_', oldline[6], oldline[7], '_', oldline[9]]
                    g.write('\t'.join(newline)) # + '\n')
                else:
                    g.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fixing conllu files for evaluation.')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')
    parser.add_argument('filename', type=str, help='name of the file to fix')
    parser.add_argument('newname', type=str, help='new name for the file')
    args = parser.parse_args()

    fixing_conllu(args.filename, args.newname, args.path)