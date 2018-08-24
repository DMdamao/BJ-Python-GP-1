import tkinter
import tkinter.messagebox
from tkinter_bank.card import Card
from tkinter_bank.person import Person
import bank_atm
import bank_admin
import bank_sys
import time

def addUser(allUsers, name, cardId, password, money):  # 开户
    print(password + "*************")
    card_num = createCardnum(allUsers)  # 卡号
    if money < 0:
        money = 0
    card = Card(card_num, password, money)
    person = Person(name, cardId, card)  # 身份证，卡都ok了，存入到所有用户里
    allUsers[card_num] = person
    bank_sys.bank_updata(allUsers)
    return card_num


def delUser(allUsers, username):  # 销户
    allUsers.pop(username)
    bank_sys.bank_updata(allUsers)


def createCardnum( Users):  # 返回值，判断是否重复，重复了就需要重新生成 6位的吧
    import random
    num = random.choice(range(900000)) + 100000
    while num in Users.keys():
        num = random.choice(range(900000)) + 100000
    return num


def add(allUsers,username,cardId,password,password2,money):
    name1 = username.get()
    cardId1 = cardId.get()
    passwd1 = password.get()
    passwd2 = password2.get()
    money1 = money.get()
    if name1 != "" and cardId1 != "":
        if passwd2 !="" and passwd1 == passwd2:
            if money1 != "":
                money1 = int(money1)
                print(passwd1+"1111111111")
                num = 0
                for x in allUsers.values():
                    print(x.cardId)
                    if cardId1 == x.cardId:
                        num = x.card.num
                if num:
                    tkinter.messagebox.showinfo("开户失败", "该身份证已办理银行卡！")
                    username.set("")
                    cardId.set("")
                    password.set("")
                    password2.set("")
                    money.set("")
                else:

                    card_num = addUser(allUsers, name1, cardId1, passwd1, money1)
                    tkinter.messagebox.showinfo("卡号信息", "请牢记您的卡号：%s" % (card_num))
                    list_mes = []
                    list_mes.append("开户")
                    list_mes.append("+"+str(money1))
                    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    list_mes.append(now_time)
                    allUsers[card_num].card.account_list.append(list_mes)
                    username.set("")
                    cardId.set("")
                    password.set("")
                    password2.set("")
                    money.set("")
                    for x in allUsers.items():
                        print(x[0])
            else:
                tkinter.messagebox.showinfo("开户失败", "预存款不能为0，请输入预存款！" )
        else:
            tkinter.messagebox.showinfo("开户失败", "密码设置错误，请重新输入！")
            password.set("")
            password2.set("")
    else:
        tkinter.messagebox.showinfo("开户失败", "信息输入不完整，请重新输入！")


def remove_user(self,allUsers,username,password):
    for x in allUsers.items():
        print(x[0])

    cardid = (username.get())
    passwd = password.get()
    if cardid != ""and passwd != "":
        cardid = int(cardid)
        if cardid in allUsers:
            if allUsers[cardid].card.lock == False:
                if self.trynum < 2:
                    if passwd == allUsers[cardid].card.passwd:
                        delUser(allUsers,cardid)
                        username.set("")
                        password.set("")
                        tkinter.messagebox.showinfo("销户成功", "%s 已经被销毁！"%cardid)
                    else:
                        tkinter.messagebox.showinfo("销户失败", "密码输入错误，请确认后重新输入！")
                        self.trynum += 1
                        password.set("")
                else:
                    tkinter.messagebox.showinfo("销户失败", "三次输入错误，该卡已经被锁定！")
                    allUsers[cardid].card.lock = True
                    bank_sys.bank_updata(allUsers)
                    self.trynum = 0
            else:
                tkinter.messagebox.showinfo("销户失败", "该卡已经被锁定，无法进行任何操作！")
        else:
            tkinter.messagebox.showinfo("销户失败", "不存在该卡号，请确认后重新输入！")
            username.set("")
            password.set("")
    else:
        tkinter.messagebox.showinfo("销户失败", "信息输入不完整，请重新输入！")


