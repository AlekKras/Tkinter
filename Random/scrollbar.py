from tkinter import *
 
root = Tk()
root.title("Scrollbar")
root.minsize(width=300, height=150)
 
fr = Frame(root, width=150, height=100, bg="lightgreen", bd=15)
sc = Scale(fr,orient=HORIZONTAL, length=300,
           from_=0, to=100, tickinterval=10,resolution=5)
fr2 = Frame(root, width=400, height=100, bg="green", bd=25)
ent = Entry(fr2, width=10)
 
fr.pack()
sc.pack()
fr2.pack()
ent.pack()
 
root.mainloop()
