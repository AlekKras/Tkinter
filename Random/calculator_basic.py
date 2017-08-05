from tkinter import *
win = Tk()
win.title("Calculator")
 
def test(e):
    try:
        lab2["text"] = eval(ent.get())
    except:
        lab2["text"] = "Incorrect input, try again"
 
 
lab = Label(text="Put raw data using +, -, *, /, //, %, **")
lab.pack()
ent = Entry(width=50,bg="white",justify=CENTER)
ent.focus()
ent.pack()
ent.bind('<Return>', test)
lab2 = Label()
lab2.pack()
 
win.mainloop()
