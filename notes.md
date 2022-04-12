# Notes

Started with mini version of the project. Getting data with requests. 
Use BeautifulSoup with html.parser and not lxml.

TO DO 

- How will I get the urls with different languages? disambiguation problem.

Started using stanza to parse the sentences. Aarne says to use UDPipe.
Calling UDPipe's API.

TO DO 

- How will I allign the sentences that contain the same semantic information?
- What topics will I focus on?
- Read Elena's thesis to look for automatic evaluation tool for UDPipe.

03/02

On text allignment: reading "Iterative, MT-based sentence alignment of parallel texts" by Sennrich and Volk. Talking about anchor points to avoid propagating errors: "This is one of the reasons why anchor points - article boundaries in our case - are so important; they serve as boundaries to the alignment algorithm and stop the propagation of errors from one article to the next".

07/02

- Topics from the articles available in most languages?
- Getting all the relevant text in the articles, including the titles. (old)

08/02

- Made the script to call when processing the text (udparsing.py).
- Saw errors in Catalan -> bad tokenising: it did not separate "l'enciclopèdia" ('the encyclopedia') or some brakets within titles.
    - surprisingly, the article fusion does not happen in other texts! Check the Italy file parsed in Catalan.

09/02

- Tables are not parsed - do we want them? Ask Aarne --> Aarne says not to keep them, and also get rid of image captions.
- TO DO!! All the sentences are parsed as sentence_id = 1. Fix this! I should probably put everything together?
  - It's different when I run it from the website itself! But (I think) I put the same options? So, why?
- Some references (e.g. \[a]) are kept in the text. This affects the separation of sentences. Fix this! Fixed!
- ~~TO DO!!~~ Remove captions!! I don't think I take them now?

10/02

- Created script for getting html files.
- Fixed Wikipedia languages dictionary to follow UD names.
- Started script for all files.
- ~~gold standard: How to analyse "Russia (Russian: Россия, tr. Rossiya, pronounced \[rɐˈsʲijə])..."?~~
  - ~~TO DO!! I did not finish that sentence~~
  - ~~POS of Федера́ция? dependency is flat/apposition?~~
  - ~~How to do text in other languages, transcriptions...?~~
  - ~~tr. is transliteration?~~
- gold standard: I am writing all the lemmas in lower - should I? E.g. Russia russia -> decided to keep them capitalised
- gold standard: "the **ninth-most** populous country" --> how do you analyse this?!
  - ninth ninth ADJ _ _ 3 advmod  _ _ 
  - \- \- PUNCT _ _ 3 punct _ _
  - most  most  ADV _ _ 4 advmod  _ _?

11/02

- The script took forever to parse! (~20h?) But it kind of makes sense because there were a bunch of articles (61) in a bunch of languages (50-60) (total minimum of 30000) and calling an API is slow.
- ~~gold standard English: what is "second" in "second-largest city..."??? line 21 in empty_russia.conllu file. I wrote ADV because it modifies and adjective but that could be discussed... ~~
- ~~gold standard English: line 225 "Orthodox Christianity" --> compound?~~

16/02

- gold standard English: "Rus'" is the name of a place, but UDPipe separates it into Rus + '.
- ~~gold standard English: "Grand Duchy" I went with compound because it seems ot have a head, but if somebody argues it could be a flat expression, I could agree with them.~~
- gold standard English: "15th century" --> based on some other UD file, I said that 15th is an amod of century, but could it also be a nummod or a flat (date)??
- ~~gold standard English: "Russian Empire" --> I said compound of PROPN, because it's capitalised, there is a head... but could be amod and ADJ + NOUN?~~
- ~~gold standard English: line 306 - "[...]the Russian SFSR became the largest and leading **constituent** of the Soviet Union[...]" --> "It became that." --> xcomp? (not obj, right?)~~
- ~~gold standard English: "The Soviet era saw **some** of the most significant technological achievements of the 20th century, **including** the world's first human-made satellite and the launching of the first human in space."~~
  - ~~is *some* a det or a noun? I would say det, but then it is an object of *saw*, which is confusing.~~
  - ~~I said that *including* is a verb introducing an acl of *achievements*, but I saw that it could also have case as the dependency. --> it has the case dependency in the gold standard of English UDPipe EWT --> CASE, and the whole thing is an nmod ~~
