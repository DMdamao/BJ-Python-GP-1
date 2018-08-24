from tkinter import *
from PIL import Image ,ImageTk

class View(object):
    # 欢迎界面
    def welcome(self):
        root = Tk()
        root.title("银行系统")
        root.geometry("1000x600+150+70")
        def a():
            root.destroy()
        bt1 = Button(root, text='欢迎使用银行自助服务系统', bg="gainsboro", fg="red", font=("Arial", 25), width=80, height=20, command=a)
        bt1.pack()
        root.mainloop()
    # 管理员界面
    def adminview(self):
        win = Tk()
        win.title("管理员界面")
        win.geometry("1000x600+150+70")
        def func():
            win.destroy()
            global ve
            ve = "11"
        def func1():
            win.destroy()
            global ve
            ve = "22"
        def func3():
            win.destroy()
            global ve
            ve = "33"
        def func4():
            win.destroy()
            global ve
            ve = "44"
        text1 = Label(win, text="管理员界面", fg="black", font=("粗体",30), anchor=S, width=12, height=1, wraplength = 200, justify="left")
        text1.place(x= 350 , y = 100)
        button1 = Button(win, text="登陆", bg='#657485', fg="red", font=("Arial", 20), width=20, height=3, command=func)
        button1.place(x=0,y=180)
        button2 = Button(win, text="退出", bg='#584756', fg="red", font=("Arial", 20), width=20, height=3, command=func1)
        button2.place(x=0,y=300)
        button3 = Button(win, text="提额", bg='#475586', fg="red", font=("Arial", 20), width=20, height=3, command=func3)
        button3.place(x=700,y=180)
        button4 = Button(win, text="改密", bg='#685574', fg="red", font=("Arial", 20), width=20, height=3, command=func4)
        button4.place(x=700,y=300)


        bm = PhotoImage(file= 'bg.png')
        label2 = Label(image=bm)
        label2.place(x =343,y=170)

        win.mainloop()
        return ve
    # 用户界面
    def userview(self):
        win = Tk()
        win.title("管理员界面")
        win.geometry("1000x600+150+70")
        def func():
            win.destroy()
            global ve
            ve = "111"
        def func1():
            win.destroy()
            global ve
            ve = "222"
        def func3():
            win.destroy()
            global ve
            ve = "333"
        def func4():
            win.destroy()
            global ve
            ve = "444"
        text1 = Label(win, text="用户界面", fg="black", font=("粗体", 30), anchor=S, width=12, height=1, wraplength=200,
                      justify="left")
        text1.place(x=350, y=100)
        button1 = Button(win, text="插卡", bg='#657485', fg="red", font=("Arial", 20), width=20, height=2, command=func)
        button1.place(x=0,y=180)
        button2 = Button(win, text="注册", bg='#584756', fg="red", font=("Arial", 20), width=20, height=2, command=func1)
        button2.place(x=0,y=300)
        button3 = Button(win, text="补卡", bg='#475586', fg="red", font=("Arial", 20), width=20, height=2, command=func3)
        button3.place(x=700,y=180)
        button4 = Button(win, text="返回", bg='#685574', fg="red", font=("Arial", 20), width=20, height=2, command=func4)
        button4.place(x=700,y=300)
        bm = PhotoImage(file= 'bg.png')
        label2 = Label(image=bm)
        label2.place(x =343,y=170)
        win.mainloop()
        return ve
    #操作界面
    def optionsView(self):
        win = Tk()
        win.title("管理员界面")
        win.geometry("1000x600+150+70")
        def func():
            win.destroy()
            global ve
            ve = "1"
        def func1():
            win.destroy()
            global ve
            ve = "2"
        def func3():
            win.destroy()
            global ve
            ve = "3"
        def func4():
            win.destroy()
            global ve
            ve = "4"
        def func5():
            win.destroy()
            global ve
            ve = "5"
        def func6():
            win.destroy()
            global ve
            ve = "6"
        def func7():
            win.destroy()
            global ve
            ve = "7"
        def func8():
            win.destroy()
            global ve
            ve = "8"
        def func9():
            win.destroy()
            global ve
            ve = "9"
        text1 = Label(win, text="欢迎使用", fg="black", font=("粗体", 30), anchor=S, width=12, height=1, wraplength=200,
                      justify="left")
        text1.place(x=350, y=100)
        button1 = Button(win, text="查余额", bg='#657485', fg="#000", font=("Arial", 15), width=20, height=2, command=func)
        button1.pack(anchor=NE)
        button2 = Button(win, text="转账", bg='#985541', fg="#000", font=("Arial", 15), width=20, height=2, command=func1)
        button2.pack(anchor=SW)
        button3 = Button(win, text="存款", bg='#145589', fg="#000", font=("Arial", 15), width=20, height=2, command=func3)
        button3.pack(anchor=E)
        button4 = Button(win, text="取款", bg='#684513', fg="#000", font=("Arial", 15), width=20, height=2, command=func4)
        button4.pack(anchor=W)
        button5 = Button(win, text="改密", bg='#315486', fg="#000", font=("Arial", 15), width=20, height=2, command=func5)
        button5.pack(anchor=NE)
        button6 = Button(win, text="注销", bg='#31548a', fg="#000", font=("Arial", 15), width=20, height=2, command=func6)
        button6.pack(anchor=NW)
        button7 = Button(win, text="锁定", bg='#a84513', fg="#000", font=("Arial", 15), width=20, height=2, command=func7)
        button7.pack(anchor=SE)
        button8 = Button(win, text="解锁", bg='#35a512', fg="#000", font=("Arial", 15), width=20, height=2, command=func8)
        button8.pack(anchor=SW)
        button9 = Button(win, text="退卡", bg='#521521', fg="#000", font=("Arial", 15), width=30, height=2, command=func9)
        button9.pack(side=BOTTOM)
        bm = PhotoImage(file= 'bg.png')
        label2 = Label(image=bm)
        label2.place(x =343,y=170)
        win.mainloop()
        return ve
    # 输出
    def error(self, ename):
        root = Tk()
        root.title("提示")
        root.geometry("1000x600+150+70")
        a = Label(root, text="%s" % ename, bg="skyBlue", font=("Arial", 20), fg="black", width=80, height=16)
        a.pack()
        def func():
            root.destroy()
        bt1 = Button(root, text="确定", bg="#657258", width=20, height=3, command=func)
        bt1.pack(anchor=SE)
        root.mainloop()
    # 输入
    def cardid(self, title):
        win = Tk()
        win.title(title)
        win.geometry("1000x600+150+70")
        def func():
            win.destroy()
        ve = Variable()
        e = Entry(win, textvariable=ve)
        button = Button(win, text="确定", command=func)
        button.pack(side=BOTTOM)
        e.pack(side=BOTTOM)
        a = Label(win, text=title, bg='skyBlue',  font=("Arial", 20), fg="black", width=70, height=16, wraplength=800, justify='left')
        a.pack()
        win.mainloop()
        return ve.get()