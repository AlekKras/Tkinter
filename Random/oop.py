from tkinter import *
 
class But_print:
     def __init__(self):
          self.but = Button(root)
          self.but["text"] = "Hi there"
          self.but.bind("<Button-1>",self.printer)
          self.but.pack()
     def printer(self,event):
          print ("Hi there, this button works!'")
 
root = Tk()
obj = But_print()
root.mainloop()
