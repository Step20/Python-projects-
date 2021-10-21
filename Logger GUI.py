from tkinter import *

root = Tk()

class logger_mainpg:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.photo =PhotoImage(file="logger_logo.png")
        self.label_logo = Label(self.master, image=self.photo)
        self.label_logo.pack(side=TOP)

        self.topFrame = Frame(self.master)
        self.topFrame.pack(side=TOP)
        self.bottomFrame = Frame(self.master)
        self.bottomFrame.pack(side=BOTTOM)

        self.button_prev = Button(self.bottomFrame, text="Previous Logs")
        self.button_make = Button(self.bottomFrame, text="Make Log")
        self.button_opt = Button(self.bottomFrame, text="Option")
        self.button_ext = Button(self.bottomFrame, text="Exit", command=self.frame.quit)

        self.button_prev.pack(side=LEFT)
        self.button_make.pack(side=LEFT)
        self.button_opt.pack(side=LEFT)
        self.button_ext.pack(side=LEFT)

class logger_prevpg:
    def __int__(self, master, controller):
        self.master = master
        self.topFrame = Frame(self.master)
        self.topFrame.pack(side=TOP)
        self.bottomFrame = Frame(self.master)
        self.bottomFrame.pack(side=BOTTOM)

        self.label = Label(self, text="Previous Logs")
        self.label.pack(self.topFrame)

        self.button_bck = Button(self.bottomFrame, text="Back to Menu", command=self.frame.quit)
        self.button_bck.pack(side=LEFT)

b= logger_mainpg(root)
root.title("Logger")
root.iconbitmap(r'C:\\Users\\A_Rob\\Pictures\\OneDrive\\Documents\\Computer\\Python\\Python\\Logger Files\\logger_icon.ico')
root.mainloop()
