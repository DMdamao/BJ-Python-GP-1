# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox  # 这个是消息框
from Control.atm import ATM
from Control.person import Person
from Control.card import Card
from Views.view_win2 import Operation
from Views.view_win5 import Register

'''
程序主界面
'''

class MyApp(tk.Tk):
    #初始化
    def __init__(self, db):
        super().__init__()
        self.title('欢迎进入银行系统')
        self.geometry("800x600+350+100")

        # 页面参数
        self.db = db
        self.passwd_time = 0          # 输入密码的次数
        self.card_id = tk.Variable()  # 输入的卡号
        self.passwd = tk.Variable()   # 输入的密码
        self.temp_id = ""             # 暂时存储卡号
        self.input_time = 3           # 密码输入次数
        self.type = "密码"
        per1 = None                   # 实例一个用户
        card1 = None                  # 实例一张卡

        self.photo = tkinter.PhotoImage(file="Views/Image/111.png")  # 背景路径
        self.photo1 = tk.PhotoImage(file="Views/Image/bg1.png")

        # 程序界面
        self.setupUI()

    #点击登录按钮
    def func1(self):
        card_id = self.card_id.get()
        passwd = self.passwd.get()
        res = ATM.check_login(1, self.db, card_id, passwd)
        info = res.split(":")
        # print(info)
        if info[0] == "1":
            card1 = Card(info[1], info[2], info[3], info[4])
            operation = Operation(self, self.db, card1)
            operation.geometry("800x600+350+100")
            self.wait_window(operation)  # 等待子窗口执行
        else:
            tkinter.messagebox.showinfo(title='错误信息', message=res)

    #点击开户按钮
    def func2(self):
        self.type = "密码："
        register = Register(self, self.db)
        register.geometry("300x370+770+150")
        self.wait_window(register)  # 等待子窗口执行

    #点击解锁按钮
    def func3(self):
        self.type = "卡号："
        register = Register(self, self.db)
        register.geometry("300x370+770+150")
        self.wait_window(register)  # 等待子窗口执行

    #点击退出按钮
    def func4(self):
        self.destroy()

    #窗口主界面
    def setupUI(self):

        imgLabel = tkinter.Label(self,image=self.photo, width=800, height=600, compound=tkinter.CENTER,)
        imgLabel.place(x=0, y=0)

        card_text = tk.Label(self, text="卡号:", fg="white", font=("宋体", 14),
                            image=self.photo1, width=50, height=20, compound=tkinter.CENTER,)
        #卡号输入框
        card_id = tk.Entry(self, textvariable=self.card_id, fg="orange", width=30, highlightcolor="red", bd=5,)

        passwd_text = tk.Label(self, text="密码:", fg="white", font=("宋体", 14),
                               image=self.photo1, width=50, height=20, compound=tkinter.CENTER,)
        # 密码输入框
        passwd = tk.Entry(self, textvariable=self.passwd, fg="orange", show="*", width=30, bd=5)

        # 登录按钮
        button1 = tk.Button(self, text="登录系统",
                            command=self.func1,  # 点击时执行的函数
                            font=("宋体", 14),
                            image=self.photo1,
                            width=205,
                            height=40,
                            compound=tkinter.CENTER,

                            fg="white",  # 自身的颜色
                            )
        # 注册按钮
        button2 = tk.Button(self, text="开户",
                            command=self.func2,  # 点击时执行的函数
                            font=("宋体", 12),
                            image=self.photo1,
                            width=90,
                            height=30,
                            compound=tkinter.CENTER,

                            fg="white",  # 自身的颜色
                            )

        button3 = tk.Button(self, text="解锁",
                            command=self.func3,  # 点击时执行的函数
                            font=("宋体", 12),
                            image=self.photo1,
                            width=90,
                            height=30,
                            compound=tkinter.CENTER,

                            fg="white",  # 自身的颜色
                            )
        button4 = tk.Button(self, text="退出",
                            command=self.func4,  # 点击时执行的函数
                            font=("宋体", 12),
                            image=self.photo1,
                            width=90,
                            height=30,
                            compound=tkinter.CENTER,

                            fg="white",  # 自身的颜色
                            )

        card_text.place(x=420, y=170)
        passwd_text.place(x=420, y=240)
        card_id.place(x=490, y=170)
        passwd.place(x=490, y=240)
        button1.place(x=490, y=330)
        button3.place(x=530, y=490)
        button4.place(x=640, y=490)
        button2.place(x=420, y=490)
