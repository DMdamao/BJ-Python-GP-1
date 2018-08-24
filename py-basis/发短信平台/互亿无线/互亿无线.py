#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 将互亿无线封装成类
@Time    : 2018/8/10 下午6:43
@Author  : 北冥神君
@File    : 互亿无线.py
@Software: PyCharm
"""

# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；


import http.client
from urllib import parse


# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C87336934"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "cd7b71fa7464c7f27b728b67b78e5f30"


class Send(object):
    def __init__(self, account, password):
        '''
        :param account: APIID
        :param password: APIKEY
        '''
        self.account = account
        self.password = password
        self.host = '106.ihuyi.com'
        self.sms_send_uri = '/webservice/sms.php?method=Submit'
        self.headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}

    def send_sms(self, mobile, text):
        """
        发送短信
        :param mobile: 手机号码
        :param text: 内容
        :return: str
        """
        params = parse.urlencode({'account': self.account,
                                  'password': self.password,
                                  'content': text,
                                  'mobile': mobile,
                                  'format': 'json'})
        conn = http.client.HTTPConnection(self.host, port=80, timeout=30)
        conn.request("POST", self.sms_send_uri, params, self.headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

if __name__ == '__main__':
    mobile = "18535812780"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
    sen = Send(account, password)
    result = sen.send_sms(mobile, text)
    print(result)
