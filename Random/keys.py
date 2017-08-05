import tkinter as tk
 
class myapp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event handling")
        self.root.bind("q",self.exitself)
        self.text = tk.Label(self.root,text='Press "q" to exit"')
        self.flagsDic = {
        'First':1,
        'Second':2,
        'Third':3,
        'Fourth':4
        }
        for key in self.flagsDic:
            self.flagsDic[key] = tk.IntVar()
            Flag = tk.Checkbutton(self.root,text=key,variable=self.flagsDic[key])
            Flag.grid(sticky='w')
        self.ent = tk.Entry(self.root,width=20)
        self.fstatus = tk.Text(self.root)
        self.text.grid(row=4,column=0,columnspan=2)
        self.fstatus.grid(row=0,column=1,rowspan=len(self.flagsDic))
        self.fstatus.bind("<Button-1>",self.display)
    def display(self,event):
        checked = []
        unchecked = []
        for key, value in self.flagsDic.items():
            if value.get():
                checked.append(key)
            else:
                unchecked.append(key)
        if len(checked) == 0:
            message = "Unchecked:"
            for s in unchecked:
                message = message + " " + s
            print(message)
        if len(unchecked) == 0:
            message = "Checked:"
            for s in checked:
                message = message + " " + s
        if len(checked) != 0 and len(unchecked) != 0:
            message = "Unchecked:"
            for s in unchecked:
                message = message + " " + s
            message = message + "\nChecked:"
            for s in checked:
                message = message + " " + s
        self.fstatus.delete(0.0,tk.END)
        self.fstatus.insert(0.0,message)
    def exitself(self,event):
        self.root.destroy()
 
def main():
    app = myapp()
    app.root.mainloop()
 
if __name__ == "__main__":
    main()
