import json
from difflib import get_close_matches
with open(r'C:\Users\#stormy\Music\data.json','r') as ptr:
    Dictionary = json.load(ptr)


def translate(word):
    if word in Dictionary:
        return Dictionary['word']
    elif word.upper() in Dictionary.keys():
        return Dictionary[word.upper]
    elif len(get_close_matches(word,Dictionary.keys())):
        close_input = input("Did you mean %s.\n Enter 'Y' for yes and 'N' for no " % get_close_matches(word,Dictionary.keys())[0])
        if close_input is "Y":
            return Dictionary[get_close_matches(word,Dictionary.keys())[0]]
        elif close_input is "N":
            return "your entry doesn't match. pls double check it"
        else:
            "we didn't understand your entry"

    else:
        return "Enter word doesn't match. pls check it again"

while True:
    word = input('word: ')
    output = translate(word.lower())
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
    command = input("1.Next for proceed further\n2.FINISH for close the program")
    command = command.lower()
    if(command == 'finish'):
        break


