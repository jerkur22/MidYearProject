import requests
import bs4
import re
item = input()
r = requests.get("https://en.wiktionary.org/wiki/" + item)
data = bs4.BeautifulSoup(r.content, features="html.parser")
data.find_all("div", {"class": "mw-parser-output"})
for item in data.find_all("div", {"class": "mw-parser-output"}):
    item_d = item.descendants
    for d in item_d:
        if d.name == 'ol':
            output = d.text
            break
i = 0
pattern = re.compile("\) (.{1,100}?)\\n")
for item in re.findall(pattern, output):
    i += 1
    if i > 2:
        break
    print(item)