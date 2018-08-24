# -*- coding:utf-8 -*-

import tkinter as tk
import tkinter.messagebox  # 这个是消息框
from Control.atm import ATM

'''
开户、解锁通用页面
'''


class Register(tk.Toplevel):

    def __init__(self, parent, db):
        super().__init__()
        self.db = db
        self.title("操作")
        self.parent = parent  # 显式地保留父窗口

        self.name = tk.Variable()  # 用户姓名
        self.Idcard = tk.Variable()  # 身份证号
        self.tel = tk.Variable()  # 身份证号
        self.passwd = tk.Variable()  # 密码/验证码

        self.photo = tkinter.PhotoImage(file="Views/Image/2.png")  # 图片路径
        self.photo1 = tk.PhotoImage(file="Views/Image/bg1.png")

        self.setupUI()  # 这一句写在最下面

    # 开户/解锁
    def func1(self):
        # 开户
        if self.parent.type == "密码：":
            res = ATM.add_user(1, self.db, self.name.get(), self.Idcard.get(), self.tel.get(), self.passwd.get())
            if str(res).isdigit():
                tkinter.messagebox.showinfo(title='提示', message="开户成功，卡号为：%s" % str(res))
                self.destroy()
            else:
                tkinter.messagebox.showinfo(title='错误信息', message=res)
        # 解锁
        elif self.parent.type == "卡号：":
            res = ATM.re_clock(1, self.db, self.name.get(), self.Idcard.get(), self.tel.get(), self.passwd.get())
            tkinter.messagebox.showinfo(title='提示', message=res)
            self.destroy()

    # 程序主界面
    def setupUI(self):
        imgLabel = tkinter.Label(self,
                                 image=self.photo, width=300, height=370, compound=tkinter.CENTER,
                                 )
        imgLabel.place(x=0, y=0)

        name_label = tk.Label(self, text="姓名:", fg="white",
                              image=self.photo1, width=60, height=20, compound=tkinter.CENTER
                              )
        Idcard_label = tk.Label(self, text="身份证号：", fg="white",
                                image=self.photo1, width=60, height=20, compound=tkinter.CENTER
                                )
        tel_label = tk.Label(self, text="电话号码:", fg="white",
                             image=self.photo1, width=60, height=20, compound=tkinter.CENTER
                             )
        passwd_label = tk.Label(self, text=self.parent.type, fg="white",
                                image=self.photo1, width=60, height=20, compound=tkinter.CENTER
                                )
        name_entry = tk.Entry(self, textvariable=self.name, width=20, bd=5)
        Idcard_entry = tk.Entry(self, textvariable=self.Idcard, width=20, bd=5)
        tel_entry = tk.Entry(self, textvariable=self.tel, width=20, bd=5)
        passwd_entry = tk.Entry(self, textvariable=self.passwd, width=20, show="*", bd=5)

        button1 = tk.Button(self, text="确认提交", command=self.func1,
                            image=self.photo1, width=140, height=27, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white", )  # 自身的颜色
        name_label.place(x=15, y=30)
        Idcard_label.place(x=15, y=90)
        tel_label.place(x=15, y=150)
        passwd_label.place(x=15, y=210)

        name_entry.place(x=100, y=30)
        Idcard_entry.place(x=100, y=90)
        tel_entry.place(x=100, y=150)
        passwd_entry.place(x=100, y=210)

        button1.place(x=100, y=280)
