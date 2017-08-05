from tkinter import *
 
def printer(event):
     print ("Hi there, this button works!'")
 
root = Tk()

but = Button(root)
but["text"] = "Hi there"
but.bind("<Button-1>",printer)
 
but.pack()
root.mainloop() 
