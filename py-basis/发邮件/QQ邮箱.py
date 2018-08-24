#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/10 下午9:08
@Author  : 北冥神君
@File    : QQ邮箱.py
@Software: PyCharm
"""

from email.mime.text import MIMEText
import smtplib

class Mail_QQ(object):
    def __init__(self, sender, password):
        '''
        初始化配置信息
        :param sender: 发送者邮箱
        :param password:  邮箱授权密码
        '''
        self.SMTP_server = "smtp.qq.com"
        self.sender = sender
        self.password = password

    def login(self):
        MIAL_server = smtplib.SMTP(self.SMTP_server, 25)      # 链接smtp服务器
        MIAL_server.login(self.sender, self.password)  # 登陆
        return MIAL_server

    def send(self, his_emiall,title, message_text):
        try:
            MIAL_server = self.login()
            msg = MIMEText(message_text)     # 转为邮件文本
            msg["From"] = self.sender   # 邮件的发送者
            msg["Subject"] = title      # 邮件主题
            MIAL_server.sendmail(self.sender, his_emiall, msg.as_string()) # 发送邮件
            MIAL_server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException:
            print('邮件发送失败')

sender = "binyoucaixiaobin@qq.com"
#授权密码(不等同于登陆密码)
password = "bwbbeimlzrgqbhga"
def main():
    mail_163 = Mail_QQ(sender,password)
    mail_163.send(his_emiall = ['binyoucaixiaobin@qq.com'],title='欢迎你来到天丰利', message_text= 'hi! hello world!')

if __name__ == '__main__':
    main()