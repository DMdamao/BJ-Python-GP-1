import tkinter
import bank_sys

def center_window(w, h):  # 居中显示
    # 获取屏幕 宽、高
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))

win = tkinter.Tk()
center_window(400,400)
allUsers = bank_sys.loading_mes()
bank_sys.Bank_Sys(win,allUsers)