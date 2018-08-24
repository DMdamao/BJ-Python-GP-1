# -*- coding:utf-8 -*-

import tkinter as tk
from   tkinter import ttk
import tkinter.messagebox  # 这个是消息框，对话框的关键
from Views.view_win3 import Input_money
from Views.view_win4 import Input_info
from Control.atm import ATM

'''
业务办理选择页面

'''

# 操作窗口

class Operation(tk.Toplevel):
    #初始化*******************************************************
    def __init__(self, parent, db, card):
        super().__init__()
        self.db = db
        self.card = card
        self.title('欢迎光临')
        self.parent = parent  # 显式地保留父窗口
        self.type = 0  # 让子窗口判断操作类型
        self.message1 = tk.Variable()  # 操作成功或失败提示
        self.money = tk.Variable()  # 余额
        self.money.set(self.card.money)
        self.message1.set("欢迎使用ATM自动取款机")

        self.photo = tkinter.PhotoImage(file="Views/Image/bg.png")  # 图片路径
        self.photo1 = tk.PhotoImage(file="Views/Image/bg1.png")

        # 程序界面
        self.setupUI()


    # 点击取款按钮*************************************************
    def func1(self):
        self.message1.set("请操作")
        self.type = 1
        input_money = Input_money(self, self.db, self.card)
        input_money.geometry("300x200+620+330")
        self.wait_window(input_money)  # 等待子窗口执行
        return


    # 点击存款按钮*************************************************
    def func2(self):
        self.message1.set("请输入")
        self.type = 2
        input_info = Input_money(self, self.db, self.card)
        input_info.geometry("300x200+620+330")
        self.wait_window(input_info)  # 等待子窗口执行
        return


    # 点击转账按钮*************************************************
    def func3(self):
        self.message1.set("请输入")
        self.type = 3
        input_info = Input_info(self, self.db, self.card)
        input_info.geometry("300x270+620+330")
        self.wait_window(input_info)  # 等待子窗口执行
        return


    # 点击修改密码按钮**********************************************
    def func4(self):
        self.message1.set("请输入")
        self.type = 4
        input_info = Input_info(self, self.db, self.card)
        input_info.geometry("300x270+620+330")
        self.wait_window(input_info)  # 等待子窗口执行
        return


    # 锁卡、挂失***************************************************
    def func5(self):
        res = ATM.Lock_card(1, self.db, self.card.card_id)
        tkinter.messagebox.showinfo(title='提示', message=res)
        self.destroy()


    # 销户********************************************************
    def func6(self):
        res = ATM.delete_card(1, self.db, self.card.card_id)
        tkinter.messagebox.showinfo(title='提示', message=res)
        self.destroy()


    # 退出系统*****************************************************
    def func7(self):
        self.parent.destroy()
        # self.destroy()


    # 写账单日志时把操作状态码具体化***********************************
    def log_info(self, db, cardid, label):
        c = db.cursor()
        res = c.execute(
            "select insert_time,type,money from loginfo where cardId = %s ORDER BY id DESC" % cardid)
        loginfo = res.fetchall()
        for i in range(len(loginfo)):
            aa = ""
            if loginfo[i][1] == 1:
                aa = "取款"
            elif loginfo[i][1] == 2:
                aa = "存款"
            else:
                aa = "转账"
            label.insert("", 0, text=loginfo[i][0], values=(aa, loginfo[i][2]))


    # 程序主页面****************************************************
    def setupUI(self):
        imgLabel = tkinter.Label(self,
                                 image=self.photo, width=800, height=600, compound=tkinter.CENTER,
                                 )
        imgLabel.place(x=0, y=40)

        title_label = tk.Label(self, text="欢迎使用ATM自动取款机",
                               textvariable=self.message1,
                               fg="white",  # 自身的颜色
                               font=("宋体", 20),
                               image=self.photo, width=800, height=60, compound=tkinter.CENTER,
                               anchor="center",  # 位置n北，e东，s南，w西，c中间，nese
                               )
        button1 = tk.Button(self, text="取款",
                            command=self.func1,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button2 = tk.Button(self, text="存款",
                            command=self.func2,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button3 = tk.Button(self, text="锁卡",
                            command=self.func5,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button4 = tk.Button(self, text="销户",
                            command=self.func6,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button5 = tk.Button(self, text="转账",
                            command=self.func3,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button6 = tk.Button(self, text="改密",
                            command=self.func4,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button7 = tk.Button(self, text="挂失",
                            command=self.func5,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )
        button8 = tk.Button(self, text="补卡",
                            command=self.func7,  # 点击时执行的函数
                            image=self.photo1, width=110, height=40, compound=tkinter.CENTER,
                            font=("宋体", 14),
                            fg="white",  # 自身的颜色
                            )

        button11 = tk.Button(self, text="退出系统",
                             command=self.func7,
                             image=self.photo1, width=300, height=40, compound=tkinter.CENTER,
                             font=("宋体", 14),
                             fg="white",  # 自身的颜色
                             )
        Label_text1 = tk.Label(self, text="账单日志",
                               font=("宋体", 16),
                               image=self.photo1, width=300, height=40, compound=tkinter.CENTER,
                               fg="pink",  # 自身的颜色
                               anchor="center",
                               )

        frame1 = tk.Frame(self, bg="white", width=420, height=100)

        frame1_text2_title = tk.Label(frame1, text="余额：¥",
                                      font=("宋体", 14),
                                      bg="white",
                                      fg="red",
                                      anchor="center", )
        frame1_text2 = tk.Label(frame1, text="0",
                                textvariable=self.money,
                                font=("宋体", 16),
                                bg="white",
                                fg="red",
                                anchor="center", )
        frame1_text1 = tk.Label(frame1, text="卡号: %s" % self.card.card_id,
                                font=("宋体", 14),
                                bg="white",
                                fg="orange",
                                anchor="center", )

        tree = ttk.Treeview(self)
        tree["columns"] = ("操作", "金额")
        # 设置列，现在还不显示
        tree.column("操作", width=100)
        tree.column("金额", width=100)

        # 设置表头
        tree.heading("操作", text="操作")
        tree.heading("金额", text="金额")

        # 添加数据
        self.log_info(self.db, self.card.card_id, tree)

        # tree.insert("", 0, text="2018.10.10", values=("取款", "200"))


        # 滚动条
        s = tk.Scrollbar(self)
        s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        s.config(command=tree.yview)
        tree.config(yscrollcommand=s.set)

        frame1.place(x=200, y=100)
        frame1_text1.place(x=20, y=15)
        frame1_text2.place(x=90, y=58)
        frame1_text2_title.place(x=20, y=60)

        Label_text1.place(x=250, y=240)
        # Label_text2.place(x=350, y=60)
        tree.place(x=200, y=300)

        title_label.place(x=0, y=0)
        button1.place(x=40, y=100)
        button2.place(x=40, y=220)
        button3.place(x=40, y=340)
        button4.place(x=40, y=460)
        button5.place(x=650, y=100)
        button6.place(x=650, y=220)
        button7.place(x=650, y=340)
        button8.place(x=650, y=460)

        button11.place(x=250, y=550)
