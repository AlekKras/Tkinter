from tkinter import *
from random import randrange as rnd

root = Tk()
fr = Frame(root)
root.geometry('800x600')

bt1 = Button(fr,text = 'Hello 1')
bt2 = Button(fr,text = 'Hello 2')

bt1.pack(side='left',padx=2)
bt2.pack(side='left',padx=2)

fr.pack(pady=5, fill = X)

canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)

colors = ['orange','red','blue','yellow','green']
 

def click(event):
    global color
    color = colors[rnd(len(colors))]
 

color = colors[rnd(len(colors))]

def move(event):
    x = event.x
    y = event.y
    canv.create_oval(x-30,y-30,x+30,y+30,fill=color)

canv.bind('<Motion>',move)
canv.bind('<Button>',click)

mainloop()
