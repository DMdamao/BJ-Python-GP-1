# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import tkinter

class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1)

        self.entryVar = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.entryVar)
        self.entry.pack()

        self.txt = tkinter.Text(frame)
        self.txt.pack()


