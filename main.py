import bib_find
import argparse

def main():
    b1 = bib_find.bibfind()
    if args.list:
        print(b1.list_books)
    elif args.search:
        b1.search_key(args.search[0], args.search[1])
    else:
        read = ' '.join(args.read)
        b1.get_verse(read)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup a bible passage on the command line")
    parser.add_argument("-l", "--list",  action='store_true', help = "List all the books of the bible")
    parser.add_argument("-s", "--search", nargs = '*', metavar = "book/all, keyword", type = str, help = "Returns verses (and the verses proximate to them) which contain the keyword argument")
    parser.add_argument("-r", "--read", nargs = '*', metavar = "read", type = str, help = "<Book> <Chapter>:<Verse>-<Verse>")

    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main()