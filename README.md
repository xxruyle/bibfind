# bibfind
 Script for looking up bible passages on the command line 


# Usage 
```  
usage: main.py [-h] [-t] [-l] [-s [<book/all> <keyword> ...]] [-f [verses ...]] [-r book]

Lookup a bible passage on the command line

options:
  -h, --help            show this help message and exit
  -t, --translations    List all the availible translations of the bible
  -l, --list            List all the books of the bible
  -s [<book/all> <keyword> ...], --search [<book/all> <keyword> ...]
                        Returns verses (and the verses proximate to them) which contain the keyword
                        argument. EX: -s ALL God, -s Matthew Jesus
  -f [verse(s) ...], --find [verse(s) ...]
                        <Book> <Chapter>:<Verse>-<Verse>
  -r book, --random book
                        Look up a random passage from the bible. EX: -r ALL, -r OT, -r NT, -r Matthew
```

# Examples of Usage
``` JSON
python main.py -f John 3:15
15 That whosoever believeth in him, may not perish, but may have life everlasting.
```

``` JSON
python main.py -s ALL Judas

...
Acts 15:32-36
32 But Judas and Silas, being prophets also themselves, comforted the brethren with many words, and confirmed them.
33 And having remained there some time, they were dismissed with peace, by the brethren, to those who had sent them.
34 But it seemed good to Silas to remain there: and Judas alone set out for Jerusalem.
35 And Paul and Barnabas continued at Antioch, teaching and preaching with many others the word of the Lord.
36 *And after some days, Paul said to Barnabas: Let us return and visit the brethren in all the cities, wherein we have preached the word of the Lord, to see how they do.


Found 161 instance(s) of 'Judas'
```

``` JSON
python main.py -s NewTestament Judas
...
Found 128 instance(s) of 'Judas' in the NT
```


``` JSON
python main.py -s "3 John" Church 

3 John 1:8-12
...
10 Wherefore, if I come, I will admonish his works which he doth, prating against us with malicious words: and as if these things were not enough for him, neither doth he himself receive the brethren: and those that do receive them he forbiddeth, and casteth out of the church.
11 Dearly beloved, follow not that which is evil, but that which is good. He that doth good, is of God: he that doth evil, hath not seen God.
...


Found 3 instance(s) of 'Church' in 3 John
```

# Changing the translation
- You can choose a translation from the bibles folder and pass it in when intializing the class
  - Example in main.py: 
``` python 
b1 = bib_find.bibfind(r"bib_find\bibles\EntireBible-DR.json")
 ```