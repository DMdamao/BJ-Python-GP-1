#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : InputPasswd.py
# @Author: Janus
# @Date  : 2018/8/15
# @Desc  :
import tkinter
from tkinter import *
from atm import ATM
ARIAL = ("arial",10,"bold")
class inputPasswd():
    def __init__(self, win,passwd):
        self.passwd = passwd
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
        self.top_frame = Frame(self.win, bg="#50A8B0")
        self.frame = Frame(self.win, bg="#728B8E", width=40, height=12)
        self.left_frame = Frame(self.win)
        self.right_frame = Frame(self.win)

        self.top_frame.grid(row=0, columnspan=3)
        self.frame.grid(row=1, column=1)
        self.left_frame.grid(row=1, column=0)
        self.right_frame.grid(row=1, column=2)

        self.header = Label(self.top_frame, text="TAN BANK", bg="#50A8B0", fg="white", font=("arial", 20, "bold"), width=40)
        self.header.grid()

        self.content = tkinter.Text(self.frame, width=40, height=12, font=("arial", 15, "bold"), bg="#728B8E", fg="white")

        self.content.grid(row=0)
        info = self.inputPasswd()
        self.content.insert(tkinter.INSERT, info)
        self.content.config(stat=DISABLED)

        self.lb1 = Button(self.left_frame, text="LB1", width=10, height=3)
        self.lb2 = Button(self.left_frame, text="LB2", width=10, height=3)
        self.lb3 = Button(self.left_frame, text="LB3", width=10, height=3)
        self.lb4 = Button(self.left_frame, text="LB4", width=10, height=3)

        # self.lb1.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # self.lb2.pack(side=tkinter.LEFT, fill=tkinter.Y)
        # self.lb3.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.lb1.grid(row=0, column=0, sticky=E, padx=5, pady=5)
        self.lb2.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        self.lb3.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.lb4.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        self.rb1 = Button(self.right_frame, text="RB1", width=10, height=3)
        self.rb2 = Button(self.right_frame, text="RB2", width=10, height=3)
        self.rb3 = Button(self.right_frame, text="RB3", width=10, height=3)
        self.rb4 = Button(self.right_frame, text="RB4", width=10, height=3)

        # self.rb1.pack(side=tkinter.RIGHT ,fill=tkinter.Y)
        # self.rb2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # self.rb3.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.rb1.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.rb2.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.rb3.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.rb4.grid(row=3, column=0, sticky=W, padx=5, pady=5)


    def inputPasswd_view(self):

        self.plabel1 = Label(self.content, text="请输入密码", bg="#728B8E", fg="white", font=ARIAL)
        self.pentry1 = Entry(self.content, bg="honeydew", highlightcolor="#50A8B0",
                             highlightthickness=2,
                             highlightbackground="white", width=40, show="*")

        self.button = Button(self.frame, text="确定", bg="#50A8B0", fg="white", font=ARIAL, command=self.inputPasswd)
        self.plabel1.place(x=125, y=200, width=200, height=30)
        self.pentry1.place(x=160, y=230, width=200, height=30)
        self.button.place(x=170, y=280, width=120, height=20)


    def inputPasswd(self):
        return self.atm.inputPasswd(self.passwd,self.pentry1.get())
