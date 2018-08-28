#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 登陆界面模块
@Time    : 2018/8/19 下午9:25
@Author  : 北冥神君
@File    : login.py
@Software: PyCharm
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import *

from . import memory, client_socket, contact_form, register, common_handler, security


class LoginForm(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        memory.Login_window = self.master
        self.master.resizable(width=False, height=False)  # 禁止修改登陆窗口大小
        self.master.geometry('300x160')   # 窗口大小

        self.label_1 = Label(self, text="QQ账号")
        self.label_2 = Label(self, text="QQ密码")

        self.username = Entry(self)
        self.password = Entry(self, show="*")  # 隐藏密码

        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(column=0, row=2, sticky=E)

        self.username.grid(row=1, column=1, pady=(10, 6))
        self.password.grid(row=2, column=1, pady=(0, 6))

        self.buttonframe = Frame(self)
        self.buttonframe.grid(row=3, column=0, columnspan=2, pady=(4, 6))

        self.logbtn = Button(self.buttonframe,
                             text="立即登录",
                             command=self.do_login)
        self.logbtn.grid(row=3, column=0)

        self.registerbtn = Button(self.buttonframe,
                                  text="注册账号",
                                  command=self.do_register)
        self.registerbtn.grid(row=3, column=1)

        self.pack()
        self.master.title("QQ Py版-匠心之韵·清新聊人")

    def do_login(self):
        username = self.username.get()
        password = self.password.get()
        password = security.loop_encrypt(password)
        if not username:
            messagebox.showerror("输入错误", "QQ账号不能为空")
            return
        if not password:
            messagebox.showerror("输入错误", "QQ密码不能为空")
            return

        res = client_socket.connect_to_server(str(memory.IP), int(memory.PORT))
        if res == "connect_fail":
            messagebox.showerror("登陆失败", "当前网络不可用，请检查您的网络设置。")
        else:
            memory.sc = res

            # 2 packs
            # First one include length infomation,
            # The second one include complete values information.
            uname = username.encode()
            pwd = password.encode()
            serializeMessage = common_handler.pack_message(
                common_handler.MessageType.login, uname, pwd)
            client_socket.send_msg(serializeMessage)
            lg_res = client_socket.recv_msg(memory.sc)

            # Get result from server
            login_result = common_handler.unpack_message(lg_res)
            if login_result[0] == common_handler.MessageType.login_successful:
                memory.Login_window.destroy()
                memory.Login_window = None
                memory.username = username
                memory.current_user[username] = login_result[1].decode()
                contact_form.run(username)
            else:
                memory.sc.close()
                messagebox.showerror("通知", "登陆失败,请您输入正确的账号")

    def do_register(self):
        self.master.withdraw()
        reg = tk.Toplevel()
        register.RegisterForm(reg)


def run():
    root = Tk()
    LoginForm(root)
    root.mainloop()


if __name__ == '__main__':
    run()
