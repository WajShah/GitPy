from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from  urllib import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

root = Tk()
list_fonts = list( font.families() )
#print(list_fonts)
artransparent = font.Font(root,family='Arabic Transparent', size=24, weight='bold')
arsimplified = font.Font(root,family='Simplified Arabic', size=24, weight='bold')
arsimplifiedfixed = font.Font(root,family='Simplified Arabic Fixed', size=24, weight='bold')
artraditional = font.Font(root,family='Traditional Arabic', size=24, weight='bold')

# topframe = Frame(root)
# topframe.pack()
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
def callback():
    url = v.get()
    print(url)
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

        Label(text=arbwords[-1], relief=RIDGE, bg='yellow', fg='blue', font=artraditional, width=18).grid(row=r, column=0,padx=5,pady=5)

        Label(text=keys, relief=RIDGE, bg='yellow', fg='blue', font="Verdana 18 bold", width=18).grid(row=r, column=1,padx=5, pady=5,sticky=W)


        r += 1
        #  print(keys, values, sep='---->')


v = StringVar()
v.set("Please Enter Aljazeera Learning Url Here")
Entry(bg='green',fg='white' ,textvariable=v,relief=SUNKEN,width=100).grid(row=0,column=0,padx=5, pady=5)
b = Button(root,  text="Get Vocabulary", width=15, command=callback).grid(row=0,column=1,sticky=W,padx=5, pady=5)


root.mainloop()
