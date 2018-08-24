import tkinter
import tkinter.messagebox
import bank_sys
import time

def back_bank(win,allUsers,frm):
    frm.pack_forget()
    bank_sys.Bank_Sys(win,allUsers)

def addmoney( allUsers, cardid, money):
    allUsers[cardid].card.money += money
    list_mes = []
    list_mes.append("存钱")
    list_mes.append("+" + str(money))
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list_mes.append(now_time)
    allUsers[cardid].card.account_list.append(list_mes)
    bank_sys.bank_updata(allUsers)


def outmoney( allUsers, cardid, money):
    allUsers[cardid].card.money -= money
    list_mes = []
    list_mes.append("取钱")
    list_mes.append("-" + str(money))
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list_mes.append(now_time)
    allUsers[cardid].card.account_list.append(list_mes)
    bank_sys.bank_updata(allUsers)


def transmoney( allUsers, cardid1, cardid2, money):
    allUsers[cardid1].card.money -= money
    allUsers[cardid2].card.money += money
    list_mes = []
    list_mes.append("转出")
    list_mes.append("-" + str(money))
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list_mes.append(now_time)
    allUsers[cardid1].card.account_list.append(list_mes)
    list_mes1 = []
    list_mes1.append("转入")
    list_mes1.append("+" + str(money))
    list_mes1.append(now_time)
    allUsers[cardid2].card.account_list.append(list_mes1)
    bank_sys.bank_updata(allUsers)


def add_money(allUsers,cardid,money):
    money1 = money.get()
    if money1 != "":
        money1 = int(money1)
        if money1 > 0:
            addmoney(allUsers,cardid,money1)
            tkinter.messagebox.showinfo("存钱成功", "当前余额为：%d ！"%allUsers[cardid].card.money)
        else:
            tkinter.messagebox.showinfo("存钱失败", "存钱金额不能小于0！")
            money.set("")
    else:
        tkinter.messagebox.showinfo("存钱失败", "请输入存钱金额！")


def out_money(allUsers,cardid,money):
    money1 = money.get()
    if money1 != "":
        money1 = int(money1)
        if money1 < allUsers[cardid].card.money:
            outmoney(allUsers, cardid, money1)
            tkinter.messagebox.showinfo("取钱成功", "当前余额为：%d ！" % allUsers[cardid].card.money)
        else:
            tkinter.messagebox.showinfo("取钱失败", "卡上余额不足，当前余额为：%d ！请重新输入" % allUsers[cardid].card.money)
            money.set("")
    else:
        tkinter.messagebox.showinfo("取钱失败", "请输入存钱金额！")

def look_money(allUsers,cardid,money):
    money.set(allUsers[cardid].card.money)

def trans_money(allUsers,card_num, money,cardid):
    cardid1 = cardid.get()
    money1 = money.get()
    if cardid1 != "" and money1 != "":
        cardid1 = int(cardid1)
        money1 = int(money1)
        if cardid1 in allUsers:
            if money1 < allUsers[card_num].card.money:
                transmoney(allUsers, card_num,cardid1,money1)
                tkinter.messagebox.showinfo("转账成功", "当前余额为：%d ！" % allUsers[card_num].card.money)
            else:
                tkinter.messagebox.showinfo("转账失败", "卡上余额不足，当前余额为：%d ！请重新输入" % allUsers[card_num].card.money)
                money.set("")
        else:
            tkinter.messagebox.showinfo("转账失败", "不存在该卡号，请确认后重新输入！")
            money.set("")
            cardid.set("")
    else:
        tkinter.messagebox.showinfo("转账失败", "信息输入不完整，请重新输入！")

def look_Bill(allUsers, frm,cardid):
    num = 3
    for user in allUsers[cardid].card.account_list:
        tkinter.Label(frm, text=user[0]).grid(row=num, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user[1]).grid(row=num, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text=user[2]).grid(row=num, column=2, stick=tkinter.W, pady=10)

        num += 1





def view_addMoney(win1,allUsers,cardid):
        frm = tkinter.Frame(win1)
        frm.pack()
        money = tkinter.StringVar()
        tkinter.Label(frm, text = '存钱', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='金额: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=money).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='存钱',command = lambda : add_money(allUsers,cardid,money)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出',command = lambda :back_bank(win1,allUsers,frm)).grid(row=3, column=1, stick=tkinter.E, pady=10)
        return frm