- ~~gold standard English: "Following the dissolution of the Soviet Union in 1991, the newly independent Russian SFSR renamed itself the Russian Federation."~~
  - ~~Is the first part (before the comma) a subordinated clause (advcl) or is it an oblique? --> obl~~
    - ~~Can a VERB have "case" as their syntactic relation? I'm going to say yes based on what I've seen in other UD files --> YES.~~
- ~~gold standard English: "universal healthcare system" amod compound root? or is it all compound? (line 513)~~
- ~~gold standard English: "**natural** gas", amod or compound? (line 611)~~

17/02

- gold standard Spanish: working on Spanish - the references in Spanish are \[n. 1] instead of \[1] - they were not eliminated when "cleaning" the text. I am going to remove them and rewrite the documents.
  - Started at 14:44
- ~~gold standard Spanish: "Rusia, \[...] conocida como Federación de Rusia" --> I said that "como" is an ADP following other UD documents that we had for Computational Syntax, but I am very unsure about it (it's not part of the list of prep we learn in school, it sounds more like an ADV, but then I don't know how to analyse it).~~
  ~~- According to the UD Pipe Gold Standard of Ancora, "conocido como" is an ADJ and as SCONJ~~
  ~~- same in line 440, 475~~
  ~~- last sentence done like # sent_id = CESS-CAST-P-20010902-85-s2 in UDPipe Ancora Gold Standard ~~
- ~~gold standard Spanish:what do I do with "del"? Contraction of "de" + "el" --> In CompSyn we would separate them, but they are not separated in UDPipe. Should I separate it? So far, I have separated it but this will detect more errors in the UDPipe analysis.~~
- ~~gold standard Spanish: "Asia del Norte"~~
- ~~gold standard Spanish: xcomp?~~
  ~~- "equivalente a **algo más**" --> x comp? (line 116) --> nope, it's amod~~
- ~~gold standard Spanish: "formada por **ochenta y cinco sujetos federales**" (line 170) --> formada por is fixed... but obl? it's case~~ --> according to Ancora GS, "formado **por X**" is an object, not an oblique!! and "formado" is an adjective
- ~~gold standard Spanish: is "exist" a root or is it a cop? (line 202)~~ --> it's a verb but it has only an nsubj

18/02

- ~~gold standard Spanish: "República Popular China"~~ --> Apparently, NOUN ADJ NOUN, ... amod appos!
- ~~gold standard Spanish: "limita con los siguientes países: bla, ble, bli..." parataxis? appos?~~ --> apparently, appos
- gold standard Spanish: line 471 --> two sentences were not separated because the full stop of aC and the end of the sentence is the same. 
- ~~gold standard Spanish: "llamados varegos" --> I put llamados as cop and varegos as acl, based on another UD file, but at the beginning I had that llamados was an acl and varegos an xcomp. Which one?~~ --> I do not think it makes much sense, but according to AnCora it is: llamados (ADJ) varegos (NOUN, obj). Similar to "formados por X". How can adjectives have objects?
- ~~gold standard Spanish: "adoptaron el cristianismo, producto de..." --> appos? xcomp?~~ --> appos, according to # sent_id = CESS-CAST-P-19991001-59-s2
- ~~gold standard Spanish: line 615, should we separate the PROPN "Vladímir-Súzdal"? I separated it and put it as flat.~~ --> I shouldn't have, I have fixed it. 

21/02

