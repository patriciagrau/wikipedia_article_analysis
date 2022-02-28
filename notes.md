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
- gold standard: How to analyse "Russia (Russian: Россия, tr. Rossiya, pronounced \[rɐˈsʲijə])..."?
  - TO DO!! I did not finish that sentence
  - POS of Федера́ция? dependency is flat/apposition?
  - How to do text in other languages, transcriptions...?
  - tr. is transliteration?
- gold standard: I am writing all the lemmas in lower - should I? E.g. Russia russia -> decided to keep them capitalised
- gold standard: "the **ninth-most** populous country" --> how do you analyse this?!
  - ninth ninth ADJ _ _ 3 advmod  _ _ 
  - \- \- PUNCT _ _ 3 punct _ _
  - most  most  ADV _ _ 4 advmod  _ _?

11/02

- The script took forever to parse! (~20h?) But it kind of makes sense because there were a bunch of articles (61) in a bunch of languages (50-60) (total minimum of 30000) and calling an API is slow.
- gold standard English: what is "second" in "second-largest city..."??? line 21 in empty_russia.conllu file. I wrote ADV because it modifies and adjective but that could be discussed...
- gold standard English: line 225 "Orthodox Christianity" --> compound?

16/02

- gold standard English: "Rus'" is the name of a place, but UDPipe separates it into Rus + '.
- gold standard English: "Grand Duchy" I went with compound because it seems ot have a head, but if somebody argues it could be a flat expression, I could agree with them.
- gold standard English: "15th century" --> based on some other UD file, I said that 15th is an amod of century, but could it also be a nummod or a flat (date)??
- gold standard English: "Russian Empire" --> I said compound of PROPN, because it's capitalised, there is a head... but could be amod and ADJ + NOUN?
- gold standard English: line 306 - "[...]the Russian SFSR became the largest and leading **constituent** of the Soviet Union[...]" --> "It became that." --> xcomp? (not obj, right?)
- gold standard English: "The Soviet era saw **some** of the most significant technological achievements of the 20th century, **including** the world's first human-made satellite and the launching of the first human in space." 
  - is *some* a det or a noun? I would say det, but then it is an object of *saw*, which is confusing. 
  - I said that *including* is a verb introducing an acl of *achievements*, but I saw that it could also have case as the dependency.
- gold standard English: "Following the dissolution of the Soviet Union in 1991, the newly independent Russian SFSR renamed itself the Russian Federation."
  - Is the first part (before the comma) a subordinated clause (advcl) or is it an oblique?
    - Can a VERB have "case" as their syntactic relation? I'm going to say yes based on what I've seen in other UD files.
- gold standard English: "universal healthcare system" amod compound root? or is it all compound? (line 513)
- gold standard English: "**natural** gas", amod or compound? (line 611)

17/02

- gold standard Spanish: working on Spanish - the references in Spanish are \[n. 1] instead of \[1] - they were not eliminated when "cleaning" the text. I am going to remove them and rewrite the documents.
  - Started at 14:44
- gold standard Spanish: "Rusia, \[...] conocida como Federación de Rusia" --> I said that "como" is an ADP following other UD documents that we had for Computational Syntax, but I am very unsure about it (it's not part of the list of prep we learn in school, it sounds more like an ADV, but then I don't know how to analyse it).
  - same in line 440, 475
- gold standard Spanish:what do I do with "del"? Contraction of "de" + "el" --> In CompSyn we would separate them, but they are not separated in UDPipe. Should I separate it? So far, I have separated it but this will detect more errors in the UDPipe analysis.
- gold standard Spanish: "Asia del Norte" --> I said PROPN de el PROPN
- gold standard Spanish: xcomp?
  - "equivalente a **algo más**" --> x comp? (line 116)
- gold standard Spanish: "formada por **ochenta y cinco sujetos federales**" (line 170) --> formada por is fixed... but obl?
- gold standard Spanish: is "exist" a root or is it a cop? (line 202)

18/02

- gold standard Spanish: "República Popular China" PROPN PROPN PROPN or PROPN ADJ PROPN?
- gold standard Spanish: "limita con los siguientes países: bla, ble, bli..." parataxis? appos?
- gold standard Spanish: line 471 --> two sentences were not separated because the full stop of aC and the end of the sentence is the same. 
- gold standard Spanish: "llamados varegos" --> I put llamados as cop and varegos as acl, based on another UD file, but at the beginning I had that llamados was an acl and varegos an xcomp. Which one?
- gold standard Spanish: "adoptaron el cristianismo, producto de..." --> appos? xcomp?
- gold standard Spanish: line 615, should we separate the PROPN "Vladímir-Súzdal"? I separated it and put it as flat.

21/02

- gold standard French: "Pour les articles homonymes, voir Russie (**homonymie**) et Russia (**homonymie**)." --> I put dep, because it's just the disambiguation page for the French Wikipedia. Should it be appos? 
- gold standards French: "Россия, Rossiïa prononciation" appos, flat to prononciation, nmod to Россия? idk 
- gold standards French: "La Russie \[...] est un État \[...] **à cheval** sur l'Asie du Nord \[...] et sur l'Europe..." --> it's a fixed expression, I said nmod of "État", but what is "sur X" modiying? I put it as "à cheval sur X et sur Y", so sur X et sur Y would be nmods of cheval - but it is VERY arguable, they could also be other nmods of État and "à cheval" be another complement
- gold standards French: "La Russie \[...] est un État fédéral transcontinental \[...] à cheval sur l'Asie du Nord **(80 % de sa superficie)** et sur l'Europe **(20 %)**." --> what are these? "80% de la superficie de Russie est sur l'Asie du Nord" --> I put nmod of Asie and Europe.
- same structure in Spanish and French (se + VERB) the pronouns "se" have different dependencies --> compound:prt or obj.
- gold standards French: mer Baltique --> NOUN PROPN (compound) or just NOUN ADJ (nmod)? line 150. In Spanish and English I think I put everything as PROPN. Should I do it differently for French?
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