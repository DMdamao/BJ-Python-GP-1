import tkinter
from tkinter import *
import sys

import csvload as cv
import MyMenus as my

popupper = (len(sys.argv) > 1)


def addMoney():
    wina=Tk()
    wina.title("提额")
    wina.geometry("600x300+200+200")
    lable=Label(wina, text="请输入你想提额的额度：", bg="red")
    lable.pack(fill=tkinter.Y, side=tkinter.TOP)
def searchCard():
    pass
def deposit():
    pass
def changeAtmPasswd():
    pass
def withdrawal():
    pass
def changeidcardpasswd():
    pass

#报错信息
def wrong():
    winw = Tk()
    winw.title("警告")
    lable = Label(winw, text="账号或密码错误请重试")
    lable.grid()

# #操作界面
# def opretaview():
#     wino=Tk()
#     wino.title("操作")
#     wino.geometry("600x300")
#     wino.geometry("+200+200")
#     lable=Label(wino, text="欢迎选择以下操作！", bg="blue", font=("宋体", 15), width=40, height=2, wraplength=100)
#     lable.grid(row=0, column=1)
#     lable1 = Label(wino, text="欢迎选择以下操作！", bg="blue", font=("宋体", 15), width=40, height=2, wraplength=100)
#     lable1.grid(row=1, column=1)
#     lable2 = Label(wino, text="欢迎选择以下操作！", bg="blue", font=("宋体", 15), width=40, height=2, wraplength=100)
#     lable2.grid(row=2, column=1)
#     lable3 = Label(wino, text="欢迎选择以下操作！", bg="blue", font=("宋体", 15), width=40, height=2, wraplength=100)
#     lable3.grid(row=3, column=1)
#     button = Button(wino, text="查询", width=10, height=2, bg="yellow", command=searchCard)
#     button.grid(row=0, column=0, sticky=E)
#     button1 = Button(wino, text="存款", width=10, height=2, bg="yellow", command=deposit)
#     button1.grid(row=1, column=0, sticky=E)
#     button2 = Button(wino, text="取款", width=10, height=2, bg="yellow", command=withdrawal)
#     button2.grid(row=2, column=0, sticky=E)
#     button3 = Button(wino, text="改密", width=10, height=2, bg="yellow", command=changeidcardpasswd)
#     button3.grid(row=3, column=0, sticky=E)
#     button4 = Button(wino, text="解锁", width=10, height=2, bg="yellow")
#     button4.grid(row=0, column=2, sticky=W)
#     button5 = Button(wino, text="存款", width=10, height=2, bg="yellow", command=deposit)
#     button5.grid(row=1, column=2, sticky=W)
#     button6 = Button(wino, text="取款", width=10, height=2, bg="yellow", command=withdrawal)
#     button6.grid(row=2, column=2, sticky=W)
#     button7 = Button(wino, text="改密", width=10, height=2, bg="yellow", command=changeidcardpasswd)
#     button7.grid(row=3, column=2, sticky=W)
#     button = Button(wino, text="返回", width=15, height=2, bg="yellow", command=wino.destroy)
#     button.grid(row=4, column=1)
#     if popupper:
#         wino.focus_set()
#         wino.grab_set()
#         wino.wait_window()
#     print("您已进入操作界面")

#登陆界面

def welcomeview():
    def check():
        cards = entry.get()
        pwd = entry1.get()
        me = cv.isPerson(cards, pwd)
        if me:
            print("登陆成功！")
            my.Menus(me)
        else:
            print("卡号或者密码错误！")

    win = Toplevel()
    win.title("登陆")
    win.geometry("600x300")
    win.geometry("+200+200")
    lable = Label(win, text="你好银行：欢迎登陆", bg="blue", font=("宋体", 15), width=20, height=3, wraplength=150)
    lable.grid()
    labe1 = Label(win, text="请输入卡号：", width=10, bg="yellow")
    labe1.grid(row=1, column=1, sticky=E)
    labe2 = Label(win, text="请输入密码：", width=10, bg="yellow")
    labe2.grid(row=2, column=1, sticky=E)
    entry = Entry(win, font=("微软雅黑", 10))
    entry.grid(row=1, column=2)
    entry1 = Entry(win, font=("微软雅黑", 10), show="*")
    entry1.grid(row=2, column=2)
    button1 = Button(win, text="确认登陆", width=10, bg="yellow", command=check)
    button1.grid(row=3, column=2, sticky=E)
    button2 = Button(win, text="开户", width=10, bg="yellow")
    button2.grid(row=4, column=0, sticky=E)
    button3 = Button(win, text="补卡", width=10, bg="yellow")
    button3.grid(row=5, column=0, sticky=E)
    button4 = Button(win, text="返回撤销", width=10, command=win.destroy, bg="yellow")
    button4.grid(row=6, column=0, sticky=E)

    if win:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print("您已进入登陆界面")

#主界面
def main():
    def welcomeView():
        if entry.get() != "1" and entry1.get() != "1":
            wrong()
        else:
            welcomeview()

    root = Tk()#创建窗口
    root.title("你好银行")#窗口名字
    root.geometry("600x300")
    root.geometry("+200+200")
    lable = Label(root, text="你好银行：请先输入管理员账户和密码",  bg="blue", font=("宋体", 15), width=20, height=3, wraplength=150)
    lable.grid()
    lable1 = Label(root, text="请输入管理员账户:", bg="yellow")
    lable1.grid(row=1, column=1)
    lable2 = Label(root, text="请输入管理员密码:", bg="yellow")
    lable2.grid(row=2, column=1)
    ve = StringVar()
    entry = Entry(root, font=("微软雅黑", 10),  textvariable=ve)
    entry.grid(row=1, column=2)
    global res1
    res1 = ve.get()
    vr = StringVar()
    entry1 = Entry(root, font=("微软雅黑", 10), textvariable=vr, show="*")
    entry1.grid(row=2, column=2)
    global res2
    res2 = vr.get()
    button = Button(root, text="确认进入", width=10, command = welcomeView, bg="yellow")
    button.grid(row=3, column=2, sticky=E)
    button1 = Button(root, text="提额", width=10, command=addMoney, bg="yellow")
    button1.grid(row=4, column=0, sticky=E)
    button2 = Button(root, text="改密", width=10, command=changeAtmPasswd, bg="yellow")
    button2.grid(row=5, column=0, sticky=E)
    button3 = Button(root, text="关机", width=10, command=root.destroy, bg="yellow")
    button3.grid(row=6, column=0, sticky=E)
    root.mainloop()#显示窗口


cv.loading()
main()

print("正在保存数据。。")
cv.Writing()
print("程序结束！")