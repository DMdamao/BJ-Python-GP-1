#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
program name :
last modification time :
changelog :
"""
import tkinter       # 导入tkinter包
from tkinter import ttk
win = tkinter.Tk()        # 创建一个窗体
win.title("theodore")
win.geometry("400x400+0+0")

cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()
# 设置下拉数据
com["value"] = ("黑龙江", "吉林", "辽宁")
# 设置默认值
com.current(0)
# 绑定事件


def func(event):
    print("good", com.get(), cv.get())


com.bind("<<ComboboxSelected>>", func)

win.mainloop()      # 这一步是保存窗口开启的状态，消息循环

