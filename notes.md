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
- Getting all the relevant text in the articles, including the titles.

08/02

- Made the script to call when processing the text (udparsing.py).
- Saw errors in Catalan -> bad tokenising: it did not separate "l'enciclopèdia" ('the encyclopedia') or some brakets within titles.