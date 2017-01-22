from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup


# colours = ['red','green','orange','white','yellow','blue']
#
# r = 0
# for c in colours:
#     Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
#     Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
#     Entry(bg='yellow', relief=SUNKEN, width=10).grid(row=r, column=2)
#     Label(text=c,bg='yellow', relief=RIDGE, width=15).grid(row=r, column=2)
#
#
#     r = r + 1
#

root = Tk()

# code goes here

url = "http://learning.aljazeera.net/dailytraining/pages/cb91f69c-25a0-49dd-92c8-58364447171f?Level=1"
content = urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

for ar in soup.find('div', id='arabicwords'):
    arabic = ar.split('$')

for en in soup.find('div', id='englishwords'):
    english = en.split('$')

voc = {}

for i in range(len(english)):
    voc[english[i]] = arabic[i]
r = 1
for keys, values in voc.items():
    arbwords = values.split('+')
    Entry(bg='green', relief=SUNKEN,width=10).grid(row=0,column=1)
    Label(text=arbwords[-2], relief=RIDGE, bg='yellow',fg = 'blue',font = "Verdana 28 bold",width=25).grid(row=r, column=0)
    Label(text=keys, relief=RIDGE, bg = 'yellow',fg = 'blue',font = "Verdana 14 bold", width=25).grid(row=r, column=1)

    r+=1
  #  print(keys, values, sep='---->')


root.mainloop()
