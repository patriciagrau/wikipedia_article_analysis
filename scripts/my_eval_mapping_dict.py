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


def writing(differences, goldwords, parsedline, gold_tok, gold_id_to_word, parsed_id_to_word):
    """
    Appends differences to list.
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
      - gold_id_to_word: dictionary mapping number to token for gold standard.
         Example:
         {'1' : 'example1', '2' : 'example2', ...}
      - parsed_id_to_word: dictionary mapping number to token for other file.
         Example:
         {'1' : 'example1', '2' : 'example2', ...}
    """
    goldline = goldwords[0]
    
    if parsedline[6] != '_':
        check_parsedline = parsed_id_to_word[parsedline[6]]
    else:
        check_parsedline = parsedline[6]
        
    if goldline[6] != '_':
        check_goldline = gold_id_to_word[goldline[6]]
    else:
        check_goldline = goldline[6]
    
    if check_parsedline == check_goldline and parsedline[7] == goldline[7]: # if refer to same word and same dep
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '', '  '.join(parsedline)))

    elif check_parsedline == check_goldline and parsedline[7] != goldline[7]: # if refer to same word and diff dep
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline))) # used to be D

    elif check_parsedline != check_goldline and parsedline[7] == goldline[7]: # if refer to diff word and same dep
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline))) # used to be H

    else: # if refer to diff word and diff dep
        differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldline), '|', '  '.join(parsedline)))
    del goldwords[0]
    del gold_tok[0]

def differences(inputgold, gold_ids, inputparsed, path, filename):
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
    
    for sent_id, (sentence, goldwords) in zip(gold_ids, gold.items()): # goldwords is the sentence as in gold standard
        
        differences = []
        
        gold_id_to_word = {x[0]:x[1] for x in goldwords} # dict mapping number to token for gold standard
        gold_id_to_word['0'] = 'root'
        max_gold = int(goldwords[-1][0])
        
        parsedwords = parsed[sentence] # parsedwords is the sentence as UDPipe parsed it
        parsed_id_to_word = {x[0]:x[1] for x in parsedwords} # dict mapping number to token for other parsed doc
        parsed_id_to_word['0'] = 'root'
        max_parsed = int(parsedwords[-1][0])

        
        gold_tok = [x[1] for x in goldwords] # sentence word forms
        n = 0 # counter for case 2
        parsed_lines = []
        
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
                        writing(differences, goldwords, parsedline, gold_tok, gold_id_to_word, parsed_id_to_word)
                        for i in range(times):
                            differences.append("{:<50}{:<5}{:<}\n".format('  '.join(goldwords[0]), 'M', ' '*50)) 
                            del goldwords[0]
                            del gold_tok[0]
                    
                    else: # case 1
                        writing(differences, goldwords, parsedline, gold_tok, gold_id_to_word, parsed_id_to_word)
                else: 
                    
                    join_gold = '' # case 3
                    join_gold_counter = 0
                    
                    for word in gold_tok:
                        if join_gold != parsedline[1]:
                            join_gold = join_gold + word
                            join_gold_counter += 1
                        else:
                            writing(differences, goldwords, parsedline, gold_tok, gold_id_to_word, parsed_id_to_word)
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
                        else:
                            join_parsed = join_parsed + parsedline[1]
                            parsed_lines.append(parsedline)

                        if join_parsed == gold_tok[0]:
                            for c, line in enumerate(parsed_lines):
                                if c == 0:
                                    writing(differences, goldwords, line, gold_tok, gold_id_to_word, parsed_id_to_word)
                                else:
                                    differences.append("{:<50}{:<5}{:<}\n".format(' '*50, 'M', '  '.join(line)))
                            n = 0
                            parsed_lines = []

            else:
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

    differences(gold, gold_ids, parsed, args.path, args.filename)