- gold standard French: "Pour les articles homonymes, voir Russie (**homonymie**) et Russia (**homonymie**)." --> I put nmod, because it's just the disambiguation page for the French Wikipedia. Should it be appos? 
- gold standards French: "Россия, Rossiïa prononciation" appos, flat to prononciation, nmod to Россия? idk 
- ~~gold standards French: "La Russie \[...] est un État \[...] **à cheval** sur l'Asie du Nord \[...] et sur l'Europe..." --> it's a fixed expression, I said nmod of "État", but what is "sur X" modiying? I put it as "à cheval sur X et sur Y", so sur X et sur Y would be nmods of cheval - but it is VERY arguable, they could also be other nmods of État and "à cheval" be another complement~~
- ~~gold standards French: "La Russie \[...] est un État fédéral transcontinental \[...] à cheval sur l'Asie du Nord **(80 % de sa superficie)** et sur l'Europe **(20 %)**." --> what are these? "80% de la superficie de Russie est sur l'Asie du Nord" --> I put nmod of Asie and Europe.~~ --> appos 
- same structure in Spanish and French (se + VERB) the pronouns "se" have different dependencies --> compound:prt or obj.
- ~~gold standards French: mer Baltique --> NOUN PROPN (compound) or just NOUN ADJ (nmod)? line 150. In Spanish and English I think I put everything as PROPN. Should I do it differently for French?~~ --> followed french ud file
- FRENCH FILE: I am missing some text!!!! 
  - "Limitrophe de l'Océan Arctique au nord, la Russie est caractérisée par un climat continental avec des hivers particulièrement froids et hostiles sur une grande partie du territoire, notamment en Sibérie, à l'est de l'Oural. La population russe est estimée à près de 146 millions d'habitants en 20211 ce qui en fait le neuvième pays le plus peuplé de la planète. 78 % de ses habitants vivent en Europe6." <-- Second and third sentence from second paragraph.
  - I know why --> some lines do not have the <\p> tags. I need to rerun the code. 
  - get_html_paragraph.py --> I need to use the .findall!! Different approach. I need the <\p> for the paragraphs, but I should also get the titles for alligning the text! The problem is that the titles have different tags, like <\h2>... I need to take a good look at it.

22/02

- Meeting with Aarne to fix missing the text. Very helpful! 😊

23/02

- Fixing script for the Wikipedia articles with most text. I decide to get rid of everything inside square brackets, because it's (from what I've seen) "edit".

24/02
- Trying to get rid of text that I'm getting but I do not want (from the infobox, etc.)

28/02

