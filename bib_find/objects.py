import json 
import re 
from os import listdir

class bibfind():
    def __init__(self, translation):
        with open(translation, 'r', encoding="UTF-8") as f:
            self.bible = json.load(f)
            

        self.list_books = list(self.bible)
        self.line_proximity = 3  # will print so many lines before and after found keyword 
        self.list_translations = '\n'.join(listdir("bibles"))

    # Parses the user input 
    #def parse_citation(self, passage):
    #    init = passage.split(' ', 1)
    #    parsed = re.split('[:-]+', init[1])
    #    parsed.insert(0, init[0])
    #    return parsed 

    def parse_citation(self, passage):
        #EX: 1 John 1:2 
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

    #If a book is passed in incorrectly it will match to the most similar book (i.e "Gen" = "Genesis")
    def smart_lookup(self, string):
        bible_books = list(self.bible)
        for book in bible_books:
            if string.upper() in book.upper(): 
                return book  

    # Looks up the verse from the json file 
    def get_verse(self, passage):
        parsed = self.parse_citation(passage)
        display_input = ' '.join(parsed)
        bible_book = self.smart_lookup(parsed[0])
        # EX Genesis 
        if len(parsed) == 1:
            for key in self.bible[bible_book]:
                print(display_input)
                for j in self.bible[bible_book][key]:
                    print(f"{j} {self.bible[bible_book][key][j]}\n")
        # Genesis 1
        elif len(parsed) == 2: 
            print(display_input)
            for key in self.bible[bible_book][parsed[1]]:
                print(f"{key} {self.bible[bible_book][parsed[1]][key]}") 

        # Genesis 1:1
        elif len(parsed) == 3:  
            print(display_input)
            print(f"{parsed[2]} {self.bible[bible_book][parsed[1]][parsed[2]]}\n")

        # Gensis 1:1-2
        elif len(parsed) == 4:
            print(display_input)
            for key in self.bible[bible_book][parsed[1]]:
                if int(key) >= int(parsed[2]) and int(key) <= int(parsed[3]):
                    print(f"{key} {self.bible[bible_book][parsed[1]][key]}")

        else:
            print("String not proper citation format")

    # used in search_key to print out the found verses pretty
    def format_verses(self, bib_book, chapter, verse):
        # Formatting 
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


    # Returns verses (and the verses proximate to them) which contain the keyword argument
    def search_key(self, book, keyword):
        bible_book = self.smart_lookup(book)
        count = 0
        if book.upper() == "ALL":
            for b in self.list_books:
                for chapter in self.bible[b]:
                    for verse in self.bible[b][chapter]:
                        if keyword.upper() in self.bible[b][chapter][verse].upper():
                            # Formatting 
                            self.format_verses(b, chapter, verse)
                            count += 1
            print(f"Found {count} instance(s) of '{keyword}'")          

        else:                    
            for chapter in self.bible[bible_book]:  # Loops through each chapter in a bible book 
                for verse in self.bible[bible_book][chapter]: # Loops through each verse in a bible book chapter 
                    if keyword.upper() in self.bible[bible_book][chapter][verse].upper(): 
                        self.format_verses(bible_book, chapter, verse)
                        count += 1
            print(f"Found {count} instance(s) of '{keyword}' in {bible_book}") 
