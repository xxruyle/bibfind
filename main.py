import bib_find
import argparse

def main():
    b1 = bib_find.bibfind()
    if args.list:
        print(b1.list_books)
    else:
        read = ' '.join(args.read)
        b1.get_verse(read)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lookup a bible passage on the command line")
    parser.add_argument("-l", "--list",  action='store_true', help = "List all the books of the bible")
    parser.add_argument("-r", "--read", nargs = '*', metavar = "read", type = str, help = "Read a passage")
    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main()