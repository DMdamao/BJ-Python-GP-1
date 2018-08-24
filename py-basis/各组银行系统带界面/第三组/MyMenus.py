import tkinter
import csvload as cv
import time

def Menus(me):  # 界面
	old = ""
	new = ""
	Selection = 0     #功能选择标志
	def Lock():        #锁定  Selection = 1
		nonlocal Selection
		Selection = 1
		te.insert(tkinter.END, "您申请锁定操作，请在下方输入您的身份证号！\n")

	def UnLock():        #解锁  Selection = 2
		nonlocal Selection
		Selection = 2
		te.insert(tkinter.END, "您申请解锁操作，请在下方输入您的身份证号！\n")

	def LookScore():        #查询余额
		temp = "余额：%s 元\n" % me.getScore()
		te.insert(tkinter.END, temp)

	def SaveScore():        #存款  Selection = 3
		nonlocal Selection
		Selection = 3
		te.insert(tkinter.END, "请输入存款金额！\n")

	def SubScore():        #取款  Selection = 4
		nonlocal Selection
		Selection = 4
		te.insert(tkinter.END, "请输入取款金额！\n")

	def ToScore():        #转款  Selection = 5
		nonlocal Selection
		Selection = 5
		te.insert(tkinter.END, "请输入您要转账的对方的卡号！\n")

	def ChangePwd():        #修改密码  Selection = 6
		nonlocal Selection
		Selection = 6
		te.insert(tkinter.END, "请输入原始密码！\n")



	def func():    #总函数
		nonlocal old
		nonlocal new
		nonlocal Selection
		nonlocal me
		if Selection == 0:
			te.insert(tkinter.END, "请先选择您的操作！！！\n")
			en.delete(0, tkinter.END)
		elif Selection == 1:   #锁定
			temp = cv.Lock(me, en.get(),1)
			if temp == False:
				te.insert(tkinter.END, "对不起！您输入的身份证信息错误！\n")
			else:
				me = temp
				la8.config(text = me.getFlag())
				te.insert(tkinter.END, "操作成功！用户已被锁定！\n")
			Selection = 0
			en.delete(0, tkinter.END)

		elif Selection == 2:   #解锁
			temp = cv.Lock(me, en.get(),0)
			if temp == False:
				te.insert(tkinter.END, "对不起！您输入的身份证信息错误！\n")
			else:
				me = temp
				la8.config(text = me.getFlag())
				te.insert(tkinter.END, "操作成功！用户已解锁！\n")
			Selection = 0
			en.delete(0, tkinter.END)

		elif Selection == 3:   #存款
			temp = cv.saveScore(me, en.get(), "+")
			if temp == False:
				te.insert(tkinter.END, "对不起！您的卡已被锁定，请解锁！\n")
			else:
				me = temp
				te.insert(tkinter.END, "操作成功！当前余额： %s 元\n" % me.getScore())
			Selection = 0
			en.delete(0, tkinter.END)

		elif Selection == 4:   #取款
			temp = cv.saveScore(me, en.get(), "-")
			if temp == False:
				te.insert(tkinter.END, "对不起！您的卡已被锁定，请解锁！\n")
			elif temp == "负数":
				te.insert(tkinter.END, "对不起！余额不足！\n")
			else:
				me = temp
				te.insert(tkinter.END, "操作成功！正在吐钞。。。\n")
				time.sleep(2)
				te.insert(tkinter.END, "当前余额： %s 元\n" % me.getScore())
			Selection = 0
			en.delete(0, tkinter.END)

		elif Selection == 5:  # 转账1
			old = en.get()
			if cv.reInfo(old) == False:
				te.insert(tkinter.END, "对不起！您输入的账户不存在！\n")
				Selection = 0
				en.delete(0, tkinter.END)
			else:
				te.insert(tkinter.END, "您即将对用户【%s】进行转账操作！\n" % cv.reInfo(old))
				Selection = 50
				en.delete(0, tkinter.END)
				te.insert(tkinter.END, "请输入转账金额！\n")

		elif Selection == 50:  # 转账2
			new = en.get()
			temp = cv.toScore(me, old, new)
			if temp == False:
				te.insert(tkinter.END, "对不起！您的账户已被锁定！请解锁后继续操作\n")
			elif temp == "负数":
				te.insert(tkinter.END, "对不起！余额不足！\n")
			else:
				me = temp
				te.insert(tkinter.END, "操作成功！当前余额： %s 元\n" % me.getScore())
			Selection = 0
			en.delete(0, tkinter.END)

		elif Selection == 6:   #修改密码1
			old = en.get()
			Selection = 60
			en.delete(0, tkinter.END)
			te.insert(tkinter.END, "请输入新密码！\n")

		elif Selection == 60:   #修改密码2
			new = en.get()
			temp = cv.changePwd(me, old, new)
			if temp == False:
				te.insert(tkinter.END, "对不起！您输入的原始密码不正确！\n")
			else:
				me = temp
				te.insert(tkinter.END, "操作成功！请牢记新密码哦！\n" )
			Selection = 0
			en.delete(0, tkinter.END)


	win = tkinter.Tk()
	win.title("中国假设银行ATM自动取款机")
	win.geometry("750x300+300+200")
	win.maxsize(750, 300)
	win.minsize(750, 300)  # 控制窗口的大小，让窗口大小不能改变
	win["background"] = "pink"

	#   标签控件声明
	la1 = tkinter.Label(win, text="欢迎来到中国假设银行办理业务！", bg="pink", fg="red", font=("Arial", 15), anchor=tkinter.SW,
						width=50, height=2, justify="center")
	la2 = tkinter.Label(win, text="用户名：", bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	la3 = tkinter.Label(win, text="卡号：", bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	la4 = tkinter.Label(win, text="请输入：", bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	# 用以显示账户姓名
	la5 = tkinter.Label(win, text=me.name, bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	# 用以显示账户卡号
	la6 = tkinter.Label(win, text=me.cards, bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	la7 = tkinter.Label(win, text="锁定状态：", bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	la8 = tkinter.Label(win, text=me.getFlag(), bg="pink", fg="blue", font=("Arial", 12), anchor=tkinter.SW, width=50,
						height=2, justify="center")
	la9 = tkinter.Label(win, text="提示面板：", bg="pink", fg="blue", font=("Arial", 9), anchor=tkinter.SW, width=50,
						height=2, justify="center")

	#    text控件声明
	te = tkinter.Text(win, width=50, height=10)  # 用以显示操作结果成功还是失败

	#   Entry控件声明
	en = tkinter.Entry(win)  # 输入金额、转账的账户卡号等输入操作

	#  按钮控件声明
	button0 = tkinter.Button(win, text="查询余额", width=9, height=1, command=LookScore, bg="green")
	button1 = tkinter.Button(win, text="存款", width=9, height=1, command=SaveScore, bg="green")
	button2 = tkinter.Button(win, text="取款", width=9, height=1, command=SubScore, bg="green")
	button3 = tkinter.Button(win, text="转账", width=9, height=1, command=ToScore, bg="green")
	button4 = tkinter.Button(win, text="修改密码", width=9, height=1, command=ChangePwd, bg="green")
	button5 = tkinter.Button(win, text="退出", width=9, height=1, command=win.destroy, bg="green")
	button6 = tkinter.Button(win, text="确认", width=9, height=1, command=func, bg="green")
	button7 = tkinter.Button(win, text="锁定", width=7, height=1,command=Lock, bg="green")
	button8 = tkinter.Button(win, text="解锁", width=7, height=1,command=UnLock, bg="green")

	#    整体布局设置
	la1.place(x=280, y=0)  # 欢迎来到中国假设银行办理业务！
	la2.place(x=15, y=50)  # 用户名
	la3.place(x=15, y=100)  # 卡号
	la4.place(x=270, y=250)  # 请输入
	la5.place(x=80, y=52)  # 用以显示账户姓名
	la6.place(x=65, y=102)  # 用以显示账户卡号
	la7.place(x=15, y=200)  # 卡锁定状态
	la8.place(x=100, y=200)  # 未锁定
	la9.place(x=260, y=74)  # 提示面板

	te.place(x=250, y=110)  # 用以显示操作结果成功还是失败
	en.place(x=350, y=270)  # 输入金额、转账的账户卡号等输入操作

	button0.place(x=650, y=25)  # 查询余额
	button1.place(x=650, y=65)  # 存款
	button2.place(x=650, y=105)  # 取款
	button3.place(x=650, y=145)  # 转账
	button4.place(x=650, y=185)  # 修改密码
	button5.place(x=650, y=225)  # 退出
	button6.place(x=525, y=265)  # 确认
	button7.place(x=15, y=250)  # 锁定
	button8.place(x=90, y=250)  # 解锁

	win.mainloop()

if __name__ == "__main__":
	cv.loading()
	cards = input("请输入卡号：")
	pwd = input("请输入密码：")
	me = cv.isPerson(cards,pwd)
	if me:
		print("登陆成功！")
		Menus(me)
	else:
		print("卡号或者密码错误！")
	print("正在保存数据。。")
	cv.Writing()
	print("程序结束！")



