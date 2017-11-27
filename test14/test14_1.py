from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label1 = Label(self, text='Hello python!')
        self.label1.pack()

        self.text = Entry(self)
        self.text.pack()

        self.button1 = Button(self, text='quit', command=self.showDialog)
        self.button1.pack()

    def showDialog(self):
        t = self.text.get() or 'no content'
        self.label1
        messagebox.showinfo('Dialog', t)


a = Application()
a.master.title('hello python')
a.mainloop()
