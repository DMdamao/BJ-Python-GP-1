#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : welcome_view.py
# @Author: Janus
# @Date  : 2018/8/15
# @Desc  :
import tkinter
from tkinter import *
from atm import ATM
from optionsView import OptionsView
from tkinter import messagebox

ARIAL = ("arial",10,"bold")

class Welcome_View():
    def __init__(self,win,):

        self.win = win
        self.atm = ATM()

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
        info = self.welcomeView()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat = DISABLED)

        self.lb1 = Button(self.left_frame, text="插卡",width=10, height=3,command = self.checkCard_view )
        self.lb2 = Button(self.left_frame, text="补卡",width=10, height=3,command=self.reisse_View)
        self.lb3 = Button(self.left_frame, text="",width=10, height=3)
        self.lb4 = Button(self.left_frame, text="", width=10, height=3)

        self.lb1.grid(row=0, column=0,  sticky=E, padx=5, pady=5)
        self.lb2.grid(row=1, column=0,  sticky=E, padx=5, pady=5)
        self.lb3.grid(row=2, column=0,  sticky=E, padx=5, pady=5)
        self.lb4.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        self.rb1 = Button(self.right_frame, text="开户",width=10, height=3,command = self.createCard_view)
        self.rb2 = Button(self.right_frame, text="返回",width=10, height=3)
        self.rb3 = Button(self.right_frame, text="",width=10, height=3)
        self.rb4 = Button(self.right_frame, text="", width=10, height=3,command = self.welcome)

        self.rb1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.rb2.grid(row=1, column=0,sticky=W, padx=5, pady=5)
        self.rb3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.rb4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

    def welcomeView(self):
        return self.atm.welcomeView()

    def createCard_view(self):
        self.content = tkinter.Text(self.frame, width=40, height=14, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
        self.content.config(stat=DISABLED)
        self.plabel1 = Label(self.content, text="请输入您的身份证号：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel2 = Label(self.content, text="请输入您的姓名：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel3 = Label(self.content, text="请输入您的手机号：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry3 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel4 = Label(self.content, text="请设置密码：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry4 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40, show="*")
        self.plabel5 = Label(self.content, text="输入预存款：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry5 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)

        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.createCard)

        self.plabel1.place(x=120, y=0, width=200, height=30)
        self.pentry1.place(x=160, y=25, width=200, height=30)
        self.plabel2.place(x=110, y=50, width=200, height=30)
        self.pentry2.place(x=160, y=75, width=200, height=30)
        self.plabel3.place(x=110, y=100, width=200, height=30)
        self.pentry3.place(x=160, y=125, width=200, height=30)
        self.plabel4.place(x=110, y=150, width=200, height=30)
        self.pentry4.place(x=160, y=175, width=200, height=30)
        self.plabel5.place(x=110, y=200, width=200, height=30)
        self.pentry5.place(x=160, y=225, width=200, height=30)
        self.button.place(x=170, y=260, width=120, height=20)
    def createCard(self):
        self.text_view()
        info = self.atm.createCard(self.pentry1.get(),self.pentry2.get(),self.pentry3.get(),self.pentry4.get(),self.pentry5.get())
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)

    def text_view(self):
        self.content = tkinter.Text(self.frame, width=40, height=14, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)

    def checkCard_view(self):
        self.text_view()
        self.plabel1 = Label(self.content, text="输入您的卡号：：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel2 = Label(self.content, text="请输入您的密码：", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40,show="*")
        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL,
                             command=self.checkCard)

        self.plabel1.place(x=125, y=80, width=200, height=30)
        self.pentry1.place(x=160, y=110, width=200, height=30)
        self.plabel2.place(x=125, y=140, width=200, height=30)
        self.pentry2.place(x=160, y=170, width=200, height=30)
        self.button.place(x=170, y=220, width=120, height=20)
    #插卡
    def checkCard(self):
        info =self.atm.checkCard(self.pentry1.get(),self.pentry2.get())
        if info[0]:
            self.win.destroy()
            win = tkinter.Tk()
            win.title("ATM")
            win.geometry("800x500+500+200")
            print(info[2], info[3])
            obj = OptionsView(win,info[2],info[3])

            win.mainloop()
        else:
            self.text_view()
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)

    def welcome(self):
        self.content = tkinter.Text(self.frame, width=40, height=14, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
        info = self.welcomeView()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)
    def reisse_View(self):
        self.text_view()
        self.content.config(stat=DISABLED)
        self.plabell = Label(self.content, text="请输入身份证号:", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel2 = Label(self.content, text="请输入要补办的卡号:", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry2 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)
        self.plabel3 = Label(self.content, text="请设置密码:", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry3 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40)

        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.rereisse)

        self.plabell.place(x=125, y=110, width=200, height=30)
        self.pentry1.place(x=160, y=140, width=200, height=30)
        self.plabel2.place(x=125, y=170, width=200, height=30)
        self.pentry2.place(x=160, y=200, width=200, height=30)
        self.plabel3.place(x=125, y=230, width=200, height=30)
        self.pentry3.place(x=160, y=260, width=200, height=30)
        self.button.place(x=170, y=300, width=120, height=20)

    def rereisse(self):

        info = self.atm.reisse(self.pentry1.get(), self.pentry2.get(), self.pentry3.get())
        self.text_view()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)



# # 创建主窗口
# win = tkinter.Tk()
# win.title("ATM")
# win.geometry("800x500+500+200")
# obj = ATM_View(win)
# win.mainloop()