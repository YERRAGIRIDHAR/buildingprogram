def sentence_maker(phrase):
    x = ("how", "what", "why", "where")
    capitalized =phrase.capitalize() 
    if phrase.startswith(x):
        return "{}?".format(capitalized)
    else:
        return"{}.".format(capitalized)
results = []
while True:
    user_input =input("say something: ")
    if user_input == "end":
        break
    else:
        results.append(sentence_maker(user_input))
print(" ". join(results))



