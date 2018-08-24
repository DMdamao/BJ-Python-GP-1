# -*- coding:utf-8 -*-

import tkinter as tk
import tkinter.messagebox #这个是消息框
from Control.atm import ATM

'''
 转账、改密通用界面
'''
class Input_info(tk.Toplevel):

    def __init__(self, parent,db,card):
        super().__init__()
        self.db = db
        self.card = card
        self.type = self.change_type(parent.type)
        self.title("操作")
        self.parent = parent  # 显式地保留父窗口
        self.entry1 = tk.StringVar() #
        self.entry2 = tk.StringVar()  #

        self.photo = tkinter.PhotoImage(file="Views/Image/2.png")  # 图片路径
        self.photo1 = tk.PhotoImage(file="Views/Image/bg1.png")

        self.text1,self.text2= self.change_type(self.parent.type)
        self.setupUI()  #这一句写在最下面

    def change_type(self,type):
        if type == 3 :
            return "对方账户：" , "金额："
        elif type == 4:
            return "新的密码：" , "确认密码："

    #转账和改密
    def func1(self):
        # 转账
        if self.parent.type == 3:
            res = ATM.Transfer_money(1,self.db,self.card.card_id,
                                     self.entry1.get(),int(self.entry2.get()))
            if res == 1:
                self.parent.message1.set("转账成功")
                money = int(self.parent.money.get()) - int(self.entry2.get())
                self.parent.money.set(money)
            else:
                self.parent.message1.set(res)
            self.destroy()
        # 改密
        elif self.parent.type == 4:
            if self.entry1.get() == self.entry2.get():
                res = ATM.Repasswd(1,self.db,self.card.card_id,self.entry1.get())
                self.parent.message1.set(res)
                self.destroy()
            else:
                self.parent.message1.set("两次密码不相同")

    #程序主页面
    def setupUI(self):
        imgLabel = tkinter.Label(self,
                                 image=self.photo, width=300, height=270, compound=tkinter.CENTER,
                                 )
        imgLabel.place(x=0, y=0)

        text_label = tk.Label(self, text=self.text1,
                              fg="white", font=("宋体", 11),
                              image=self.photo1, width=80, height=25, compound=tkinter.CENTER
                              )
        text_labe2 = tk.Label(self, text=self.text2,
                              fg="white", font=("宋体", 11),
                              image=self.photo1, width=80, height=25, compound=tkinter.CENTER
                              )
        # 金额输入框
        entry1 = tk.Entry(self, textvariable=self.entry1, width=20,bd=5)
        entry2 = tk.Entry(self, textvariable=self.entry2, width=20,bd=5)

        button1 = tk.Button(self, text="确认",command=self.func1,
                            image=self.photo1, width=140, height=30, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white", )  # 自身的颜色

        text_label.place(x=10, y=30)
        text_labe2.place(x=10, y=100)
        entry1.place(x=120, y=30)
        entry2.place(x=120, y=100)
        button1.place(x=120, y=170)