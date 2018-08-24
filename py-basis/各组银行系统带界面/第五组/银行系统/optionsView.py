#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : optionsView.py
# @Author: Janus
# @Date  : 2018/8/15
# @Desc  :
import tkinter
from tkinter import *
from atm import ATM

from welcome import Welcome
import time

from tkinter import messagebox

ARIAL = ("arial",10,"bold")
class OptionsView():
    def __init__(self, win, user, card):
        self.user = user
        self.card = card
        self.win = win
        self.atm = ATM()
        self.money = card.money


        # self.header = Label(self.win, text="TAN BANK", bg="#50A8B0", fg="white", font=("arial", 20, "bold"))
        # self.header.grid(row = 0, column = 0)
        self.uentry = Entry(win, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40)
        self.pentry = Entry(win, bg="honeydew", show="*", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40)
        self.top_frame= Frame(self.win,bg="#50A8B0")
        self.frame = Frame(self.win, bg="#728B8E",width=40,height=12)
        self.left_frame = Frame(self.win)
        self.right_frame = Frame(self.win)

        self.top_frame.grid(row =0,columnspan=3)
        self.frame.grid(row=1, column=1)
        self.left_frame.grid(row=1, column=0)
        self.right_frame.grid(row=1, column=2)

        self.header = Label(self.top_frame, text="TAN BANK", bg="#50A8B0", fg="white", font=("arial", 20, "bold"),width=40)
        self.header.grid()

        self.content = tkinter.Text(self.frame,width=40,height=12,font=("arial", 15, "bold"),bg="#728B8E",fg="white")

        self.content.grid(row = 0)
        info = self.optionsView()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat = DISABLED)

        self.lb1 = Button(self.left_frame, text="查询",width=10, height=3,command=self.searchCardView)
        self.lb2 = Button(self.left_frame, text="存款",width=10, height=3,command=self.deposit_View)
        self.lb3 = Button(self.left_frame, text="改密",width=10, height=3,command=self.changeCardPasswd_view)
        self.lb4 = Button(self.left_frame, text="锁定", width=10, height=3, command=self.lock_view)



        # self.lb1.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # self.lb2.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # self.lb3.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.lb1.grid(row=0, column=0,  sticky=E, padx=5, pady=5)
        self.lb2.grid(row=1, column=0,  sticky=E, padx=5, pady=5)
        self.lb3.grid(row=2, column=0,  sticky=E, padx=5, pady=5)
        self.lb4.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        self.rb1 = Button(self.right_frame, text="转账",width=10, height=3,command=self.transfer_View)
        self.rb2 = Button(self.right_frame, text="取款",width=10, height=3,command=self.withdrawal_View)
        self.rb3 = Button(self.right_frame, text="注销",width=10, height=3,command=self.logout_view)
        self.rb4 = Button(self.right_frame, text="解锁", width=10, height=3,command=self.unlock_view)

        self.rb1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.rb2.grid(row=1, column=0,sticky=W, padx=5, pady=5)
        self.rb3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.rb4.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    #查询
    def searchCardView(self):
        self.text_view()
        a = []
        a.append("该卡已被锁定，请解锁后继续其他操作！")
        if self.card.isLock is True:
            self.content.insert(tkinter.INSERT, a[0])
            self.content.config(stat=DISABLED)
        else:
            self.content.insert(tkinter.INSERT, self.card.money)
            self.content.config(stat=DISABLED)

    #存款
    def deposit_View(self):
        self.text_view()
        self.plabel2 = Label(self.content, text="请输入存款金额：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.depositView)

        self.plabel2.place(x=125, y=80, width=200, height=30)
        self.pentry2.place(x=160, y=110, width=200, height=30)
        self.button.place(x=170, y=220, width=120, height=20)
    def depositView(self):
        print(type(self.pentry2.get()))
        money = int(self.pentry2.get())
        print(type(money))
        info = self.atm.deposit(self.card, money)
        self.text_view()
        if info[0] is True:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
    #取款
    def withdrawal_View(self):
        self.text_view()
        self.plabel2 = Label(self.content, text="请输入取款金额：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.withdrawal)

        self.plabel2.place(x=125, y=80, width=200, height=30)
        self.pentry2.place(x=160, y=110, width=200, height=30)
        self.button.place(x=170, y=220, width=120, height=20)
    def withdrawal(self):
        print(type(self.pentry2.get()))
        money = int(self.pentry2.get())
        print(type(money))
        info = self.atm.withdrawal(self.card, money)
        self.text_view()

        if info[0] is True:


            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:

            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)

    #改密
    def changeCardPasswd_view(self):
        self.text_view()
        self.content.config(stat=DISABLED)
        self.plabel1 = Label(self.content, text="请输入原始密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40,show="*")
        self.plabel2 = Label(self.content, text="请输入新密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40, show="*")
        self.plabel3 = Label(self.content, text="请输验证密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry3 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40, show="*")

        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.changeCardPasswd)

        self.plabel1.place(x=125, y=0, width=200, height=30)
        self.pentry1.place(x=160, y=30, width=200, height=30)
        self.plabel2.place(x=125, y=60, width=200, height=30)
        self.pentry2.place(x=160, y=90, width=200, height=30)
        self.plabel3.place(x=125, y=120, width=200, height=30)
        self.pentry3.place(x=160, y=150, width=200, height=30)
        self.button.place(x=170, y=180, width=120, height=20)
    def changeCardPasswd(self):
        info = self.atm.changeCardPasswd(self.card,self.pentry1.get(),self.pentry2.get(),self.pentry3.get())
        self.text_view()
        if info[0] == -1:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        elif info[0] == -2:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        elif info[0] == 0:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:
            self.card.passwd = info[0]
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
    #转账
    def transfer_View(self):
        self.text_view()
        self.content.config(stat=DISABLED)
        self.plabel1 = Label(self.content, text="请输入对方账号", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel2 = Label(self.content, text="请输入转账金额", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel3 = Label(self.content, text="请输入密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry3 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40, show="*")

        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.transferView)

        self.plabel1.place(x=125, y=0, width=200, height=30)
        self.pentry1.place(x=160, y=30, width=200, height=30)
        self.plabel2.place(x=125, y=60, width=200, height=30)
        self.pentry2.place(x=160, y=90, width=200, height=30)
        self.plabel3.place(x=125, y=120, width=200, height=30)
        self.pentry3.place(x=160, y=150, width=200, height=30)
        self.button.place(x=170, y=180, width=120, height=20)

    def transferView(self):
        self.text_view()
        if self.pentry3.get() != self.card.passwd:
            info = ["密码错误！"]
            self.content.insert(tkinter.INSERT, info[0])
            self.content.config(stat=DISABLED)
        else:
            info = self.atm.transfer(self.card, self.pentry1.get(), self.pentry2.get())
            if info[0] == 0:
                self.content.insert(tkinter.INSERT, info[1])
                self.content.config(stat=DISABLED)
            elif info[0] == 1:
                self.content.insert(tkinter.INSERT, info[1])
                self.content.config(stat=DISABLED)
            else:
                # self.card.passwd = info[0]
                self.content.insert(tkinter.INSERT, info[1])
                self.content.config(stat=DISABLED)
    #锁定
    def lock_view(self):
        info = self.atm.lock(self.user, self.card)
        self.text_view()
        if info[0] is True:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:
            self.card.islock = True
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
    #解锁
    def unlock_view(self):
        info = self.atm.unlock(self.user, self.card)
        self.text_view()
        if info[0] is True:
            self.card.islock = False
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
    def logout_view(self):
        info = self.atm.logout(self.card)
        self.text_view()
        if info[0] is True:
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)
        else:

            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)

            if info[0]==False:
                messagebox.showinfo("退出", "正在退出·······")

                self.win.destroy()

    def optionsView(self):
        print(self.user.name)
        print(self.card.cardId)
        return self.atm.optionsView(self.user.name, self.card.cardId)
    def text_view1(self):
        self.content = tkinter.Text(self.frame,text="添加成功", width=40, height=14, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
    def text_view(self):
        self.content = tkinter.Text(self.frame, width=40, height=14, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
    def welcome_view(self):
        self.win.destroy()
        Welcome()