from tkinter import *
 
root = Tk()
 
but = Button(root,
          text="It is a button", # text on the button
          width=30,height=5, # width and height of the button
          bg="white",fg="blue") # background and foreground
 
but.pack()
root.mainloop()
