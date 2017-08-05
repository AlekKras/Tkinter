from tkinter import *
 
class Form:
    def __init__(self):
        self.root = Tk()
        self.root.title('Response form')
        self.root.geometry('500x400+300+200')
        self.width = 50
 
class Question:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.ent = Entry(form.root, width=form.width+16)
        self.lab.pack()
        self.ent.pack()
 
class BigQuestion:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.txt = Text(form.root, width=form.width, height=4)
        self.lab.pack()
        self.txt.pack()
 
class RadioBut:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.lab.pack()
        self.var = IntVar()
        self.var.set(1)
        self.rad0 = Radiobutton(form.root, text="$", variable=self.var,value=1)
        self.rad1 = Radiobutton(form.root, text='$$', variable=self.var, value=2)
        self.rad2 = Radiobutton(form.root, text='$$$', variable=self.var, value=3)
        self.rad3 = Radiobutton(form.root, text='$ $ $ $', variable=self.var, value=4)
        self.rad0.pack()
        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()
 
class Flags:
    def __init__(self, form, question):
        self.lab = Label(form.root, text=question)
        self.lab.pack()
        self.c0 = IntVar()
        self.c1 = IntVar()
        self.c2 = IntVar()
        self.c3 = IntVar()
        self.che0 = Checkbutton(form.root, text="Red",bg='red',
                                variable=self.c0, onvalue=1, offvalue=0)
        self.che1 = Checkbutton(form.root, text="Blue", bg='blue',
                                variable=self.c1, onvalue=1, offvalue=0)
        self.che2 = Checkbutton(form.root, text="Green", bg='green',
                                variable=self.c2, onvalue=1, offvalue=0)
        self.che3 = Checkbutton(form.root, text="Yellow",bg='yellow',
                                variable=self.c3, onvalue=1, offvalue=0)
        self.che0.pack()
        self.che1.pack()
        self.che2.pack()
        self.che3.pack()
 
class Scene:
    def __init__(self):
        self.form = Form()
        self.qstn = Question(self.form, 'Your address:')
        self.comm = BigQuestion(self.form, 'Comments:')
        self.radi = RadioBut(self.form, 'How much?')
        self.flag = Flags(self.form, 'What color?')
        self.butt = Button(self.form.root, text='Send')
        self.butt.pack()
        self.butt.bind('<Button-1>', self.go)
        self.form.root.mainloop()
 
    def go(self, event):
        print('Send:\n',
              'Colors:', self.flag.c0.get(), self.flag.c1.get(),
              self.flag.c2.get(), self.flag.c3.get(),
              'Count:', self.radi.var.get())
 
scene = Scene()
