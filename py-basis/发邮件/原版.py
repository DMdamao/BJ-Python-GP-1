#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/10 下午8:09
@Author  : 北冥神君
@File    : 原版.py
@Software: PyCharm
"""


# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

#服务器
SMTPserver = "smtp.163.com"
#发送邮件的地址
sender = "13691511443@163.com"
#授权密码(不等同于登陆密码)
password = "sunck1999"

#发送的内容
message = "sunck is a good man"
#转为邮件文本
msg = MIMEText(message)
#邮件主题
msg["Subject"] = "nice"
#邮件的发送者
msg["From"] = sender


#链接smtp服务器
mailServer = smtplib.SMTP(SMTPserver, 25)
#登陆
mailServer.login(sender, password)
#发送邮件
mailServer.sendmail(sender, ["m15735183437@163.com", "1281499513@qq.com"], msg.as_string())
mailServer.quit()







