import tkinter as tk
from tkinter import Frame, Label, W, E, Button, LEFT, RIGHT, BOTH, YES, NO, TOP, Variable,messagebox
from singleton import singletonDeco
from atm import ATM
from tkinter import *
import atmInitView

import math, sys, time

atm = ATM()
'''松耦合'''
# 返回*********************************************************************************
class BackDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('是否返回')
        self.isback = 0
        # 弹窗界面

    def setup_UI(self):
        # 第一行（两列）
        self.geometry("300x150+810+320")

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=20)
        Label(row1, text="是否返回初始界面？", font=("宋体", 15), width=30).pack(side=TOP)

        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)
    def ok(self):
        self.destroy()
        self.isback = 1
    def cancel(self):
        self.destroy()


# 改密*********************************************************************************
class changePasswdDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('加钞输入框')
        # 弹窗界面

    def setup_UI(self):
        self.geometry("350x200+790+300")
        self.tip = tk.StringVar()
        self.old_passwd = tk.StringVar()

        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=5)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP,pady=5)
        tk.Label(row1, text='管理员原密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.old_passwd, width=20, show="*").pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(side=TOP, pady=5)
        tk.Label(row2, text='管理员新密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.new_passwd1, width=20, show="*").pack(side=tk.LEFT)

        # 第三行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=5)
        tk.Label(row3, text='再次确认新密码：', font=("宋体", 10), width=15).pack(side=tk.LEFT)
        self.new_passwd2 = tk.StringVar()
        tk.Entry(row3, textvariable=self.new_passwd2, width=20, show="*").pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(side=TOP, pady=10)
        tk.Button(row4, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row4, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)

    def ok(self):
        # print(atm.passwd,self.old_passwd.get())
        if self.old_passwd.get() != "":
            if atm.passwd != self.old_passwd.get():
                self.tip.set("原密码输入错误！")
            else:
                if self.new_passwd1.get() != "":
                    if self.new_passwd1.get() != self.new_passwd2.get():
                        self.tip.set("新密码两次输入不一致！")
                    else:
                        atm.passwd = self.new_passwd1.get()
                        messge = messagebox.askokcancel("消息框", "密码修改成功！请牢记新密码：%s" % atm.passwd)
                        try:
                            self.wait_window(messge)
                        except:
                            pass
                        self.destroy()
                else:
                    self.tip.set("新密码不能为空！")

        else:
            self.tip.set("原密码不能为空！")

        self.old_passwd.set("")
        self.new_passwd1.set("")
        self.new_passwd2.set("")

    def cancel(self):
        self.destroy()

# 加钞*********************************************************************************
class InputDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('提款输入框')
        # 弹窗界面

    def setup_UI(self):
        # 第一行（两列）
        self.geometry("350x200+790+320")
        self.tip = tk.StringVar()

        row1 = tk.Frame(self)
        row1.pack(side=TOP, pady=30)
        Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP)
        tk.Label(row1, text='请输入添加款数：', font=("宋体", 10), width=15).pack(side=tk.LEFT, pady=5)
        self.money = tk.StringVar()
        tk.Entry(row1, textvariable=self.money, width=20).pack(side=tk.LEFT)  # 第二行
        row3 = tk.Frame(self)
        row3.pack(side=TOP, pady=20)
        tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT, padx=20)
        tk.Button(row3, text="确定", width=10, command=self.ok).pack(side=tk.LEFT, padx=40)
    def ok(self):
        try:
            acount = float(self.money.get())
            math.sqrt(acount)
            atm.money += acount
            # print(atm.money)
            messge = messagebox.askokcancel("消息框", "加钞成功！当前机器余额：%.2f" % atm.money)
            try:
                self.wait_window(messge)
            except:
                pass
            self.destroy()
        except Exception as e:
            self.tip.set("款数输入错误！请重新输入")
            self.money.set("")

    def cancel(self):
        self.destroy()


# 主窗******************************************************************************************

class RootLoginView(tk.Tk):
    def __init__(self):
        super().__init__()

    def setupRootLoginUI(self):
        # self.pack() # 若继承 tk.Frame ，此句必须有！
        self.title('管理员操作界面')
        self.geometry("900x600+500+150")
        # 程序参数/数据
        self.tipVar = Variable()
        self.tipVar.set("当前ATM机内余额为：%.2f" % atm.money)
        self.resizable(width=False, height=False)
        # 使用Frame增加一层容器

        fm1 = Frame(self)
        fm2 = Frame(self)
        fm3 = Frame(self)

        # img_gif = PhotoImage(file="1.gif")
        # lable_img = Label(self, image=img_gif,z_index =-99)
        # lable_img.pack()

        button_image_gif3 = PhotoImage(file="提额.gif")
        Button(fm1, text='加钞', font=("宋体", 15),image=button_image_gif3, width=190, height=45, command=self.addCharge).pack(side=TOP, anchor=W,
                                                                                                 expand=NO)
        button_image_gif4 = PhotoImage(file="改密按钮.gif")
        Button(fm1, text='改密', font=("宋体", 15), image=button_image_gif4, width=190, height=45, command=self.modPasswd).pack(side=TOP, anchor=W,
                                                                                                 expand=NO, pady=80)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES, pady=150)

        Label(fm3, text="欢迎进入sunck银行管理员操作界面，非管理员请勿操作！谢谢合作！",
              font=("宋体", 15), width=30, height=7, wraplength=350).pack(side=TOP)
        Label(fm3, textvariable=self.tipVar, font=("宋体", 15), width=30, height=10).pack(side=TOP)
        fm3.pack(side=LEFT, fill=BOTH, expand=YES)

        button_image_gif5 = PhotoImage(file="关机按钮.gif")
        Button(fm2, text='关机', font=("宋体", 15), image=button_image_gif5, width=190, height=45, command=self.shutdown).pack(side=TOP, anchor=E,
                                                                                                expand=NO)
        button_image_gif6 = PhotoImage(file="返回按钮.gif")
        Button(fm2, text='返回', font=("宋体", 15), image=button_image_gif6, width=190, height=45, command=self.back).pack(side=TOP, anchor=E,
                                                                                            expand=NO, pady=80)
        fm2.pack(side=RIGHT, fill=BOTH, expand=YES, pady=150)
        self.mainloop()

    # 设置参数
    def addCharge(self):
        # print("addCharge")
        inDlog = InputDialog()
        inDlog.setup_UI()
        self.wait_window(inDlog)    #  等待窗口修改值
        self.tipVar.set("当前ATM机内余额为：%.2f" % atm.money)

    def shutdown(self):
        sys.exit(0)

    def modPasswd(self):
        chPwdDlog = changePasswdDialog()
        chPwdDlog.setup_UI()
        self.wait_window(chPwdDlog)

    def back(self):
        res = self.backView()
        # print("========", res)
        if res:
            self.quit()
            self.destroy()
            atmView = atmInitView.ATMInitView()
            atmView.setupATMInitView()



    def backView(self):
        backDlog = BackDialog()
        backDlog.setup_UI()
        self.wait_window(backDlog)
        return backDlog.isback

# if __name__ == '__main__':
# atm = ATM()
# rview = RootView()
# rview.mainloop()
# try:
#     rview.destroy()
# except:
#     print("root Exce")

# rootView = RootLoginView()
# rootView.setupRootLoginUI()
