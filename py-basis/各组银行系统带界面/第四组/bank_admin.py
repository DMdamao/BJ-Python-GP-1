import tkinter
import tkinter.messagebox
import bank_sys

def lock_Accout(allUsers,username):
    cardid = username.get()
    if cardid != "":
        cardid = int(cardid)
        if cardid in allUsers:
            if allUsers[cardid].card.lock ==False:
                allUsers[cardid].card.lock = True
                tkinter.messagebox.showinfo("锁定成功", "该卡已经被锁定！")
            else:
                tkinter.messagebox.showinfo("锁定失败", "该卡已被锁定！")
        else:
            tkinter.messagebox.showinfo("锁定失败", "不存在该卡号！")
            username.set("")
    else:
        tkinter.messagebox.showinfo("锁定失败", "请输入卡号！")

def unlock_Accout(allUsers,username):
    cardid = username.get()
    if cardid != "":
        cardid = int(cardid)
        if cardid in allUsers:
            if allUsers[cardid].card.lock == True:
                allUsers[cardid].card.lock = False
                tkinter.messagebox.showinfo("解锁成功", "该卡已经解锁！")
            else:
                tkinter.messagebox.showinfo("解锁失败", "该卡未被锁定！")
        else:
            tkinter.messagebox.showinfo("解锁失败", "不存在该卡号！")
            username.set("")
    else:
        tkinter.messagebox.showinfo("解锁失败", "请输入卡号！")

def repair_Accout(allUsers,username,password):
    cardid = username.get()
    passwd1 = password.get()
    print(cardid)
    if cardid != "" and passwd1 != "":
        num = 0
        for x in allUsers.values():
            if cardid == x.cardId:
                num = x.card.num
        if num:
            if passwd1 == allUsers[num].card.passwd:

                tkinter.messagebox.showinfo("补卡成功成功", "您的卡号是：%d ，请牢记！！！！"%num)
            else:
                tkinter.messagebox.showinfo("补卡失败", "密码输入错误！")
        else:
            tkinter.messagebox.showinfo("补卡失败", "该身份证没有办理银行卡！")
            username.set("")
            password.set("")
    else:
        tkinter.messagebox.showinfo("补卡失败", "请输入信息！")

def look_Accout(allUsers,frm):
    num=3
    for user in allUsers.values():
        tkinter.Label(frm, text=user.name).grid(row=num, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user.cardId).grid(row=num, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user.card.num).grid(row=num, column=2, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user.card.money).grid(row=num, column=3, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user.card.lock).grid(row=num, column=4, stick=tkinter.W, pady=10)
        num += 1


def back_bank(win,allUsers,frm):
    frm.pack_forget()
    bank_sys.Bank_Sys(win,allUsers)

def view_lockAccount( win,allUsers):
    frm = tkinter.Frame(win)
    frm.pack()
    username = tkinter.StringVar()
    tkinter.Label(frm, text='锁卡', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='卡号: ').grid(row=1, stick=tkinter.W, pady=10)
    tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
    tkinter.Button(frm, text='锁定', command = lambda : lock_Accout(allUsers,username)).grid(row=3, stick=tkinter.W, pady=10)
    tkinter.Button(frm, text='退出', command = lambda :back_bank(win,allUsers,frm)).grid(row=3, column=1, stick=tkinter.E, pady=10)

    return frm


def view_unlockAccount(win,allUsers):
    frm = tkinter.Frame(win)
    frm.pack()
    username = tkinter.StringVar()
    tkinter.Label(frm, text='解卡', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='卡号: ').grid(row=1, stick=tkinter.W, pady=10)
    tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
    tkinter.Button(frm, text='解除', command = lambda : unlock_Accout(allUsers,username)).grid(row=3, stick=tkinter.W, pady=10)
    tkinter.Button(frm, text='退出', command=lambda: back_bank(win, allUsers, frm)).grid(row=3, column=1, stick=tkinter.E,
                                                                                       pady=10)
    return frm


def view_repairAccount( win,allUsers):
    frm = tkinter.Frame(win)
    frm.pack()
    username = tkinter.StringVar()
    password = tkinter.StringVar()
    tkinter.Label(frm, text='补卡', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='身份证号: ').grid(row=1, stick=tkinter.W, pady=10)
    tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
    tkinter.Label(frm, text='密码: ' ).grid(row=2, stick=tkinter.W, pady=10)
    tkinter.Entry(frm, textvariable=password,show = "*").grid(row=2, column=1, stick=tkinter.E)
    tkinter.Button(frm, text='补卡',command=lambda:  repair_Accout(allUsers,username,password)).grid(row=3, stick=tkinter.W, pady=10)
    tkinter.Button(frm, text='退出', command=lambda: back_bank(win, allUsers, frm)).grid(row=3, column=1, stick=tkinter.E,
                                                                                       pady=10)
    return frm


def view_lookAllAccount( win,allUsers):
    frm = tkinter.Frame(win)
    frm.pack()
    tkinter.Label(frm, text='查看所有用户', font="15").grid(row=0, column=2, stick=tkinter.W, pady=10)
    tkinter.Button(frm, text='查看', command=lambda: look_Accout(allUsers, frm)).grid(row=1, stick=tkinter.W,
                                                                                       pady=10)
    tkinter.Button(frm, text='退出', command=lambda: back_bank(win, allUsers, frm)).grid(row=1, column=4, stick=tkinter.E,
                                                                                       pady=10)
    tkinter.Label(frm, text='姓名: \t').grid(row=2, stick=tkinter.W,)
    tkinter.Label(frm, text='身份证号: \t').grid(row=2, column=1, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='卡号: \t').grid(row=2, column=2, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='余额: \t').grid(row=2, column=3, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='是否锁定: \t').grid(row=2, column=4, stick=tkinter.W, pady=10)

    return frm


class AdminView(object):
    def  __init__(self, win,allUsers):
        self.allUsers = allUsers
        win.title("管理员操作界面")
        menubar = tkinter.Menu(win)
        win.config(menu=menubar)
        menubar.add_command(label="锁卡", command=self.func1)
        menubar.add_command(label="解卡", command=self.func2)
        menubar.add_command(label="补卡", command=self.func3)
        menubar.add_command(label="查看所有用户", command=self.func4)
        self.frm1 = view_lockAccount(win,allUsers)  # 锁卡
        self.frm1.pack()
        self.frm2 = view_unlockAccount(win,allUsers)  # 解卡
        self.frm2.pack_forget()
        self.frm3 = view_repairAccount(win,allUsers)  # 补卡
        self.frm3.pack_forget()
        self.frm4 = view_lookAllAccount(win,allUsers)  # 查看所有用户
        self.frm4.pack_forget()
        win.mainloop()

    def func1(self):  # 锁卡
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm1.pack()

    def func2(self):  # 解卡
        self.frm1.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm2.pack()

    def func3(self):  # 补卡
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm4.pack_forget()
        self.frm3.pack()

    def func4(self):  #显示所有用户
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack()










