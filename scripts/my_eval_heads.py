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


def writing(differences, goldwords, parsedline, gold_tok, list_of_extra_gold, list_of_extra_parsed, list_of_starters_gold, list_of_starters_parsed):
    """
    Writes differences in file.

    Args:
      - differences: list in which to save the differences.
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
      - list_of_extra_gold: list of integers counting missing 
        gold lines.
      - list_of_extra_parsed: list of integers counting missing 
        parsed lines.
      - list_of_starters_gold: list of numbers indicating missing
        gold lines.
      - list_of_starters_parsed: list of numbers indicating missing
        parsed lines.
    """
    goldline = goldwords[0]
    
    checking_parsed = parsedline[6]
    checking_gold = goldline[6]

    if checking_parsed != '_':
        if len(list_of_starters_parsed) > 0:
            checking_parsed = int(checking_parsed)
            for i, num in enumerate(list_of_starters_parsed):
                if i == (len(list_of_starters_parsed) - 1): # the last one
                    if checking_parsed > num:
                        checking_parsed += list_of_extra_parsed[-1]
                        break
                elif i == 0: # the first one
                    if checking_parsed <= num: # check first possibility
                        break
                    elif checking_parsed > num and checking_parsed <= list_of_starters_parsed[i+1]: # check second possibility
                        checking_parsed += list_of_extra_parsed[i]
                        break
                else:
                    if checking_parsed > num and checking_parsed <= list_of_starters_parsed[i+1]:
                        checking_parsed += list_of_extra_parsed[i]
                        break
        else:
            checking_parsed = int(checking_parsed)
        
    if checking_gold != '_':
        if len(list_of_starters_gold) > 0 and len(list_of_extra_gold) > 0:
            checking_gold = int(checking_gold)
            for i, num in enumerate(list_of_starters_gold):
                if i == (len(list_of_starters_gold) - 1): # the last one
                    if checking_gold > num:
                        checking_gold += list_of_extra_gold[-1]
                        break
                elif i == 0: # the first one
                    if checking_gold <= num: # check first possibility
                        break
                    elif checking_gold > num and checking_gold <= list_of_starters_gold[i+1]: # check second possibility
                        checking_gold += list_of_extra_gold[i]
                        break
                else:
                    if checking_gold > num and checking_gold <= list_of_starters_gold[i+1]:
                        checking_gold += list_of_extra_gold[i]
                        break
        else:
            checking_gold = int(checking_gold)
    
    if checking_parsed == checking_gold and parsedline[7] == goldline[7]:
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '', '  '.join(parsedline)))

    elif checking_parsed == checking_gold and parsedline[7] != goldline[7]:
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline)))

    elif checking_parsed != checking_gold and parsedline[7] == goldline[7]:
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline)))

    else:
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline)))
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
    to_dict = {}
    
    file = open(f'{path}{filename}', 'w')
    for sent_id, (sentence, goldwords) in zip(gold_ids, gold.items()): # goldwords is the sentence as in gold standard
        
        parsedwords = parsed[sentence] # parsedwords is the sentence as UDPipe parsed it
        gold_tok = [x[1] for x in goldwords] # sentence word forms
        n = 0 # counter for case 2
        parsed_lines = []
        list_of_starters_gold = [] 
        list_of_starters_parsed = [] # a list containing the numbers that guide when to add the extra elements
        list_of_extra_gold = []
        list_of_extra_parsed = []
        extra_gold = 0
        extra_parsed = 0
        
        differences = []
        max_gold = int(goldwords[-1][0])
        max_parsed = int(parsedwords[-1][0])
        
        for parsedline in parsedwords: # i. e. ['1', 'example1', '_', 'POS', '_', '_', '0', 'root']
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
                        list_of_starters_parsed.append(int(parsedline[0]))
                        extra_parsed += (int(numbers[-1]) - int(numbers[0]))
                        list_of_extra_parsed.append(extra_parsed)
                        writing(differences, goldwords, parsedline, gold_tok, list_of_extra_gold, list_of_extra_parsed, list_of_starters_gold, list_of_starters_parsed)
                        for _ in range(times):
                            differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldwords[0]), 'M', ' '*50)) 
                            del goldwords[0]
                            del gold_tok[0]
                    
                    else: # case 1
                        writing(differences, goldwords, parsedline, gold_tok, list_of_extra_gold, list_of_extra_parsed, list_of_starters_gold, list_of_starters_parsed)
                else: 
                    
                    join_gold = '' # case 3
                    join_gold_counter = 0
                    
                    for word in gold_tok:
                        if join_gold != parsedline[1]:
                            join_gold = join_gold + word
                            join_gold_counter += 1
                        else:
                            list_of_starters_parsed.append(int(parsedline[0]))
                            writing(differences, goldwords, parsedline, gold_tok, list_of_extra_gold, list_of_extra_parsed, list_of_starters_gold, list_of_starters_parsed)
                            extra_parsed += join_gold_counter - 1
                            list_of_extra_parsed.append(extra_parsed)

                            for i in range(join_gold_counter - 1): # i = 0, 1, 2, 3...
                                differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldwords[0]), 'M', ' '*50)) 
                                del goldwords[0]
                                del gold_tok[0]
                            break
                    
                    if join_gold != parsedline[1]: # case 2
                        n += 1
                        if n == 1:
                            join_parsed = parsedline[1] 
                            parsed_lines.append(parsedline) 
                            list_of_starters_gold.append(int(goldwords[0][0]))
                        else:
                            join_parsed = join_parsed + parsedline[1]
                            parsed_lines.append(parsedline) 

                        if join_parsed == gold_tok[0]:
                            for c, line in enumerate(parsed_lines):
                                if c == 0:
                                    writing(differences, goldwords, line, gold_tok, list_of_extra_gold, list_of_extra_parsed, list_of_starters_gold, list_of_starters_parsed)
                                else:
                                    extra_gold += c
                                    list_of_extra_gold.append(extra_gold)
                                    differences.append("{:<50}{:<5}{:<}\n".format(' '*50, 'M', '  '.join(line)))
                            n = 0
                            parsed_lines = []

            else:
                print('ERROR')
                differences.append("{:<50}{:<5}{:<}\n".format(' '*50, 'E', '  '.join(parsedline))) 
        
        # calculate UD scores
        maximum_length = max_gold if max_gold>= max_parsed else max_parsed
        numerator_score = copy.deepcopy(maximum_length)
        for line in differences:
            if '|' in line:
                numerator_score -= 1
        to_dict[sent_id] = (numerator_score/maximum_length, maximum_length, differences)
        
    # sort by score and write to_dict contents in file
    file = open(f'{path}{filename}', 'w')
    
    sorted_by_score = {k: v for k, v in sorted(to_dict.items(), key=lambda item: item[1])} #, reverse = True)}
    for sent_id, (score, maximum_length, differences) in sorted_by_score.items():
        file.write(sent_id)
        file.write(f'Score = {score}, TotalLength = {maximum_length}, PerfectMatch = {1 if score == 1 else 0} \n')
        for line in differences:
            file.write(line)
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