# Wikipedia article analysis


TLDR (Keivan)

- The data is in the folder "data" separated by topic, and in the folder "joined_by_lang" not separated by topics (simply concatenated, not in correct conllu format).
- Cosine sim scripts in creating_shell_scripts/language_scripts and creating_shell_scripts/topic_scripts. 
- Cosine sim data in cosine-sim-per-topic and cosine-sim-per-lang .
- Language structures scripts in creating_shell_scripts/language_structures.sh .
- Language structures data in folder lang_structures, separated by lang, and all together in file common_lang_structures.txt (from lang_structures notebook!)
- Information about POS and dependencies by lang in the folder joined_by_lang/results_joined_by_lang/.



This repository contains the code for the master's thesis on Wikipedia Article Analysis, by Patricia Grau Francitorra.

- The directory "scripts" contains the different scripts created. 
- The directory "creating_shell_scripts" contains some basic shell scripts to run gfud.
- The directory "testing_scripts" contains test files that were created to see if the scripts worked. 
- The directory "jupiter" was a test used to learn how to work with html files and requests. 
- The directory "gold_standard" contains:
  - deprecated: old gold standard files.
  - more_dependencies: manually annotated files that will be the gold standard for the UD evaluation, as well as the parsed files. 
  - simplified: the "simplified" version of more_dependencies, after passing them through the script fixing_scripts/fixing_conllu_for_eval.py.
  - results_gfud: files with the results from gfud eval.
  - my_results: files with the results from scripts/my_eval_heads.py and scripts/my_eval_mapping_dict.py.
- The directory "data" contains the results of the script "udparsing_all_languages.py".
- The directory "joined_by_lang" contains:
  - data_joined_by_lang: the files from "data", joined according to the language they are.
  - results_joined_by_lang: statistical analysis based on POS tags.
- The directory "cosine-sim-per-lang" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the language.
- The directory "cosine-sim-per-topic" contains the cosine similarity values between the files of the data based on gfud DEPREL, separated depending on the topic.
- The directory "old_cosine-sim-per-topic" contains the same as "cosine-sim-per-topic", but depending on the size (i.e. number of sentences) of the topic.
- The directory "lang_structures" contains the most common language structures for each language, and the most common structures among all languages.
- "exploratory_analysis" is a notebook where I test most things.
- "cosine-sim-visualisation" is the notebook where you can visualise the cosine similarities among the data.
- "lang_structures" is a notebook where I work with the most common language structures in the directory lang_structures.
- "notes" is a markdown file where I write notes/a diary about what I do and the problems I encounter.
