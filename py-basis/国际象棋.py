#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 国际象棋
@Time    : 2018/8/2 下午5:28
@Author  : 北冥神君
@File    : 国际象棋.py
@Software: PyCharm
"""
import turtle
# 画国际象棋的整体思路是，先画一个黑的或者白色的方块，然后通过两层循环控制落笔坐标。注意一点是，如何控制方块的颜色。


bool_bool =True
turtle.speed(10)
for x in range(-200,200,50):
    for y in  range(-200,200,50):
        print(x,y)
        if bool_bool:
            #画黑色
            turtle.goto(x,y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.end_fill()
            turtle.penup()
        else:
             #画白色
            turtle.goto(x, y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("white")
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.end_fill()
            turtle.penup()
        bool_bool = bool(int(bool_bool)-1)  #画完一个格子之后转换颜色。
    bool_bool = bool(int(bool_bool) - 1)    #画完一列之后转换颜色
    print(bool_bool)
turtle.done()
#bool_bool = bool(int(bool_bool) - 1)  真-->假  假-->真  对应  黑->白  白-->黑
#int(False) = 0,int(True) = 1 bool(0) = False,bool(非零)=True，