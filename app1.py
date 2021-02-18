import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def define(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Couldn't find word, did you mean %s instead? (Y)es/(N)o: "
            % get_close_matches(w, data.keys())[0]
        )
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Ok, well, that word doesn't exist...sorry"
        else:
            return "Please enter either Y or N"
    else:
        return "Nice try, this isn't a real word!"


word = input("Enter word: ")

output = define(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
