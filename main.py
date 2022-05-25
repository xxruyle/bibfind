import bib_find
import argparse

def main():
    b1 = bib_find.bibfind("bibles/EntireBible-DR.json")
    if args.list:
        print(b1.list_books)
    elif args.translations:
        print(b1.list_translations)
    elif args.search:
        b1.search_key(args.search[0], args.search[1])
    elif args.random:
        b1.random_verse(args.random)
    else:
        read = ' '.join(args.read)
        b1.get_verse(read)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup a bible passage on the command line")
    parser.add_argument("-t", "--translations",  action='store_true', help = "List all the availible translations of the bible")
    parser.add_argument("-l", "--list",  action='store_true', help = "List all the books of the bible")
    parser.add_argument("-s", "--search", nargs = '*', metavar = "book/all, keyword", type = str, help = "Returns verses (and the verses proximate to them) which contain the keyword argument")
    parser.add_argument("-f", "--find", nargs = '*', metavar = "find", type = str, help = "<Book> <Chapter>:<Verse>-<Verse>")
    parser.add_argument("-r", "--random", metavar = "random", type = str, help = "Look up a random passage from the bible. EX: -r ALL, -r Matthew")

    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main()