- Getting rid of the things in between square brackets was not the smartes thing to do - now I do not have any pronounciation -> I'm gonna do it again. Oops!
  - Pronunciations: Russia (Russian: Россия, tr. Rossiya, pronounced **\[rɐˈsʲijə\])**, or the Russian Federation, is a country spanning Eastern Europe and Northern Asia.
  - \[cite required\]
  - parts of some text that are missing: Peter Harvey also agrees that “much” of the Pali Canon “must derive from his **\[the Buddha's\]** teachings.” Likewise, A. K. Warder has written that “there is no evidence to suggest that it **\[the shared teaching of the early schools\]** was formulated by anyone other than the Buddha and his immediate followers.”
- Since I reran the data, now I have to get the gold standard in the same format... so I have to check everything (some articles were edited too)


01/03

- rerunning main script keeping \[things inside square brackets\] (except for references like \[a\], \[1\], \[n. 1\]).
- ~~gold standard English: line 315 ?? xcomp??~~

03/03

- ~~gold standard French: "à près de 146 millions..." (line 247)--> following the structure of # newdoc id = w01026 # sent_id = w01026024 in fr_pud-ud-test.conllu --> Is the dependency of "près" case or advmod of 146? I'd say the latter.~~
- gold standard French: "le plus peuplé" (line 270) --> following the same file, decided on DET of plus, advmod of peuplé --> some people say "le plus" is det and fixed, some others say it's det and advmod. Since the exact phrase is in the Gold Standard, I'm gonna go with the analysis in there
- ~~gold standard French: "La Révolution russe **consécutive** \[à la Première Guerre mondiale\]" --> amod of "consécutive"?~~ --> based of GS of UDPipe, it's obl of an adjective
- problem (maybe): sentence ids repeat themselves for every paragraph!

TO DO 
- Look if elements in brackets contain heads of elements outside the brackets. Do the brackets change the parsing of the sentence? Is it connected correctly?
- Labelled accuracy score (check GFUD - computational syntax) --> check UDPipe!!
  - 0 for sentences that have been separated wrong? --> keep statistics of how many were badly split
  - ignore them?
  - relable 
- ~~Orthodox Christianity --> ADJ NOUN, amod of Christianity~~
- ~~Look at the goldstandard treebanks for these details!! (if they are consistent)~~
- ~~UD documentation --> do they number paragraphs? or have unique ids for sentences?~~ unique ids for sentences

07/03 + 08/03

- Fixing previous UD mistakes checking the UDPipe Gold Standard
- gold standard French: line ~585 I had never seen such a construction, with "dont" and no verb, but following the UDPipe GS for French, I will put it as an acl:relcl.
- Fixing sentence ID and new paragraphs, adding changes to GS.

09/03

- Found problem with using VSC to write Gold Standard --> instead of tabs, I get spaces. Fixing with script change_to_tabs.py.
- [gusgraupa@GU.GU.SE@eduserv gold_standard]$ gfud eval macro LAS Russia_english_gold_standard.conllu Russia_english_intro_UDPipe.conllu
- evaluating macro LAS Russia_english_gold_standard.conllu Russia_english_intro_UDPipe.conllu
- gfud: ERROR:obl invalid UDId
- CallStack (from HasCallStack):
  - error, called at UDConcepts.hs:145:12 in main:UDConcepts
- [gusgraupa@GU.GU.SE@eduserv gold_standard]$ gfud eval macro LAS Russia_spanish_gold_standard.conllu Russia_spanish_intro_UDPipe.conllu
- evaluating macro LAS Russia_spanish_gold_standard.conllu Russia_spanish_intro_UDPipe.conllu
- gfud: ERROR:conj invalid UDId
- CallStack (from HasCallStack):
  - error, called at UDConcepts.hs:145:12 in main:UDConcepts
- [gusgraupa@GU.GU.SE@eduserv gold_standard]$ gfud eval macro LAS Russia_french_gold_standard.conllu Russia_french_intro_UDPipe.conllu
- evaluating macro LAS Russia_french_gold_standard.conllu Russia_french_intro_UDPipe.conllu
- gfud: ERROR:acl:relcl invalid UDId
- CallStack (from HasCallStack):
  - error, called at UDConcepts.hs:145:12 in main:UDConcepts

10/03 and 11/03

- Tried to create virtual environment for GF and GFUD, ran into a million problems with dependencies and permissions.
- Found the cause of the error of the gfud eval, realised I have to change some things again.
  - scripts/fixing_scripts/fixing_conllu_for_eval.py for all files
- I used LAS. From the grammarbook:

The evaluation metrics measures the agreement between dependency trees:
what percentage of words have been labelled correctly. There are two variants:
- Labelled Attachment Score (LAS): \correctly" means that both the
head (i.e.n the position number of the head) and the label to be tested
are equal to the head and label in the gold standard.
- Unlabelled Attachment Score (UAS): \correctly" means only that
the head to be tested is equal to the head in the gold standard.
The UAS score is obviously always at least as high as LAS.

- Cosine similarity among languages. --> script failed

14/03

- Ancora (Spanish Treebank) doesn't use compound:prt for passives. Changing it to expl:pv or expl:pass.
  - Reflexive pronouns (see the feature Reflex) usually replace objects of verbs. However, some verbs are inherently reflexive, i.e. the verb always occurs with a reflexive prounoun, and the pronoun cannot be replaced by a non-reflexive pronoun.
  - If the verb is in the treebank, I use the same tag. Otherwise, I choose bewteen expl:pass and expl:pv depending on the previous definition.
  - Consejo de Seguridad de las Naciones Unidas. Naciones Unidas is flat according to the Ancora treebank, but I thought it should be NOUN ADJ and ... amod.

31/03

The problem with using the number-token correspondance to check head alignment is that two words might have
the same form but not refer to the same element (head). In a very specific example talking about Matryoshka dolls:
```
A)
                 (head)
- GOLD STANDARD                            - PARSED (incorrect)
- 1  the     DET    2    det               - 1  the     DET    2    det
- 2  doll    NOUN   0    root              - 2  doll   NOUN    0    root
- 3  in      ADP    5    case              - 3  in      ADP    5    case
- 4  the     DET    5    det               - 4  the     DET    5    det
- 5  doll    NOUN   2    nmod              - 5  doll    NOUN   2    nmod
- 6  ,       PUNCT  9    punct             - 6  ,       PUNCT  9    punct
- 7  in      ADP    9    case              - 7  in      ADP    9    case
- 8  the     DET    9    det               - 8  the     DET    9    det
- 9  ugly    ADJ    10   amod              - 9  ugly    ADJ    10   nmod
- 10 one     NOUN   5    appos             - 10 one     NOUN   2    nmod 
```
The last token (10, "one") in both cases reffers to "doll", but to different words! So it would be marked as
correct, even though it is not. However, working with the heads can be very hard when there are missing elements,
such as this example:

B)
```
- GOLD STANDARD                            - PARSED
- 1     El      DET   2    det             - 1  el        DET   2    det
- 2     chico   NOUN  0    root            - 2  chico     NOUN  0    root
- 3-4   del                                - 3  del       ADP   4    case
- 3     de      ADP   5    case                     
- 4     el      DET   5    det                    
- 5     mercado NOUN  2    nmod            - 4  mercado   NOUN  2    nmod --> no change in head
- 6-7   del                                - 5  del       ADP   7    case
- 6     de      ADP   9    case
- 7     el      DET   9    det
- 8     otro    ADJ   9    amod            - 6  otro      ADJ   7    amod --> add 2
- 9     lado    NOUN  5    nmod            - 7  lado      NOUN  4    nmod --> add 1
- 10-11 del                                - 8  del       CASE  9    case
- 10    de      ADP   12   case
- 11    el      DET   12   det
- 12    valle   NOUN  9    nmod            - 9  valle     NOUN  7    nmod --> add 2
- 13    verde   ADJ   12   amod            - 10 verde     ADJ   9    amod --> add 3
```

