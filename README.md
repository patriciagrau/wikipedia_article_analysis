# The Linguistic Structure of Wikipedia

This repository contains the code for the master's thesis on The Linguistic Structure of Wikipedia, by Patricia Grau Francitorra.

- The directory "scripts" contains the different scripts created. 
- The directory "creating_shell_scripts" contains some basic shell scripts to run gfud.
- The directory "gold_standard" contains:
  - more_dependencies: manually annotated files that will be the gold standard for the UD evaluation, as well as the parsed files. 
  - simplified: the "simplified" version of more_dependencies, after passing them through the script fixing_scripts/fixing_conllu_for_eval.py.
  - results_gfud: files with the results from gfud eval.
  - my_results: files with the results from scripts/my_eval_heads.py.
- The directory "data" contains the results of the script "udparsing_all_languages.py".
- The directory "joined_by_lang" contains:
  - data_joined_by_lang: the files from "data", joined according to the language they are.
  - results_joined_by_lang: statistical analysis based on POS tags and dependency relations.
- The directory "cosine-sim-per-lang" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the language.
- The directory "cosine-sim-per-topic" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the topic.
- The directory "cosine-sim-per-language-structure" contains the cosine similarity values between the files of the data based on their structures.
- The directory "lang_structures" contains the most common language structures for each language, and the most common structures among all languages.
- "exploratory_analysis" is a notebook where I test most things.
- "cosine-sim-visualisation" is the notebook where you can visualise the cosine similarities among the data.
- "lang_structures" is a notebook where I work with the most common language structures in the directory lang_structures.
