# bibfind
 Script for looking up bible passages on the command line 


# Usage 
```
usage: main.py [-h] [-l] [-s [book/all, keyword [book/all, keyword ...]]] [-r [read [read ...]]]

Lookup a bible passage on the command line

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List all the books of the bible
  -s [book/all, keyword [book/all, keyword ...]], --search [book/all, keyword [book/all, keyword ...]]
                        Returns verses (and the verses proximate to them) which contain the keyword argument
  -r [read [read ...]], --read [read [read ...]]
                        <Book> <Chapter>:<Verse>-<Verse>
```

# Examples of Usage
```
python main.py -r John 3:15
15 That whosoever believeth in him, may not perish, but may have life everlasting.
```

```
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

```
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
```
b1 = bib_find.bibfind(r"bib_find\bibles\EntireBible-DR.json")
 ```