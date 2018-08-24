#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
program name :
last modification time :
changelog :
"""
import tkinter       # 导入tkinter包
from tkinter import ttk
"""
框架控件
在屏幕上显示一个矩形区域，多作为容器控件
"""
win = tkinter.Tk()        # 创建一个窗体
win.title("theodore")
win.geometry("400x400+0+0")

# frm = tkinter.Frame(win)
# frm.pack()
#
# # left
# frm_l = tkinter.Frame(frm)
# # tkinter.Label(frm_l, text="左上", bg="blue").pack(side=tkinter.TOP)
# # tkinter.Label(frm_l, text="左下", bg="pink").pack(side=tkinter.TOP)
# frm_l.pack(side=tkinter.LEFT)
# # right
# frm_r = tkinter.Frame(frm)
# # tkinter.Label(frm_r, text="右上", bg="yellow").pack(side=tkinter.TOP)
# # tkinter.Label(frm_r, text="右下", bg="green").pack(side=tkinter.TOP)
# frm_r.pack(side=tkinter.RIGHT)
#
# # 表格
# tree = ttk.Treeview(frm_l)
# # 定义列
# tree["columns"] = ("姓名", "年龄", "身高", "体重")
# # 设置列
# tree.column("姓名", width=100)
# tree.column("年龄", width=100)
# tree.column("身高", width=100)
# tree.column("体重", width=100)
#
# tree.heading("姓名", text="名字-name")
# tree.heading("年龄", text="年龄-age")
# tree.heading("身高", text="身高-height")
# tree.heading("体重", text="体重-weight")
#
# # 添加数据
# tree.insert("", 0, text="line1", values=("1", "2", "3", "4"))
# tree.insert("", 1, text="line2", values=("5", "6", "7", "8"))
#
# tree.pack()
#
# tree1 = ttk.Treeview(frm_r)
# tree1.pack()
#
# # 添加一级树枝
# treeF1 = tree1.insert("", 0, "中国", text="中国CHI", values=("F1"))
# treeF2 = tree1.insert("", 1, "美国", text="美国USA", values=("F1"))
# treeF3 = tree1.insert("", 2, "英国", text="英国ENG", values=("F1"))
#
# # 添加二级树枝
# treeF1_1 = tree1.insert(treeF1, 0, "黑龙江", text="中国-黑龙江", values=("F1_1"))
# treeF1_2 = tree1.insert(treeF1, 1, "吉林", text="中国-吉林", values=("F1_2"))
# treeF1_3 = tree1.insert(treeF1, 2, "辽宁", text="中国-辽宁", values=("F1_3"))
#
# treeF2_1 = tree1.insert(treeF2, 0, "德克萨斯州", text="美国-德克萨斯州", values=("F2_1"))
# treeF2_2 = tree1.insert(treeF2, 1, "底特律", text="美国-底特律", values=("F2_2"))
# treeF2_3 = tree1.insert(treeF2, 2, "旧金山", text="美国-旧金山", values=("F2_3"))
#
# # 三级树枝
# treeF1_1_1 = tree1.insert(treeF1_1, 0, "1", text="美国-德克萨斯州", values=("F1_1_1"))
# treeF1_1_2 = tree1.insert(treeF1_1, 1, "2", text="美国-底特律", values=("F1_1_2"))
# treeF1_1_3 = tree1.insert(treeF1_1, 2, "3", text="美国-旧金山", values=("F1_1_3"))

# label1 = tkinter.Label(win, text="good", bg="blue")
# label2 = tkinter.Label(win, text="nice", bg="red")
# label3 = tkinter.Label(win, text="cool", bg="pink")
# label4 = tkinter.Label(win, text="handsome", bg="yellow")

# 绝对布局  宽口的变化对位置没影响
# label1.place(x=10, y=10)
# label2.place(x=50, y=50)
# label3.place(x=100, y=100)
# 相对布局  窗体改变对控件有影响
# tkinter.BOTH
# label1.pack(fill=tkinter.BOTH, side=tkinter.LEFT)
# label2.pack(fill=tkinter.X, side=tkinter.TOP)
# label3.pack(fill=tkinter.Y, side=tkinter.BOTH)

# 表格布局
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1)
# label3.grid(row=1, column=0)
# label4.grid(row=1, column=1)

# 鼠标点击事件
"""
Bi-Motion  当鼠标左键按住小构件且移动鼠标时发生
Button-i  Button-1、Button-2、Button-3表明左键、中键、右键，当在小构
          件上单击鼠标左键时，Tkinter会自动抓取鼠标左键时的指针位置，
          ButtonPressed-i是Button_i的代名词
ButtonPressed-i  当释放鼠标左键时发生
Double-Button-i  当双击鼠标时事件发生
Enter  当鼠标光标进入小构件时事件发生
Key  当单机一个键时发生
Leave  当鼠标光标离开小构件时事件发生
Return  当单机“Enter”键时事件发生，可以将键盘上的任意键
       （像“A”，“B”，“Up”，“Down”，“Left”，“Right”）和一个事件绑定
Shift-A  当单机“Shift+A”键时事件发生，可以将Alt、Shift和Control和其他键组合
Triple-Button-i  当三次单击鼠标左键时事件发生
"""


def func(event):
    """

    :param event:
    :return:
    """
    print(event)


win.bind("<Key>", func)

button1 = tkinter.Button(win, text="leftmouse button")
button1.bind("<Button-1>", func)
button1.pack()

label1 = tkinter.Label(win, text="leftmouse button")
label1.bind("<Button-3>", func)
label1.pack()

win.mainloop()      # 这一步是保存窗口开启的状态，消息循环
