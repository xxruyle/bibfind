import json 
import re 
with open("bib_find/bibles/EntireBible-DR.json", 'r', encoding="UTF-8") as f:
    bible = json.load(f)


#OldTestament = []
#NewTestament = []
#
#matthewindex = mylist.index("Matthew")
#for i, book in enumerate(mylist): 
#    if book == "Matthew" or i >= matthewindex:
#        NewTestament.append(book)
#    else:
#        OldTestament.append(book)

bookdic = {
    'Genesis': ['Gen', 'Ge', 'Gn'], 
    'Exodus': ['Ex', 'Exod', 'Exo'], 
    'Leviticus': ['Lev', 'Le', 'Lv'], 
    'Numbers': ['Num', 'Nu', 'Nm', 'Nb'], 
    'Deuteronomy': ['Deut', 'De', 'Dt'], 
    'Josue': ["Josh", 'Jos', 'Jsh'], 
    'Judges': ['Judg', 'Jdg', 'Jg', 'Jdgs'], 
    'Ruth': ['Rth', 'Ru'], 
    '1 Kings': ['1 Samuel', '1 Sm', '1 Sa', '1 S', 'I Sam'], 
    '2 Kings': ['2 Samuel', '2 Sm', '2 Sa', 'I S', 'II Sam'], 
    '3 Kings': ['III Kings'], 
    '4 Kings': ['IV Kings'], 
    '1 Paralipomenon': ['1 Chronicles', 'I Chronicles'], 
    '2 Paralipomenon': ['2 Chronicles', 'II Chronicles'], 
    '1 Esdras': ['I Ezra', '1 Ezra', '1 Ez', 'I Ez'], 
    '2 Esdras': ['II Ezra', '2 Ezra', '2 Ez', 'II Ez'], 
    'Tobias': ['Tob', 'Tb'], 
    'Judith': ['Jth', 'Jdth', 'Jdt'], 
    'Esther': ['Esth'], 
    'Job': ['Jb'], 
    'Psalms': ['Ps', 'Psalm', 'Pslm', 'Psa', 'Psm', 'Pss'], 
    'Proverbs': ['Prov', 'Pro', 'Prv', 'Pr'], 
    'Ecclesiastes': ['Eccles', 'Eccle', 'Ecc', 'Ec', 'Qoh'], 
    'Canticles': ['Song of Solomon', 'Songs', 'SOS', 'So', 'Canticle of Canticles', 'Cant'], 
    'Wisdom': ['Wisdom of Solomon', 'Wis', 'Ws'], 
    'Ecclesiasticus': ['Sirach', 'Sir'], 
    'Isaias': ['Isa', 'Is'], 
    'Jeremias': ['Jer', 'Je', 'Jr'], 
    'Lamentations': ['Lam', 'La'], 
    'Baruch': ['Bar'], 
    'Ezechiel': ['Ezek', 'Eze', 'Ezk'], 
    'Daniel': ['Dan', 'Da', 'Dn'], 
    'Osee': ['Hosea', 'Hos', 'Ho', 'Os'], 
    'Joel': ['Jl'], 
    'Amos': ['Am'], 
    'Abdias': ['Obadiah', 'Obad', 'Ob', 'Abd', 'Ab'], 
    'Jonas': ['Jonah', 'Jnh', 'Jon'], 
    'Micheas': ['Micah', 'Mic', 'Mc'], 
    'Nahum': ['Nah', 'Na'], 
    'Habacuc': ['Habakkuk', 'Hab', 'Hb'], 
    'Sophonias': ['Zephaniah', 'Zeph', 'Zep', 'Zp', 'Soph'], 
    'Aggeus': ['Haggai', 'Hag', 'Hg', 'Agg'], 
    'Zacharias': ['Zechariah', 'Zech', 'Zec', 'Zc'], 
    'Malachias': ['Malachi', 'Mal', 'Ml'], 
    '1 Machabees': ['1 Maccabees', 'I Maccabees', '1 Mac', 'I Mac'], 
    '2 Machabees': ['2 Maccabees', 'II Maccabees', '2 Mac', 'II Mac'], 
    'Matthew': ['Matt', 'Mt'], 
    'Mark': ['Mrk', 'Mar', 'Mk', 'Mr'], 
    'Luke': ['Luke', 'Luk', 'Lk'], 
    'John': ['Joh', 'Jhn', 'Jn'], 
    'Acts': ['Act', 'Ac'], 
    'Romans': ['Rom', 'Ro', 'Rm'], 
    '1 Corinthians': ['1 Cor', 'I Cor'], 
    '2 Corinthians': ['2 Cor', 'II Cor'], 
    'Galatians': ['Gal', 'Ga'], 
    'Ephesians': ['Eph', 'Ephes'], 
    'Philippians': ['Phil', 'Php', 'Pp'], 
    'Colossians': ['Col', 'Co'], 
    '1 Thessalonians': ['1 Thess', 'I Thess'], 
    '2 Thessalonians': ['2 Thess', 'II Thess'], 
    '1 Timothy': ['1 Tim', 'I Tim'], 
    '2 Timothy': ['2 Tim', 'II Tim'], 
    'Titus': ['Tit', 'Ti'], 
    'Philemon': ['Philem', 'Phm', 'Pm'], 
    'Hebrews': ['Heb'], 
    'James': ['Jas', 'Jm'], 
    '1 Peter': ['1 Pet', '1 Pe', '1 Pt', 'I Peter'], 
    '2 Peter': ['2 Pet', '2 Pe', '2 Pt', 'II Peter'], 
    '1 John': ['1 John', '1 Jhn', '1 Jn', 'I John'], 
    '2 John': ['2 John', '2 Jhn', '2 Jn', 'II John'], 
    '3 John': ['3 John', '3 Jhn', '3 Jn', 'III John'], 
    'Jude': ['Jud', 'Jd'], 
    'Apocalypse': ['Revelation', 'Rev', 'Apoc']
}


def smart_lookup(string):
    bible_books = list(bookdic)
    for book in bible_books: 
        for abbrev in bookdic[book]:
            if string.upper() == abbrev.upper():
                print('First Solution')
                return book 
        if string.upper() in book.upper():
            print('Second Solution')
            return book 
    

