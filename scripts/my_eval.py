"""
Evaluation for conllu files

Compares two conllu files, similar to gfud eval, but
with some adjustments for misalignments. 
"""

import copy
import sys
from unicodedata import category
import argparse

# fancy punctuation
chrs = (chr(i) for i in range(sys.maxunicode + 1))
noperiod = set(c for c in chrs if category(c).startswith("P"))
noperiod.remove('.')

def golddict(goldfile):
    """
    Returns the contents of a gold standard conllu
    file as a dictionary.

    Args:
      - goldfile: path to gold standard conllu file.

    Returns:
      - gold: a dictionary with sentences as keys and
        each parsed line as the values. 
      - gold_ids: a list of the sentences ids.
    """
    gold = {}
    gold_ids = []
    with open(goldfile, 'r') as f:
        document = f.readlines() + ['\n']
        for line in document:
            if line.startswith('# text ='):
                key = line[:-1]
                gold[key] = []
            elif line.startswith('# sent_id ='):
                gold_ids.append(line)
            elif line[0].isdigit() and key:
                gold[key].append(line[:-1])
            elif line.strip() == '':
                sentences = []
                for e in gold[key]:
                    text = e.split('\t')
                    sentences.append(text[:-2])
                gold[key] = sentences
                key = False
    return gold, gold_ids

def rearrange_parsed(gold, parsedfile):
    """
    Rearranges the sentence parsing of a conllu file
    to match with the gold standard of the same text.

    Args:
      - gold: the output from golddict.
      - parsedfile: path to other conllu file in doubt.

    Returns:
      - parsed: a dictionary with the gold sentences as 
        keys and each parsed line as the values. 
      - bad_sentence_tokenization: a counter of the times
        a sentence has been badly split.
    """
    parsed = {}
    bad_sentence_tokenization = 0
    started = False
    
    with open(parsedfile, 'r') as g:
        document = g.readlines() + ['\n']
        for line in document:
            if line.startswith('#') and 'text' not in line:
                pass
            elif line.startswith('# text ='):
                if line[:-1] in gold:
                    key = line[:-1]
                    parsed[key] = []
                    correct = True # the sentence is separated correctly
                else: 
                    if started: # if this is not the beginning of the sentence
                        key = key + line[9:-1]
                        if key in gold:
                            parsed[key] = text
                            correct = True
                            started = False
                    else:
                        bad_sentence_tokenization += 1
                        correct = False # the sentence is separated incorrectly
                        started = True
                        key = line[:-1] # the beginning of the correct sentence
                        text = []
            else:
                if correct:
                    if line[0].isdigit() and key:
                        parsed[key].append(line[:-1])
                    if line.strip() == '':
                        sentences = []
                        for e in parsed[key]:
                            text = e.split('\t')
                            sentences.append(text[:-2])
                        parsed[key] = sentences
                        key = False
                else:
                    if line[0].isdigit():
                        text.append(line[:-1])
    
    return parsed, bad_sentence_tokenization


def writing(file, goldwords, parsedline, gold_tok, extra_gold, extra_parsed, start_gold = 0, start_parsed = 0):
    """
    Writes differences in file.

    Args:
      - file: opened file from the function where it's called.
      - goldwords: the analysed words per sentence of the gold standard. 
         Example:
         [['1', 'example1', '_', 'EX', '_', '_', '0', 'dep'],
          ['2', 'example2', '_', 'EX', '_', '_', '1', 'dep'], ...]
      - parsedline: every analysed words of the UD parsed words:
         Example:
         ['1', 'example1', '_', 'EX', '_', '_', '0', 'dep']
      - gold_tok:  a list containing the tokens of the sentence, based
         on the gold standard.
         Example:
         ['example1', 'example2', 'example3', ...]
      - extra_gold: integer counting missing gold lines.
      - extra_parsed: integer counting missing parsed lines.
      - start_gold: optional integer, marks whether to add extra_gold
         to the head of the goldline.
      - start_parsed: optional integer, marks whether to add extra_parsed
         to the head of the parsedline.
    """
    goldline = goldwords[0]
    if '-' in goldline[0]: # if there is a range of numbers in the gold standard
        str_gold_number, _ = goldline[0].split('-')
        gold_number = int(str_gold_number)
    else:
        gold_number = int(goldline[0])
    
    if '-' in parsedline[0]: # if there is a range of numbers in the other parsed text
        str_parsed_number, _ = goldline[0].split('-')
        parsed_number = int(str_parsed_number)
    else:
        parsed_number = int(parsedline[0])

    if start_gold == 0: # if start_gold is unspecified, it will be the 1st element
        start_gold = gold_number
    if start_parsed == 0: # if start_parsed is unspecified, it will be the 1st element
        start_parsed = parsed_number

    if parsedline[6] != '_':
        if start_parsed < int(parsedline[6]):
            parsed_head = int(parsedline[6]) + extra_parsed # add numbers for misalignments
        else:
            parsed_head = int(parsedline[6])
    else:
        parsed_head = parsedline[6]

    if goldline[6] != '_':
        if start_gold < int(goldline[6]):
            gold_head = int(goldline[6]) + extra_gold # add numbers for misalignments
        else:
            gold_head = int(goldline[6])
    else:
        gold_head = goldline[6]

    if parsed_head == gold_head and parsedline[7] == goldline[7]:
        file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '', '  '.join(parsedline)))

    elif  parsed_head == gold_head and parsedline[7] != goldline[7]:
        file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldline), 'D', '  '.join(parsedline)))

    elif  parsed_head != gold_head and parsedline[7] == goldline[7]:
        file.write('parsed_head ' + str(parsed_head) + '\n')
        file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldline), 'H', '  '.join(parsedline)))

    else:
        file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline)))
    del goldwords[0]
    del gold_tok[0]

