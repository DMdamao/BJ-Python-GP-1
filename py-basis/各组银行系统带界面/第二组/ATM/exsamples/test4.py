#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
program name :
last modification time :
changelog :
"""

import tkinter  # 导入Tkinter模块
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("1024x768+500+100")

# im = tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open("img.gif")
im = ImageTk.PhotoImage(image)  # image
canvas = tkinter.Canvas(root, width=1024, height=768, bg='white')
canvas.create_image((0, 0), image=im)  # 1440, 1280  1024, 768 (512, 384)
canvas.place(x=0, y=0)
# lb1 = tkinter.Label(root, text="123", image=im)
# lb1.pack()
root.mainloop()
