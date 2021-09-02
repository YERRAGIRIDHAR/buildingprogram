import mysql.connector
from difflib import get_close_matches 

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

# def result(w):
#     word = w.lower()
#     if word in con:
#          return con[word]

#     elif len(get_close_matches(word, con.expression())) > 0:
#         # "The {} may be {}:".format(word,get_close_matches(word, data.keys())[0])
#         return con[get_close_matches(word, con.expression())[0]]

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(results[0])
else:
    print("No word found")