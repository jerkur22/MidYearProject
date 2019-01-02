# Handy-Dict
# Definitions in seconds!
import requests
import bs4
import re
from tkinter import  *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,text =  "Enter word you would like to define").grid(row = 0,column = 0, columnspan = 2, sticky = W)

        self.word = Entry(self)
        self.word.grid(row = 1, column = 1, sticky = W)


        Button(self,text = "Click for story",command = self.give).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self,width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def give(self):
        output = ""
        self.word = str(self.word)
        r = requests.get("https://en.wiktionary.org/wiki/" + self.word)
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

            self.story_txt.insert(0.0, item)

root = Tk()
root.title("Handy-Dict")
app = Application(root)
root.mainloop()
