import tkinter
from tkinter_bank.bank_view import bank_View
import pickle
import os
view = bank_View()  # 初始化界面
bank_message = "bank.data"



def bank_updata( allUsers):  # 这个是更新数据的每次修改之后需要重新写入一次
    f = open(bank_message, "wb")
    pickle.dump(allUsers, f)
    f.close()



def loading_mes():  # 读取数据
    if os.path.exists(bank_message):

        if os.path.getsize(bank_message) > 0: # 判断文件是为空，如果为空就创建一个空字典 如果不为空就读取数据
            f = open(bank_message, "rb")
            allUsers = pickle.load(f)
        else:
            allUsers = {}
    else:
        allUsers = {}
    return allUsers


class Bank_Sys(object):

    def  __init__(self,win,allUsers):

        self.allUsers = allUsers
        win.title("银行系统")

        self.frm1 = view.view_Login(win, allUsers)  # ATM界面
        self.frm2 = view.view_adminLogin(win,allUsers)  # 管理员登录界面
        self.frm2.pack_forget()
        self.frm = tkinter.Frame(win)
        self.frm3 = view.view_addUser(win, allUsers)  # 开户界面
        self.frm3.pack_forget()
        self.frm4 = view.view_delUser(win, allUsers)  # 销户界面
        self.frm4.pack_forget()

        # 创建的菜单
        menubar = tkinter.Menu(win)
        win.config(menu=menubar)
        menubar.add_command(label="ATM", command=self.func1)

        menubar.add_command(label="管理员", command=self.func2)

        Bmenu = tkinter.Menu(menubar, tearoff=False)
        Bmenu.add_command(label="开户", command=self.func3)
        Bmenu.add_command(label="销户", command=self.func4)
        menubar.add_cascade(label="办理业务", menu=Bmenu)
        win.mainloop()

    def func1(self):  # 存钱
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm1.pack()

    def func2(self):  # 取钱
        self.frm1.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm2.pack()

    def func3(self):  # 查询
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm4.pack_forget()
        self.frm3.pack()

    def func4(self):  #转账
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack()







