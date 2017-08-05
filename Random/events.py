from tkinter import *

def b1(event):
     root.title("Left mouse click")
     
def b2(event):
     root.title("Middle mouse click")
     
def b3(event):
     root.title("Right mouse click")
     
def db1(event):
    root.title("Double left mouse click")
    
def move(event):
     root.title("Mouse movement")

root = Tk()
root.minsize(width = 500, height=400)
 
root.bind('<Button-1>',b1)
root.bind('<Button-2>', b2)
root.bind('<Button-3>',b3)
root.bind('<Double-Button-1>',db1)
root.bind('<Motion>',move)

root.mainloop() 