It is not enough to add the number of missing lines to check for missalignments, because there are heads
which refer to words previous to the missing lines, which should not need to get number of lines added. 
Depending on what the head is refering to, we might need to add 1, 2, 3... to make the number align.

I am going to try to make it work with the first way (A) while getting (LAS) scores and ordering them de-
pending on the number of errors.


04/04 + 05/04

I realised that there will be an issue with the mapping writing, given that a sentence might have been formed by joining other sentences, which can lead to this:

```
- GOLD STANDARD                                 - PARSED TEXT
- 1  In        ADP     3     case               - 1  In        ADP     3     case
- 2  the       DET     3     det                - 2  the       DET     3     det
- 3  year      NOUN    7     obl                - 3  year      NOUN    0     root  
- 4  2         NUM     5     nummod             - 4  2         NUM     5     nummod
- 5  a.C.      NOUN    3     nmod               - 5  a.C.      NOUN    3     nmod
- 6  he        PRON    7     nsubj              - 1  he        PRON    2     nsubj
- 7  was       AUX     8     cop                - 2  was       AUX     3     cop
- 8  famous    ADJ     0     root               - 3  famous    ADJ     0     root
```
There are two elements that refer to 1, two that refer to 2 and two more that map to 3. 


I went back to case B), working with heads instead of the mapping dictionary. There IS one case that does not work, which is when there are missing lines in text that has not been parsed already (spanish sent_id = 21). Fixed.

12/04

- In Spanish:
- "Federación de Rusia" has a flat dependency in the UD Treebanks for Ancora, so I had to chage it to flat, even though for me it is clearly an nmod.
- Regarding # sent_id = 7 in Spanish:
  - In Ancora Treebank: # sent_id = CESS-CAST-A-20000413-10268-s9, "partidos sin ganar" is acl with mark, same with "sin vencer" in # sent_id = CESS-CAST-A-20000416-12803-s21, but in # sent_id = CESS-CAST-A-20000416-12803-s28, "sin perder" is xcomp with mark.
  - I am going to go with acl with mark, because it seems to be more common.
  - "es considerada la mayor superpotencia energética" I think "la mayor superpotencia energética" should be an xcomp, but based on the Ancora Treebank it should be an obj. So I wrote obj.
- "Estados Unidos" is flat according to the Ancora Treebank. 
- in sent_id = 11, the structure of "en concreto, con el estado de Alaska" is based on # sent_id = CESS-CAST-A-20001013-10127-s13 in the Ancora Treebank.
- Regarding # sent_id = 19: "se convirtió en la fuerza principal..." I put obj, not obl, based on Ancora.
- Regarding # sent_id = 12, "Unión de Repúblicas Populares" is flat and not nmod based on Treebank, # sent_id = 3LB-CAST-211_C-5-s17.
- On sentence 16, "Europa Occidental" was changed from amod to flat based on the Treebank.
- "siglo XXI" (or any other century) is sometimes a compound, a flat, an nmod, an appos... in the Ancora Treebank. I chose compound because it seems to be the most common. Same with "en el año Y" ('in the year Y'), it is a compound. I would have said nummod, but it's not what they choose in the Treebank.
- sent_id = 17 "llevada a cabo" it is a compound, not fixed (apparently).

- It seems that the annotators of the Ancora Treebank use "flat" very often.

- In English:
- "Russian Federation" appears twice in the ewt Treebank, one as a a compound and one as an amod.