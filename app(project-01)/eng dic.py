import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    word = w.lower()
    if word in data:
         return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        # "The {} may be {}:".format(word,get_close_matches(word, data.keys())[0])
        return data[get_close_matches(word, data.keys())[0]]
    else:
        print("This word is not in data.")

word = input("Enter word: ")
      
output = meaning(word)
if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)