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
- TO DO!! Remove captions!!

10/02

- Created script for getting html files.
- Fixed Wikipedia languages dictionary to follow UD names.
- Started script for all files.
- gold standard: How to analyse "Russia (Russian: Россия, tr. Rossiya, pronounced \[rɐˈsʲijə])..."?
  - TO DO!! I did not finish that sentence
- gold standard: I am writing all the lemmas in lower - should I? E.g. Russia russia -> decided to keep them capitalised
- gold standard: "the **ninth-most** populous country" --> how do you analyse this?!
  - ninth ninth ADJ _ _ 3 advmod  _ _ 
  - \- \- PUNCT _ _ 3 punct _ _
  - most  most  ADV _ _ 4 advmod  _ _?

11/02

- The script took forever to parse! (~20h?) But it kind of makes sense because there were a bunch of articles (61) in a bunch of languages (50-60) (total minimum of 30000) and calling an API is slow.
- gold standard: what is "second" in "second-largest city..."??? line 21 in empty_russia.conllu file. I wrote ADV because it modifies and adjective but that could be discussed...
- gold standard: line 225 "Orthodox Christianity" --> I put 'Orthodox' as an adjective, so an amod to Christianity, but it could be a flat or a compound???

16/02

- gold standard: "Rus'" is the name of a place, but UDPipe separates it into Rus + '.
- gold standard: "Grand Duchy" I went with compound because it seems ot have a head, but if somebody argues it could be a flat expression, I could agree with them.
- gold standard: "15th century" --> based on some other UD file, I said that 15th is an amod of century, but could it also be a nummod or a flat (date)??
- gold standard: "Russian Empire" --> I said compound of PROPN, because it's capitalised, there is a head... but could be amod and ADJ + NOUN?
- gold standard: line 306 - "[...]the Russian SFSR became the largest and leading **constituent** of the Soviet Union[...]" --> "It became that." --> xcomp? (not obj, right?)
- gold standard: "The Soviet era saw **some** of the most significant technological achievements of the 20th century, **including** the world's first human-made satellite and the launching of the first human in space." 
  - is *some* a det or a noun? I would say det, but then it is an object of *saw*, which is confusing. 
  - I said that *including* is a verb introducing an acl of *achievements*, but I saw that it could also have case as the dependency.
- gold standard: "Following the dissolution of the Soviet Union in 1991, the newly independent Russian SFSR renamed itself the Russian Federation."
  - Is the first part (before the comma) a subordinated clause (advcl) or is it an oblique?
    - Can a VERB have "case" as their syntactic relation? I'm going to say yes based on what I've seen in other UD files.
- gold standard: "universal healthcare system" amod compound root? or is it all compound? (line 513)
- gold standard: "**natural** gas", amod or compound? (line 611)