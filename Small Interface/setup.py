from tkinter import *
import os
from tkinter import messagebox
from PIL import Image, ImageTk
#creating window
class Window(Frame):

    def __init__(self, master = None):

        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")

        self.pack(fill= BOTH, expand = 1)
        quitButton = Button(self,
                            text="Intro",
                            command=self.user_intro).place(x = 125,
                                                          y = 50,
                                                          width = 150,
                                                          height = 50)
        quitButton = Button(self,
                            text="Fun",
                            command=self.user_fun).place(x = 125,
                                                          y = 110,
                                                          width = 150,
                                                          height = 50)

        quitButton = Button(self,
                            text="Quit",
                            command=self.user_exit).place( x = 125,
                                                           y = 170,
                                                           width = 150,
                                                           height = 50)


        intro = Menu(self.master)
        self.master.config(menu=intro)

        file = Menu(intro)
        file.add_command(label="New", command=self.newProgram)
        file.add_command(label="ABORT!!!", command=self.restart)
        file.add_command(label="Exit", command=self.user_exit)
        intro.add_cascade(label="File", menu=file)

        random = Menu(intro)
        random.add_command(label="Cure OS", command=self.shutdown)
        intro.add_cascade(label="Random", menu=random)

        help = Menu(intro)
        help.add_command(label="Credits", command=self.credit)
        help.add_command(label="Show Image", command=self.showImg)
        help.add_command(label="Show text", command=self.showTxt)
        intro.add_cascade(label="More Info", menu=help)

        CLICK = Menu(intro)
        CLICK.add_command(label="Click it", command=self.deletePython)
        intro.add_cascade(label="Totally safe to click", menu=CLICK)
    #button commands
    def user_exit(self):
        exit()
    def user_intro(self):
        messagebox.showinfo("Intro", "This is my first attempt trying to make GUI app with Python. It was pretty fun and not quite challenging as documentation is pretty clear. Also, Google helps a lot while coding :)")
    def user_fun(self):
        messagebox.showwarning("What the heck?", "<<< This is the warning thing. Be careful, bro")
        messagebox.showinfo("GUI Python", "Hello," + os.getlogin())
    #cascade commands
    def newProgram(self):
        os.system('python module.py')
    def restart(self):
        os.system('shutdown -r -t 60 ')
    def shutdown(self):
        os.system("shutdown -s -t 1")
    def credit(self):
        messagebox.showinfo("Some info about me", "This is just a draft")
    def deletePython(self):
        path = sys.executable
        os.remove(path)
        os.removedirs(path)
    def showImg(self):
        load = Image.open("log.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)
    def showTxt(self):
        text = Label(self, text='''totally safe to click''')
        text.pack()

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()