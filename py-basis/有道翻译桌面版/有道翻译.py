#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/4 下午9:01
@Author  : 北冥神君
@File    : music_gui.py
@Software: PyCharm
"""
from tkinter import *
from fanyi import YoudaoTranslation

# ----------------------主框架部分----------------------

window = Tk()
window.geometry("580x340+520+360") # 设置窗口大小和弹出位置
window.title('有道翻译-BJ-python-GP-1-by北冥')
Label_window = Label(window)


# -----------------------定义规则------------------------

def translate(content):
    youdao = YoudaoTranslation()
    fanyi  = youdao.get_fanyi(content)
    return fanyi

# 还可以继续增加规则函数，只要是两输入的参数都可以
# ----------------------触发函数-----------------------

def Answ():  # 规则函数

    Ans.insert(END, translate(var_first.get()))


def Clea():  # 清空函数
    input_num_first.delete(0, END)  # 这里entry的delect用0
    Ans.delete(0, END)  # text中的用0.0


# ----------------------输入选择框架--------------------
frame_input = Frame(window)
Label_input = Label(frame_input, text='原文', font=('Arial', 20))
var_first = StringVar()
input_num_first = Entry(frame_input, textvariable=var_first)

# ---------------------计算结果框架---------------------
frame_output = Frame(window)
Label_output = Label(frame_output, font=('Arial', 20))
Ans = Listbox(frame_output, height=15, width=40)  # text也可以，Listbox好处在于换行

# -----------------------Button-----------------------

calc = Button(frame_output, text='翻译', width=8,height=3,command=Answ)
cle = Button(frame_output, text='清空',width=8,height=3, command=Clea)
# -----------------------包裹显示-----------------------
Label_window.pack(side=TOP)
frame_input.pack(side=TOP)
Label_input.pack(side=LEFT)

input_num_first.pack(side=LEFT)

frame_output.pack(side=TOP)
Label_output.pack(side=LEFT)
calc.pack(side=LEFT)
cle.pack(side=LEFT)
Ans.pack(side=LEFT)

# -------------------window.mainloop()------------------

window.mainloop()