def differences(inputgold, inputparsed, path, filename):
    """
    Writes in file the evaluation of the content of two 
    conllu files in dictionary form.

    Args:
      - inputgold: gold standard dictionary from golddict function.
      - gold_ids: a list of the sentence ids from the gold standard.
      - inputparsed: parsed dictionary from splitting function.
      - path: path in which to save the file.
      - filename: name of the evaluation file. 
    """

    gold = copy.deepcopy(inputgold)
    parsed = copy.deepcopy(inputparsed)
    
    file = open(f'{path}{filename}', 'w')
    for sent_id, (sentence, goldwords) in zip(gold_ids, gold.items()): # goldwords is the sentence as in gold standard
        file.write(sent_id)
        parsedwords = parsed[sentence] # parsedwords is the sentence as UDPipe parsed it
        gold_tok = [x[1] for x in goldwords] # sentence word forms
        n = 0 # counter for case 2
        parsed_lines = []
        extra_gold = 0
        extra_parsed = 0
        
        for parsedline in parsedwords: # i. e. ['1', 'exampl1', '_', 'POS', '_', '_', '0', 'root']
            # Possible outcomes:
            # 1. words match
            # 2. the word has been split into more pieces in the parsing
            # 3. the word has not been split
            # 4. the word is not morhologically separed (example del > de el)
                 
            if gold_tok:
                if parsedline[1] == gold_tok[0]:
                    if '-' in goldwords[0][0] and '-' not in parsedline[0]: # case 4
                        numbers = goldwords[0][0].split('-')
                        times = int(numbers[-1]) - int(numbers[0]) + 1 # the number of tokens that make the goldword
                        writing(file, goldwords, parsedline, gold_tok, extra_gold, extra_parsed, start_parsed=int(numbers[0]))
                        extra_parsed += (int(numbers[-1]) - int(numbers[0]))
                        for _ in range(times):
                            file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldwords[0]), 'M', ' '*50)) # does not work for French. TO DO
                            del goldwords[0]
                            del gold_tok[0]
                    
                    else: # case 1
                        writing(file, goldwords, parsedline, gold_tok, extra_gold, extra_parsed)
                else: 
                    
                    join_gold = '' # case 3
                    join_gold_counter = 0
                    
                    for word in gold_tok:
                        if join_gold != parsedline[1]:
                            join_gold = join_gold + word
                            join_gold_counter += 1
                        else:
                            writing(file, goldwords, parsedline, gold_tok, extra_gold, extra_parsed)
                            extra_parsed += join_gold_counter - 1
                            for i in range(join_gold_counter - 1): # i = 0, 1, 2, 3...
                                file.write("{:<50}{:<5}{:<}\n".format('  '.join(goldwords[0]), 'M', ' '*50))
                                del goldwords[0]
                                del gold_tok[0]
                            break
                    
                    if join_gold != parsedline[1]: # case 2
                        n += 1
                        if n == 1:
                            join_parsed = parsedline[1]
                            parsed_lines.append(parsedline)
                        else:
                            join_parsed = join_parsed + parsedline[1]
                            parsed_lines.append(parsedline)

                        if join_parsed == gold_tok[0]:
                            for c, line in enumerate(parsed_lines):
                                if c == 0:
                                    writing(file, goldwords, line, gold_tok, extra_gold, extra_parsed)
                                else:
                                    extra_gold += n
                                    file.write("{:<50}{:<5}{:<}\n".format(' '*50, 'M', '  '.join(line)))
                            n = 0
                            parsed_lines = []

            else:
                print('ERROR')
                file.write("{:<50}{:<5}{:<}\n".format(' '*50, 'E', '  '.join(parsedline)))
        file.write('\n')
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluation for conllu files. Compares two conllu files, similar to gfud eval, but with some adjustments for misalignments.')
    parser.add_argument('gold_path', type=str, help='path of the gold standard conllu file.')
    parser.add_argument('parsed_path', type=str, help='path of the other conllu file.')
    parser.add_argument('filename', type=str, help='name for the created file')
    parser.add_argument('--path', default= './',type=str, help='folder where we save the files')

    args = parser.parse_args()

    gold, gold_ids = golddict(args.gold_path)
    parsed, bad_sentence_tokenization = rearrange_parsed(gold, args.parsed_path)

    print(f'{bad_sentence_tokenization} sentences were split differently in the input file compared to the gold standard.')

    differences(gold, parsed, args.path, args.filename)