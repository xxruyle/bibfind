import json 
import re 


class bibfind():
    def __init__(self):
        with open(r"bib_find\EntireBible-CPDV.json", 'r', encoding="UTF-8") as f:
            self.bible = json.load(f)

        self.list_books = list(self.bible)

    def parse_citation(self, passage):
        init = passage.split(' ', 1)
        parsed = re.split('[:-]+', init[1])
        parsed.insert(0, init[0])
        return parsed 

    def smart_lookup(self, string):
        bible_books = list(self.bible)
        for book in bible_books:
            if string.upper() in book.upper(): 
                return book  

    def get_verse(self, passage):
        parsed = self.parse_citation(passage)
        
        bible_book = self.smart_lookup(parsed[0])
        chapter = f"\n{bible_book}, Chapter {parsed[1]}\n"
        # EX Genesis 
        if len(parsed) == 1:
            for key in self.bible[bible_book]:
                print(chapter)
                for j in self.bible[bible_book][key]:
                    print(f"{j} {self.bible[bible_book][key][j]}\n")
        # Genesis 1
        elif len(parsed) == 2: 
            print(chapter)
            for key in self.bible[bible_book][parsed[1]]:
                print(f"{key} {self.bible[bible_book][parsed[1]][key]}\n") 

        # Genesis 1:1
        elif len(parsed) == 3:  
            print(f"{parsed[2]} {self.bible[bible_book][parsed[1]][parsed[2]]}\n")

        # Gensis 1:1-2
        elif len(parsed) == 4:
            print(chapter)
            for key in self.bible[bible_book][parsed[1]]:
                if int(key) >= int(parsed[2]) and int(key) <= int(parsed[3]):
                    print(f"{key} {self.bible[bible_book][parsed[1]][key]}\n")

        else:
            print("String not proper citation format")