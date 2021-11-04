import os
import json

import requests
from bs4 import BeautifulSoup

def partOne():
  if not os.path.isfile("msu.html"):
    page = requests.get("https://directory.msutexas.edu/users")
    with open("msu.html","w") as f:
      f.write(page.content)
    page = page.content
  else:
    with open("msu.html") as f:
      page = f.read()


  soup = BeautifulSoup(page, "html.parser")

  names = soup.findAll("dd")

  saveList = []

  for name in names:
    printname = name.text.strip()
    if "," in printname:
      last,first = printname.split(",")
      person = {
        'link':name.a['href'],
        'first':first.strip(),
        'last':last.strip()
      }
    else:
      continue
    # print(name.a['href'])
    # print(name.text.strip())
    saveList.append(person)

  with open("people.json","w") as f:
    f.write(json.dumps(saveList,indent=4))


def getPageEmail(link):
  page = requests.get(link)

  soup = BeautifulSoup(page.content, "html.parser")

  email = soup.findAll("dd")

  print(len(email))
  print(email[2].text.strip())


def readPeople():
  with open("people.json") as f:
    people = json.loads(f.read())

  for person in people:
    print(person['link'])
    getPageEmail(person['link'])

#partOne()
readPeople()
