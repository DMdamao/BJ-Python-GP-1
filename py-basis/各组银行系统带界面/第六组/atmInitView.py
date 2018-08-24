import tkinter as tk
from  tkinter import Frame,Label,W,E,Button,LEFT,RIGHT,BOTH,YES,NO,TOP
from atm import ATM
from tkinter import *
import rootView,optionsView


'''松耦合'''
atm = ATM()
# 弹窗
class MyDialog(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title('管理员登录')
    self.isLogin = 0
    # 弹窗界面
  def rootlogin(self):
    # 第一行（两列）
    self.geometry("450x200+725+350")
    row1 = tk.Frame(self)
    self.tip = tk.StringVar()

    row1.pack(side= TOP, pady = 20)
    Label(row1, textvariable=self.tip, font=("宋体", 10), width=30).pack(side=TOP)
    Label(row1, text='管理员帐号：', font=("宋体", 10), width=10).pack(side=tk.LEFT,pady = 5)
    self.name = tk.StringVar()
    tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)
    # 第二行
    row2 = tk.Frame(self)
    row2.pack(side= TOP)
    tk.Label(row2, text='管理员密码：', font=("宋体", 10), width=10).pack(side=tk.LEFT)
    self.passwd = tk.StringVar()
    tk.Entry(row2, textvariable=self.passwd, width=20,show="*").pack(side=tk.LEFT)
    # 第三行
    row3 = tk.Frame(self)
    row3.pack( side= TOP, pady = 20)
    tk.Button(row3, text="取消", width=10, command=self.cancel).pack(side=tk.RIGHT,padx= 20)
    tk.Button(row3, text="确定", width=10,  command=self.ok).pack(side=tk.LEFT,padx = 40)

  def ok(self):
    atm = ATM()
    # print(self.passwd,self.name,atm.passwd,atm.account)
    if self.passwd.get() != atm.passwd or self.name.get() != atm.account:
        self.tip.set("账号或密码错误！请重新输入")
        self.name.set("")
        self.passwd.set("")
    else:
        self.destroy() # 销毁窗口
        self.isLogin = self.passwd.get()


  def cancel(self):
    self.destroy()


# 主窗

class ATMInitView(tk.Tk):
  def __init__(self):
    super().__init__()
  def setupATMInitView(self):
    # self.pack() # 若继承 tk.Frame ，此句必须有！
    self.title('ATM开机界面')
    self.geometry("900x600+500+150")


    # 程序参数/数据

    self.resizable(width=False, height=False)


    fm1 = Frame(self)
    fm2 = Frame(self)
    fm3 = Frame(self)




    button_image_gif1 = PhotoImage(file="管理员登录按钮.gif")
    Button(fm1, text='管理', font=("宋体", 10),image=button_image_gif1, width=140, height=28, command=self.setup_config).pack(side=TOP, anchor=W,
                                                                                                  expand=NO)
    fm1.pack(side=LEFT, fill=BOTH, expand=YES, pady=250)

    Label(fm3, text=self.bug, font=("宋体", 15), width=50).pack(side=TOP, pady=30)
    Label(fm3, text="佛系编程，永无BUG", font=("宋体", 20), width=30, height=10).pack(side=TOP, expand=NO)
    fm3.pack(side=LEFT, fill=BOTH, expand=NO)

    button_image_gif2 = PhotoImage(file="普通用户登录按钮.gif")
    Button(fm2, text='普通', font=("宋体", 10), image=button_image_gif2,width=140, height=28,command=self.enterOpView).pack(side=TOP, anchor=E, expand=NO)

    fm2.pack(side=RIGHT, fill=BOTH, expand=YES, pady=250)
    self.mainloop()


  # 设置参数
  def setup_config(self):
    res = self.backsetup_config()
    # print("*********",res)
    if res:
        self.quit()
        self.destroy()
        # rView = rootView.RootView()
        rLView = rootView.RootLoginView()
        rLView.setupRootLoginUI()

  def backsetup_config(self):
    myDialog = MyDialog()
    myDialog.rootlogin()
    self.wait_window(myDialog)
    return  myDialog.isLogin

  def enterOpView(self):
    self.quit()
    self.destroy()
    opView = optionsView.OptionsView()
    opView.setupOptionsView()
  bug =r'''
    _ooOoo_  
    o8888888o  
    88" . "88  
    (| -_- |)  
    O\ = /O  
    ____/`---'\____  
  .'   \\| |// `.  
    / \\||| : |||// \  
    / _||||| -:- |||||- \  
    | | \\\ - /// | |  
    | \_| ''\---/'' |_/ |  
    \ .-\__ `-` ___/-. /  
  ___`. .' /--.--\ `. . __  
  ."" '< `.___\_<|>_/___.' >'"".  
   | | : `- \`.;`\ _ /`;.`/ - `: | |  
   \ \ `-. \_ __\ /__ _/ .-` / /  
   ======`-.____`-.___\_____/___.-`____.-'======  
   `=---='  
  '''

# if __name__ == '__main__':
# app = ATMInitView()
# app.mainloop()
# try:
#     app.destroy()
# except:
#     print("atm Exce")
# app = ATMInitView()
# app.setupATMInitView()






