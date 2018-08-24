#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/15 上午6:53
@Author  : 北冥神君
@File    : 计算器.py
@Software: PyCharm
"""

import re
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('300x270+400+100')
#不允许修改窗口大小
root.resizable(False,False)
# 设置窗口标题
root.title('计算器')

# 放置信息交流文本框，并设置为只读
contentVar = tkinter.StringVar(root, '')
cententEntry = tkinter.Entry(root, textvariable=contentVar)
cententEntry['state'] = 'readonly'
cententEntry.place(x=10, y=10, width=280, height=20) # 显示位置

# 按钮处理
def buttonClick(btn):
    content = contentVar.get() # 获取按钮内容
    print(content)
    # 如果已有内容是以小数点开头的，前面加0
    if content.startswith('.'):
        content = '0' + content
    if btn in '01234567890':
        content += btn
    elif btn =='.':
        lastPart = re.split(r'\+|-|\*|/]', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误','小数点太多了')
            return None
        else:
            content += btn
    elif btn == 'C':
        content = ''
    elif btn == '=':
        try:
            # 计算
            content = str(eval(content))
        except:
                tkinter.messagebox.showerror('错误','表达式错误')
                return None
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误','不允许存在连续的运算符')
            return None
        content += btn
    elif btn == 'Sqrt':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(),n)):
            content = eval(content)  ** 0.5
        else:
            tkinter.messagebox.showerror('错误','表达式错误')
            return None
    contentVar.set(content)


# 放置清除和等号按钮
btnClear = tkinter.Button(root, text='Clear', command=lambda:buttonClick('C'))
btnClear.place(x=40, y=40, width=80, height=20)
btnComputer = tkinter.Button(root, text='=', command=lambda:buttonClick('='))
btnComputer.place(x=170, y=40, width=80, height=20)

# 放置10个数字、小数点和平方根 按钮
digits = list('01234567890') + ['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(root, text=d,command=lambda x=d:buttonClick(x))
        btnDigit.place(x=20 + col*70, y=80 +row*50, width=50, height=20)

# 放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(root, text=operator, command=lambda  x=operator:buttonClick(x))
    btnOperator.place(x=230, y=80+ index*30, width=50, height=20)

#运行
root.mainloop()

