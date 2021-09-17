import requests
from bs4 import BeautifulSoup

'''Sample coding Practise for web scraping'''

v = requests.get("http://pythonhow.com/example.html")
k = v.content

#print(k)

soup = BeautifulSoup(k,"html.parser")

print(soup.prettify())
print(".................")

all=soup.find_all("div",{"class":"cities"})
print(all)

all[0].find_all("h2")[0].text
for item in all:
    print(item.find_all("h2")[0].text)
    print(item.find_all("p")[0].text)