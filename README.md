# bibfind
 Script for looking up bible passages on the command line 


# Usage 
```  
usage: main.py [-h] [-t] [-a] [-l] [-s [<book/all> <keyword> ...]] [-f [verses ...]] [-r book]

Lookup a bible passage on the command line

options:
  -h, --help            show this help message and exit
  -t, --translations    List all the availible translations of the bible
  -a, --abbrvs          List all the explicit abbreviations of each bible book (dictionary data
                        structure)
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

### Finding a bible verse 
``` 
python main.py -f John 3:15
15 That whosoever believeth in him, may not perish, but may have life everlasting.
```

``` 
python main.py -s ALL Judas
...
Acts 15:32-36
34 But it seemed good to Silas to remain there: and Judas alone set out for Jerusalem.

Found 161 instance(s) of 'Judas'
```

### Searching for a keyword 

``` 
python main.py -s NewTestament Judas
...
Found 128 instance(s) of 'Judas' in the NT
```


``` 
python main.py -s "3 John" Church 

3 John 1:8-12
...
10 Wherefore, if I come, I will admonish his works which he doth, prating against us with malicious words: and as if these things were not enough for him, neither doth he himself receive the brethren: and those that do receive them he forbiddeth, and casteth out of the church.
...


Found 3 instance(s) of 'Church' in 3 John
```
# Smart Lookup 
- Bible books passed in as arguments will first try to match with an *explicit* abbrevation found in `abbrv.py`.

```python
{
  "Genesis": ['Gen', 'Ge', 'Gn']},
  # ...
  'Matthew': ['Matt', 'Mt'], 
  'Mark': ['Mrk', 'Mar', 'Mk', 'Mr'], 
  'Luke': ['Luke', 'Luk', 'Lk'], 
  'John': ['Joh', 'Jhn', 'Jn'], 
  'Acts': ['Act', 'Ac'], 
}
```
- These explicit abbreviations can be changed or added to.

- If no abbrevation is found it will match to the most similar book *implicitly*.


# Line Proximity 
- You can change the amount of verses printed proximate to a found keyword in the bibfind init function.


``` python 
self.line_proximity = 3 # will print so many lines before and after found keyword 
```


# Changing the translation
- You can choose a translation from the bibles folder and pass it in when intializing the class
  - Example in `main.py`: 
``` python 
b1 = bib_find.bibfind(r"bib_find\bibles\EntireBible-DR.json")
 ```

 ## Adding your Own Translation 
 - If you want to add a new translation, it must be a json file and have the following format
  
Example of the format 
``` json
{
 "Genesis": // Book Name
  {
   "1": // Chapter Number
     {
      "1": "In the *beginning God created heaven and earth.", // verses 
      "2": "*And the earth was void and empty, and darkness was upon the face of the deep: and   the   Spirit of God moved over the waters.",
      "3": "And God said: *Be light made. And light was made.",
     }
  }
}

```

