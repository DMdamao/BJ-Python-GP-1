#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : atm_view.py
# @Author: Janus
# @Date  : 2018/8/14
# @Desc  :
import time
import tkinter
from tkinter import *
from atm import ATM

from welcome_view import Welcome_View
from tkinter import messagebox

ARIAL = ("arial",10,"bold")
class ATM_View():

    def __init__(self,win):
        self.win = win
        self.atm = ATM()
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
        info = self.atmInitView()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat = DISABLED)

        self.lb1 = Button(self.left_frame, text="登陆",width=10, height=3, command=self.checkPasswd_view)
        self.lb2 = Button(self.left_frame, text="提额",width=10, height=3,command=self.addMoney_view)
        self.lb3 = Button(self.left_frame, text="",width=10, height=3)
        self.lb4 = Button(self.left_frame, text="", width=10, height=3)

        self.lb1.grid(row=0, column=0,  sticky=E, padx=5, pady=5)
        self.lb2.grid(row=1, column=0,  sticky=E, padx=5, pady=5)
        self.lb3.grid(row=2, column=0,  sticky=E, padx=5, pady=5)
        self.lb4.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        self.rb1 = Button(self.right_frame, text="关机",width=10, height=3,command = self.win.destroy)
        self.rb2 = Button(self.right_frame, text="改密",width=10, height=3,command = self.changeAtmPasswd_view)
        self.rb3 = Button(self.right_frame, text="",width=10, height=3)
        self.rb4 = Button(self.right_frame, text="", width=10, height=3,command = self.atmInitView_refresh)

        self.rb1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.rb2.grid(row=1, column=0,sticky=W, padx=5, pady=5)
        self.rb3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.rb4.grid(row=3, column=0, sticky=W, padx=5, pady=5)
    def atmInitView(self):
        return self.atm.atmInitView()

    def checkPasswd_view(self):
        self.content = tkinter.Text(self.frame, width=40, height=12, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
        self.content.config(stat=DISABLED)
        # self.content.delete(0,END)
        self.userlabel = Label(self.frame, text="请输入系统账号", bg="#728B8E", fg="white", font=ARIAL)
        self.uentry = Entry(self.frame, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white",width=40)
        self.plabel = Label(self.content, text="请输入系统密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry = Entry(self.content, bg="honeydew", show="*", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white",width=40)
        self.button = Button(self.frame, text="LOGIN", bg="#50A8B0", fg="white", font=ARIAL, command=self.checkPasswd)
        self.userlabel.place(x=125, y=100, width=200, height=30)
        self.uentry.place(x=160, y=130, width=200, height=30)
        self.plabel.place(x=125, y=160, width=200, height=30)
        self.pentry.place(x=160, y=190, width=200, height=30)
        self.button.place(x=170, y=230, width=120, height=20)

    def addMoney_view(self):
        self.text_view()
        self.content.config(stat=DISABLED)
        self.plabel = Label(self.content, text="请输入提额额度", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                            highlightthickness=2,
                            highlightbackground="white", width=40)
        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.addMoney)
        self.plabel.place(x=125, y=160, width=200, height=30)
        self.pentry.place(x=160, y=190, width=200, height=30)
        self.button.place(x=170, y=230, width=120, height=20)

    def changeAtmPasswd_view(self):
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
        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.changeAtmPasswd)


        self.plabel1.place(x=125, y=0, width=200, height=30)
        self.pentry1.place(x=160, y=30, width=200, height=30)
        self.plabel2.place(x=125, y=60, width=200, height=30)
        self.pentry2.place(x=160, y=90, width=200, height=30)
        self.plabel3.place(x=125, y=120, width=200, height=30)
        self.pentry3.place(x=160, y=150, width=200, height=30)
        self.button.place(x=170, y=180, width=120, height=20)
    def changeAtmPasswd(self):
        info = self.atm.changeAtmPasswd(self.pentry1.get(),self.pentry2.get(),self.pentry3.get())
        self.text_view()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)

    def addMoney(self):
        info=self.atm.addMoney(int(self.pentry.get()))
        self.text_view()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)

    def atmInitView_refresh(self):
        self.text_view()
        info = self.atmInitView()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)

    def checkPasswd(self):
        info = self.atm.checkPasswd(self.uentry.get(), self.pentry.get())
        self.content = tkinter.Text(self.frame, width=40, height=12, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)
        if not info[0]:
            self.win.destroy()
            win = tkinter.Tk()
            win.title("ATM")
            win.geometry("800x500+500+200")
            obj = Welcome_View(win)
            win.mainloop()
        else:
            self.text_view()
            self.content.insert(tkinter.INSERT, info[1])
            self.content.config(stat=DISABLED)

    def text_view(self):
        self.content = tkinter.Text(self.frame, width=40, height=12, font=("arial", 15, "bold"), bg="#728B8E",
                                    fg="white")
        self.content.grid(row=0)

# 创建主窗口
win = tkinter.Tk()
win.title("ATM")
win.geometry("800x500+500+200")
obj = ATM_View(win)
win.mainloop()