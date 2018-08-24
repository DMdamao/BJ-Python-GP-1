#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
program name :
last modification time :
changelog:
Pillow做验证码
requests爬虫
chardet
os
"""
import tkinter       # 导入tkinter包
win = tkinter.Tk()        # 创建一个窗体
win.title("theodore")
# win.geometry("400x400+0+0")
'''
Label:标签控件
    text:显示文本
    bg:背景颜色
    fg:字体颜色
    font:字体
    width:宽
    height:高
    wraplength:指定text文本换行宽度
    justify:换行后对齐方式
    anchor：位置 center居中 n上 e右 s下 w左
'''
label = tkinter.Label(win,
                      text="good man",
                      bg="pink",
                      fg="red",
                      font=("黑体", 20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="n")
# 挂载到窗口
label.pack()
'''
Button
'''


def func():
    print(e.get())


button = tkinter.Button(win, text="按钮", command=func, width=4, height=2)
button.pack()
'''
Entry:输入控件
用于显示简单的文本内容
    show 密文显示eg:  show="*"
'''
# 绑定变量
e = tkinter.Variable()
# 设置值

entry = tkinter.Entry(win, textvariable=e)
e.set("good man")
entry.pack()
'''
Text:文本控件，用于多行文本

'''
# text = tkinter.Text(win, width=30, height=4)
# 创建滚动条
# scroll = tkinter.Scrollbar(text)
# side=tkinter.RIGHT放到窗口那一侧
# fill 填充
# scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 关联
# scroll.config(command=text.yview)
# text.config(yscrollcommand=scroll.set)
str1 = '''
岩浆，地质学专业术语。火山在活动时不但有蒸汽、石块、晶屑和熔浆团块自火山口喷出，而且还有炽热粘稠的熔融物质自火山口溢流出来。前者被
称为挥发分（volatilecomponent）和火山碎屑物质（volcaniclasticmaterial），后者则叫做熔岩流（lavaflow）。
目前，我们把这种产生于上地幔和地壳深处，含挥发分的高温粘稠的主要成分为硅酸盐的熔融物质称之为岩浆（Magma）。
还有一种解释为，岩浆（Magma）是指地下熔融或部分熔融的岩石。当岩浆喷出地表后，则被称为熔岩（Lava）。喷出地表的岩浆成为喷
出岩（Extrusive rocks）；侵入地壳中的称为侵入岩（Intrusive rocks）。
'''
# text.insert(tkinter.INSERT, str1)
'''
CheckButton多选框控件

'''


# def update():
#     # 清除text中所有内容 0.0：下表为0的第0行 tkinter.END：清空到最后
#     text.delete(0.0, tkinter.END)
#     message = ""
#     if hobby1.get() is True:
#         message += "money\n"
#     if hobby2.get() is True:
#         message += "power\n"
#     if hobby3.get() is True:
#         message += "people\n"
#     text.insert(tkinter.INSERT, message)


# # 绑定变量
# hobby1 = tkinter.BooleanVar()
# hobby2 = tkinter.BooleanVar()
# hobby3 = tkinter.BooleanVar()
# # 多选框
# check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=update)
# check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=update)
# check3 = tkinter.Checkbutton(win, text="people", variable=hobby3, command=update)
# check1.pack()
# check2.pack()
# check3.pack()
'''
RadioButton单选框控件
'''


def update2():
    print(r.get())


# 绑定变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=update2)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=update2)
radio2.pack()
'''
Listbox:列表框控件
可以包含一个或多个文本框
作用：在listbox控件小窗口显示一个字符串
'''
# 绑定变量 , listvariable=lbv
# lbv = tkinter.StringVar()
# 创建一个listbox，添加几个元素  tkinter.BROWSE与tkinter.SINGLE相似，
# 但tkinter.SINGLE不支持鼠标按下移动选中位置
# tkinter.EXTENDED 可以使listbox支持shift和control
# tkinter.MULTIPLE 支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()
for item in [" good", " nice", " handsome"]:
    lb.insert(tkinter.END, item)
# 在开始添加
# lb.insert(tkinter.ACTIVE, " cool")
# 将列表当成一个元素添加
# lb.insert(tkinter.END, [" very cool", " very nice"])
# 删除  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引出的内容
# lb.delete(1, 3)
# 选中  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引出的内容
# lb.select_set(2, 4)
# 取消选中
# lb.select_clear(3)
# 获取到列表中元素的个数
# print(lb.size())
# 获取选中元素
# print(lb.get(2, 4))
# 返回当前选中的索引项
# print(lb.curselection())
# 判断一个选项是否被选中
# print(lb.select_includes(1))
# 打印当前列表中的选项
# print(lbv.get())
# 设置选项
# lbv.set(("1", "2", "3"))
# 绑定事件


# def myprint(event):
#     print(lb.get(lb.curselection()))


# lb.bind("<Double-Button-1>", myprint)
# scroll2 = tkinter.Scrollbar()
# scroll2.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# lb.configure(yscrollcommand=scroll2.set)
# scroll2['command'] = lb.yview()
'''
Scale
供用户拖拽指示器改变变量的值，可以水平，也可以竖直
'''
# orient=tkinter.HORIZONTAL 水平的  tkinter.VERTICAL 竖直
# 水平时length表示宽度竖直时表示高度
# tickinterval现实值将会为该值倍数
scale1 = tkinter.Scale(win, from_=0, to=100,
                       orient=tkinter.HORIZONTAL,
                       tickinterval=100, length=200)
# 设置值
scale1.set(20)


def shownum():
    print(scale1.get())


tkinter.Button(win, text="按钮", command=shownum).pack()
scale1.pack()
'''
Spinbox:数字范围控件
'''
# 绑定变量
v = tkinter.StringVar()
# increment=5 增加或减小的步长，默认为1
# values 最好不要和from_ ，to一起用  from_=0, to=100, increment=1,
# command 只要值改变就会执行对应方法
sp = tkinter.Spinbox(win, values=(0, 2, 4, 6, 8), textvariable=v)
sp.pack()
# 设置值
v.set(20)
# 取值
print(v.get())
'''
Menu:顶层菜单
'''
# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)
# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)


def func():
    print("good")


# 给菜单添加内容
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "汇编", "NodeJS", "Exit"]:
    if item == "Exit":
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)
# 向菜单条上添加菜单
menubar.add_cascade(label="语言", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="233")
menubar.add_cascade(label="神马", menu=menu2)

# 右键菜单
menubar2 = tkinter.Menu(win)
menu3 = tkinter.Menu(menubar2, tearoff=False)
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "汇编", "NodeJS", "Exit"]:
    menu3.add_command(label=item)
menubar2.add_cascade(label="3", menu=menu3)


def showMenu(event):
    menubar2.post(event.x_root, event.y_root)


win.bind("<Button-3>", showMenu)
'''
Combobox
'''
'''
Frame
'''

win.mainloop()      # 这一步是保存窗口开启的状态，消息循环