def view_outMoney(win1,allUsers,cardid):
        frm = tkinter.Frame(win1)
        frm.pack()
        money = tkinter.StringVar()
        tkinter.Label(frm, text = '取钱', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='金额: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=money).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='取钱',command = lambda :out_money(allUsers,cardid,money)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command = lambda :back_bank(win1,allUsers,frm)).grid(row=3, column=1, stick=tkinter.E, pady=10)
        return frm


def view_lookMoney(win1,allUsers,cardid):
        frm = tkinter.Frame(win1)
        frm.pack()
        username = tkinter.StringVar()
        tkinter.Label(frm, text = '查询', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='余额: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='查询', command = lambda :look_money(allUsers,cardid, username)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command = lambda :back_bank(win1,allUsers,frm)).grid(row=3, column=1, stick=tkinter.E, pady=10)
        return frm
def view_lookBill( win,allUsers,cardid):
    frm = tkinter.Frame(win)
    frm.pack()
    tkinter.Label(frm, text='查看所有用户', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
    tkinter.Button(frm, text='查看', command=lambda: look_Bill(allUsers, frm,cardid)).grid(row=1, stick=tkinter.W,
                                                                                       pady=10)
    tkinter.Button(frm, text='退出', command=lambda: back_bank(win, allUsers, frm)).grid(row=1, column=2, stick=tkinter.E,
                                                                                       pady=10)
    tkinter.Label(frm, text='操作: \t\t').grid(row=2, stick=tkinter.W,)
    tkinter.Label(frm, text='钱数: \t\t').grid(row=2, column=1, stick=tkinter.W, pady=10)
    tkinter.Label(frm, text='时间: \t\t').grid(row=2, column=2, stick=tkinter.W, pady=10)


    return frm


def view_transMoney(win1,allUsers,card_num):
        frm = tkinter.Frame(win1)
        frm.pack()
        money = tkinter.StringVar()
        cardid = tkinter.StringVar()
        tkinter.Label(frm, text='转账', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='金额: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=money).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='卡号: ').grid(row=2, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=cardid).grid(row=2, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='转账',command = lambda :trans_money(allUsers,card_num, money,cardid) ).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command = lambda :back_bank(win1,allUsers,frm)).grid(row=3, column=1, stick=tkinter.E, pady=10)
        return frm


class AtmView(object):

    def  __init__(self,win1,allUsers,cardid):

        self.allUsers = allUsers
        self.cardid = cardid
        win1.title("ATM")
        menubar = tkinter.Menu(win1)
        win1.config(menu=menubar)
        menubar.add_command(label="存钱", command=self.func1)
        menubar.add_command(label="取钱", command=self.func2)
        menubar.add_command(label="查询", command=self.func3)
        menubar.add_command(label="转账", command=self.func4)
        menubar.add_command(label="账单", command=self.func5)
        self.frm1 = view_addMoney(win1, allUsers,cardid)  # 存钱
        self.frm1.pack()
        self.frm2 = view_outMoney(win1,allUsers,cardid)  # 取钱
        self.frm2.pack_forget()
        self.frm3 = view_lookMoney(win1,allUsers,cardid)  # 查询
        self.frm3.pack_forget()
        self.frm4 = view_transMoney(win1,allUsers,cardid)  # 转账
        self.frm4.pack_forget()
        self.frm5 = view_lookBill(win1, allUsers, cardid)  # 转账
        self.frm5.pack_forget()
        win1.mainloop()

    def func1(self):  # 存钱
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm5.pack_forget()
        self.frm1.pack()

    def func2(self):  # 取钱
        self.frm1.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm5.pack_forget()
        self.frm2.pack()

    def func3(self):  # 查询
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm4.pack_forget()
        self.frm5.pack_forget()
        self.frm3.pack()

    def func4(self):  #转账
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm5.pack_forget()
        self.frm4.pack()

    def func5(self):  #转账
        self.frm1.pack_forget()
        self.frm2.pack_forget()
        self.frm3.pack_forget()
        self.frm4.pack_forget()
        self.frm5.pack()









