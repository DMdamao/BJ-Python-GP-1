import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win=tkinter.Tk()
win.title("sunck")
# win.geometry("900x400+200+0")

info = InfoWindows(win)
tree = TreeWindows(win, r"/Users/tencenting/PycharmProjects/cuiqingcai/基础", info)


win.mainloop()