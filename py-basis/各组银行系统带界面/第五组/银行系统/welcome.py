#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : welcome.py
# @Author: Janus
# @Date  : 2018/8/15
# @Desc  :
import tkinter

ARIAL = ("arial",10,"bold")

class Welcome():

    def __init__(self,win):
        win = tkinter.Tk()
        win.title("ATM")
        win.geometry("800x500+500+200")

        obj = Welcome_View(win)
        win.mainloop()

