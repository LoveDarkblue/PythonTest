from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # 把自己挂到父容器Frame上
        self.createWidget()

    def createWidget(self):
        self.label1 = Label(self, text='Hello python!')
        self.label1.pack()  # 把自己挂到Application上

        self.text = Entry(self)
        self.text.pack()

        self.button1 = Button(self, text='quit', command=self.showDialog)  # 点击执行showDialog方法
        self.button1.pack()

    def showDialog(self):
        t = self.text.get() or 'no content'  # 获取text控件的值，如果没有，赋值no content
        messagebox.showinfo('Dialog', t)  # 用一个提示Dilog显示出来


a = Application()
a.master.title('hello python')  # 窗体名字
a.mainloop()  # 开启线程
