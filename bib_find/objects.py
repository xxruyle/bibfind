import json 
import re 
import os
import random
from bib_find.abbrv import bible_abrvs

# The absolute path which contains the bible translations
dirname = os.path.dirname(__file__)
biblefolder = os.path.join(dirname, "bibles")

class bibfind():
    def __init__(self, translation):
        with open(translation, 'r', encoding="UTF-8") as f:
            self.bible = json.load(f)
            

        self.list_books = list(self.bible)
        self.line_proximity = 3  # will print so many lines before and after found keyword verse-line  
        self.list_translations = '\n'.join(os.listdir(biblefolder))
        self.OldTestament = []
        self.NewTestament = []
        
        matthewindex = self.list_books.index("Matthew")
        for i, book in enumerate(self.list_books): 
            if book == "Matthew" or i >= matthewindex:
                self.NewTestament.append(book)
            else:
                self.OldTestament.append(book)

    def parse_citation(self, passage):
        '''
        Parses the user input in accessible format for bible citation

        :return: a list of strings

        :example:

        >>> parse_citation("John 1:1")
        >>> [John, 1, 1]
        '''
        if passage[0].isdigit():
            init = passage.split(' ', 2)
            parsed = re.split('[:-]+', init[2])
            book = passage[0] + ' '+ init[1]
            parsed.insert(0, book)
        #EX: John 1:2 
        else:
            init = passage.split(' ', 1)
            parsed = re.split('[:-]+', init[1])
            parsed.insert(0, init[0])

        return parsed 

    #
    def smart_lookup(self, string):
        '''
        If a book is passed in incorrectly it will first try to match it to an abbrevation found in abbrv.py.
        If no abbrevation is found it will match to the most similar book.

        :return: The most similar name of a book in the bible

        >>> smart_lookup("Gen")
        >>> "Genesis"  
        '''
        bible_books = list(self.bible)
        for book in bible_books: 
            for abbrev in bible_abrvs[book]:
                if string.upper() == abbrev.upper():
                    return book 
            if string.upper() in book.upper():
                return book 

    def get_verse(self, passage):
        '''
        Looks up the verse from the json file 

        :param passage: Proper bible citation format 
        
        :example:

        >>> get_verse("John 1:1")
        :prints: str
        John 1:1
        1 In the beginning was the Word, and the Word was with God, and the Word was God.
        
        '''
        parsed = self.parse_citation(passage)
        bible_book = self.smart_lookup(parsed[0])
        # EX Genesis 
        if len(parsed) == 1:
            for key in self.bible[bible_book]:
                print(f"{bible_book} {parsed[1]}:{parsed[2]}")
                for j in self.bible[bible_book][key]:
                    print(f"{j} {self.bible[bible_book][key][j]}\n")
        # Genesis 1
        elif len(parsed) == 2: 
            print(f"{parsed[0].capitalize()} {parsed[1]}")
            for key in self.bible[bible_book][parsed[1]]:
                print(f"{key} {self.bible[bible_book][parsed[1]][key]}") 

        # Genesis 1:1
        elif len(parsed) == 3:  
            print(f"{bible_book} {parsed[1]}:{parsed[2]}")
            print(f"{parsed[2]} {self.bible[bible_book][parsed[1]][parsed[2]]}\n")

        # Gensis 1:1-2
        elif len(parsed) == 4:
            print(f"{bible_book} {parsed[1]}:{parsed[2]}-{parsed[3]}")
            for key in self.bible[bible_book][parsed[1]]:
                if int(key) >= int(parsed[2]) and int(key) <= int(parsed[3]):
                    print(f"{key} {self.bible[bible_book][parsed[1]][key]}")

        else:
            print("String not proper citation format")

    def format_verses(self, bib_book, chapter, verse): 
        '''
        used in search_key to print out the found verses pretty.

        :param bib_book: the book 
        :param chapter: the chapter
        :param verse: the verse 
        '''
        int_verse = int(verse)
        if str(int_verse - self.line_proximity) in self.bible[bib_book][chapter] and str(int_verse + self.line_proximity) in self.bible[bib_book][chapter]:
            print(f"{bib_book} {chapter}:{str(int_verse - self.line_proximity + 1)}-{str(int_verse + self.line_proximity - 1)}")
            for j in reversed(range(0, self.line_proximity)):
                print(f"{str(int_verse - j)} {self.bible[bib_book][chapter][str(int_verse - j)]}")
            for i in range(1, self.line_proximity):
                print(f"{str(int_verse + i)} {self.bible[bib_book][chapter][str(int_verse + i)]}")
            print("\n")
        else:
            print(f"{bib_book} {chapter}:{verse}")
            print(f"{verse} {self.bible[bib_book][chapter][verse]}\n")

 
    def search_key(self, book, keyword):
        '''
        Returns verses (and the verses proximate to them) which contain the keyword argument
        :param book: Takes either a single 'book' or 'all' or 'NT' or 'OT' in the bible
        :param keyword: The word you want to search for in stated book parameter 

        :Example:

        >>> search_key("ALL", "Jesus")
        :returns: found 938 instance(s) of 'Jesus'
        '''
        bible_book = self.smart_lookup(book)
        count = 0
        if book.upper() == "ALL" or book.upper() == "OT" or book.upper() == "NT":
            if book.upper() == "ALL":
                biblist = self.bible
            elif book.upper() == "OT" or book.upper() == "OLDTESTAMENT" or book.upper() == "OLD TESTAMENT":
                biblist = self.OldTestament
            elif book.upper() == "NT" or book.upper() == "NEWTESTAMENT" or book.upper() == "NEW TESTAMENT":
                biblist = self.NewTestament
            for b in biblist:
                for chapter in self.bible[b]:
                    for verse in self.bible[b][chapter]:
                        if keyword.upper() in self.bible[b][chapter][verse].upper():
                            # Formatting 
                            self.format_verses(b, chapter, verse)
                            count += 1
            print(f"Found {count} instance(s) of '{keyword}' in {book}")          

        else:                    
            for chapter in self.bible[bible_book]:  # Loops through each chapter in a bible book 
                for verse in self.bible[bible_book][chapter]: # Loops through each verse in a bible book chapter 
                    if keyword.upper() in self.bible[bible_book][chapter][verse].upper(): 
                        self.format_verses(bible_book, chapter, verse)
                        count += 1
            print(f"Found {count} instance(s) of '{keyword}' in {bible_book}") 


    def random_format(self, randomBook):
        '''
        used in random_verse to print out verses pretty 
        '''
        randomChapter = random.choice(list(self.bible[randomBook]))
        randomVerse = random.choice(list(self.bible[randomBook][randomChapter]))
        print(f"{randomBook} {randomChapter}:{randomVerse}")
        print(self.bible[randomBook][randomChapter][randomVerse])

    def random_verse(self, book):
        '''
        Returns a random verse in the bible or returns a random verse from a specific book 

        @param book: Either pass in "ALL", "OT", "NT", or "{book}"

        :example:

        >>> random_verse("ALL")
        :returns: 
        >>> 
        1 John 5:1
        Every one who believeth that Jesus is the Christ, is born of God. And every one that loveth him that begot, loveth him also who was born of him.

        >>> random_verse("Matthew")
        :returns: 
        >>> 
        Matthew 2:8
        And sending them into Bethlehem, said: Go, and search diligently after the child; and when you have found him, bring me word again, that I also may come and adore him.
        '''
        if book.upper() == "OT" or book.upper() == "OLDTESTAMENT" or book.upper() == "OLD TESTAMENT":
            randomBook = random.choice(self.OldTestament)
            self.random_format(randomBook)
        elif book.upper() == "NT" or book.upper() == "NEWTESTAMENT" or book.upper() == "NEW TESTAMENT":
            randomBook = random.choice(self.NewTestament)
            self.random_format(randomBook)
        elif book.upper() == "ALL":
            randomBook = random.choice(self.list_books)
            self.random_format(randomBook)
        else:
            randomBook = random.choice(self.list_books)
            bookChoice = self.smart_lookup(book)
            randomChapter = random.choice(list(self.bible[bookChoice]))
            randomVerse = random.choice(list(self.bible[bookChoice][randomChapter]))
            print(f"{bookChoice} {randomChapter}:{randomVerse}")
            print(self.bible[bookChoice][randomChapter][randomVerse])
            




            