def func2(self,frm,win,allUsers,username,password):#进入ATM界面
    for x in allUsers.items():
        print(x[0],x[1].card.passwd)
    cardid = username.get()
    passwd = password.get()
    if cardid != "" and passwd != "":
        cardid = int(cardid)
        if cardid in allUsers:
            if allUsers[cardid].card.lock == False:
                if self.trynum < 2:
                    if passwd == allUsers[cardid].card.passwd:
                        frm.pack_forget()
                        bank_atm.AtmView(win,allUsers,cardid)
                    else:
                        tkinter.messagebox.showinfo("进入ATM失败", "密码输入错误，请确认后重新输入！")
                        self.trynum += 1
                        print(self.trynum)
                        password.set("")
                else:
                    tkinter.messagebox.showinfo("进入ATM失败", "三次输入错误，该卡已经被锁定！")
                    allUsers[cardid].card.lock = True
                    bank_sys.bank_updata(allUsers)
                    self.trynum = 0
            else:
                tkinter.messagebox.showinfo("进入ATM失败", "该卡已经被锁定，无法进行任何操作！")
        else:
            tkinter.messagebox.showinfo("进入ATM失败", "不存在该卡号，请确认后重新输入！")
            username.set("")
            password.set("")
    else:
        tkinter.messagebox.showinfo("进入ATM失败", "信息输入不完整，请重新输入！")


def func3(frm,win,allUsers,username,password):#进入ATM界面


    cardid = username.get()
    passwd = password.get()
    if cardid != "" and passwd != "":
        if cardid =="xiaoha":
                    if passwd == "123456":
                        frm.pack_forget()
                        bank_admin.AdminView(win,allUsers)
                    else:
                        tkinter.messagebox.showinfo("进入管理员失败", "密码输入错误，请确认后重新输入！")
                        password.set("")

        else:
            tkinter.messagebox.showinfo("进入管理员失败", "不存在该账号，请确认后重新输入！")
            username.set("")
            password.set("")
    else:
        tkinter.messagebox.showinfo("进入ATM失败", "信息输入不完整，请重新输入！")





class bank_View(object):
    def __init__(self):
        self.trynum=0


    def view_Login(self,win,allUsers):

        frm = tkinter.Frame(win)
        frm.pack()

        username = tkinter.StringVar()
        password = tkinter.StringVar()
        tkinter.Label(frm, text='进入ATM', font="15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='卡号: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='密码: ').grid(row=2, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=password, show='*').grid(row=2, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='登录', command=lambda :func2(self,frm,win,allUsers,username,password)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command=win.quit).grid(row=3, column=1, stick=tkinter.E, pady=10)

        return frm

    def view_addUser(self,win,allUsers):
        frm = tkinter.Frame(win)
        frm.pack()
        username = tkinter.StringVar()
        cardId = tkinter.StringVar()
        password = tkinter.StringVar()
        password2 = tkinter.StringVar()
        money = tkinter.StringVar()
        tkinter.Label(frm, text = '开户界面', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text = '姓名: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable = username).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Label(frm, text = '身份证号: ').grid(row=2, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=cardId).grid(row=2, column=1, stick=tkinter.E)
        tkinter.Label(frm, text = '密码:').grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=password, show="*").grid(row=3, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='确认密码:').grid(row=4, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=password2, show = "*").grid(row=4, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='预存款:').grid(row=5, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=money).grid(row=5, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='开户', command=lambda :add(allUsers,username,cardId,password,password2,money)).grid(row=6, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command=win.quit).grid(row=6, column=1, stick=tkinter.E, pady=10)
        for x in allUsers.items():
            print(x[0])
        return frm

    def view_delUser(self,win,allUsers):

        frm = tkinter.Frame(win)
        frm.pack()

        username = tkinter.StringVar()
        password = tkinter.StringVar()
        tkinter.Label(frm, text = '销户界面', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='卡号: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='密码: ').grid(row=2, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=password, show='*').grid(row=2, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='销户',command=lambda :remove_user(self,allUsers,username,password)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command=win.quit).grid(row=3, column=1, stick=tkinter.E, pady=10)

        return frm

    def view_adminLogin(self,win,allUsers):

        frm = tkinter.Frame(win)
        frm.pack()
        username = tkinter.StringVar()
        password = tkinter.StringVar()
        tkinter.Label(frm, text = '管理员登录', font = "15").grid(row=0, column=1, stick=tkinter.W, pady=10)
        tkinter.Label(frm, text='账号: ').grid(row=1, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=username).grid(row=1, column=1, stick=tkinter.E)
        tkinter.Label(frm, text='密码: ').grid(row=2, stick=tkinter.W, pady=10)
        tkinter.Entry(frm, textvariable=password, show='*').grid(row=2, column=1, stick=tkinter.E)
        tkinter.Button(frm, text='登录',command=lambda :func3(frm,win,allUsers,username,password)).grid(row=3, stick=tkinter.W, pady=10)
        tkinter.Button(frm, text='退出', command=win.quit).grid(row=3, column=1, stick=tkinter.E, pady=10)
        return frm
