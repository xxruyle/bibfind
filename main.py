import bib_find
import argparse
import os 
from pprint import pprint

# The absolute path which contains the bible translations
dirname = os.path.dirname(__file__)
bibleTranslation = os.path.join(rf"{dirname}\bib_find", "bibles\EntireBible-DR.json")

def main():
    b1 = bib_find.bibfind(bibleTranslation)
    if args.list:
        print(b1.list_books)
    elif args.abbrvs:
        pprint(bib_find.bible_abrvs, sort_dicts=False)
    elif args.translations:
        print(b1.list_translations)
    elif args.chapter:
        b1.list_chapters(args.chapter)
    elif args.search:
        b1.search_key(args.search[0], args.search[1], args.search[2])
    elif args.random:
        b1.random_verse(args.random)
    else:
        find = ' '.join(args.find)
        b1.get_verse(find)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup a bible passage on the command line")
    parser.add_argument("-t", "--translations",  action='store_true', help = "List all the availible translations of the bible")
    parser.add_argument("-a", "--abbrvs",  action='store_true', help = "List all the explicit abbreviations of each bible book as a dictionary")
    parser.add_argument("-l", "--list",  action='store_true', help = "List all the books of the bible")
    parser.add_argument("-c", "--chapter", metavar = "book", type = str, help = "Lists the chapters of a bible book and its first verse")
    parser.add_argument("-s", "--search", nargs = '*', metavar = "<book/all> <keyword> <line_proximity>", type = str, help = "Returns verses (and the verses proximate to them) which contain the keyword argument. EX: -s ALL God 2, -s Matthew Jesus 1")
    parser.add_argument("-f", "--find", nargs = '*', metavar = "verse(s)", type = str, help = "<Book> <Chapter>:<Verse>-<Verse>")
    parser.add_argument("-r", "--random", metavar = "book", type = str, help = "Look up a random passage from the bible. EX: -r ALL, -r OT, -r NT, -r Matthew")
    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main()