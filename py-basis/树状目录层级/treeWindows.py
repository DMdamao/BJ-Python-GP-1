# -*- coding:utf-8 -*-
import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, other):
        self.other = other

        frame = tkinter.Frame(master)
        frame.grid(row=0,column=0)

        self.tree = tkinter.ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

        #头部
        self.tree.heading("#0",text="Path")

        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        #插入一个节点
        root = self.tree.insert("","end",text=os.path.split(path)[1], open=True, values=(path))
        self.loadtree(root, path)

        #绑定事件
        self.tree.bind( "<<TreeviewSelect>>"   ,self.func)




    def loadtree(self, parent, rootpath):
        # 遍历当前目录
        for path in os.listdir(rootpath):
            # 路径链接
            abspath = os.path.join(rootpath, path)
            # 插入树枝
            oid = self.tree.insert(parent, 'end', text=os.path.split(abspath)[1], open=False, values=(abspath))
            if os.path.isdir(abspath):
                # 递归回去
                if os.path.splitext(abspath)[1] != ".mindnode":
                    self.loadtree(oid, abspath)


    def func(self, event):
        self.select = event.widget.selection()  # 选择
        for idx in self.select:
            file = self.tree.item(idx)["text"]
            filePath = self.tree.item(idx)["values"][0]
            # print(file)
            # print(filePath)
            self.other.entryVar.set(file)
            if os.path.splitext(filePath)[1] == ".py":
                #读取文件内容
                with open(filePath, "r") as f:
                    # print(f.read())
                    self.other.txt.delete(0.0, tkinter.END)
                    self.other.txt.insert(tkinter.INSERT, f.read())
