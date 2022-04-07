# Wikipedia article analysis

This repository contains the code for the master's thesis on Wikipedia Article Analysis, by Patricia Grau Francitorra.

- The folder "scripts" contains the different scripts created. 
- The folder "creating_shell_scripts" contains some basic shell scripts to run gfud.
- The folder "testing_scripts" contains test files that were created to see if the scripts worked. 
- The folder "jupiter" was a test used to learn how to work with html files and requests. 
- The folder "gold_standard" contains:
  - deprecated: old gold standard files.
  - more_dependencies: manually annotated files that will be the gold standard for the UD evaluation, as well as the parsed files. 
  - simplified: the "simplified" version of more_dependencies, after passing them through the script fixing_scripts/fixing_conllu_for_eval.py.
  - results_gfud: files with the results from gfud eval.
  - my_results: files with the results from scripts/my_eval_heads.py and scripts/my_eval_mapping_dict.py.
- The folder "data" contains the results of the script "udparsing_all_languages.py".
- The folder "joined_by_lang" contains:
  - data_joined_by_lang: the files from "data", joined according to the language they are.
  - results_joined_by_lang: statistical analysis based on POS tags.
- The folder "cosine-sim-per-lang" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the language.
- The folder "cosine-sim-per-topic" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the topic.
- "exploratory_analysis" is a notebook where I test most things.
- "cosine-sim-visualisation" is the notebook where you can visualise the cosine similarities among the data.
- "notes" is a markdown file where I write notes/a diary about what I do and the problems I encounter.


TLDR

- The data is in the folder "data" separated by topic, and in the folder "joined_by_lang" not separated by topics.
