import re 

def parse_citation(passage):
    if passage[0].isdigit():
        init = passage.split(' ', 2)
        parsed = re.split('[:-]+', init[2])
        book = passage[0] + ' '+ init[1]
        parsed.insert(0, book)
    else:
        init = passage.split(' ', 1)
        parsed = re.split('[:-]+', init[1])
        print(init)
        parsed.insert(0, init[0])
        
    return parsed 

print(parse_citation("1 John 1"))