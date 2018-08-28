#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 密码加密模块
@Time    : 2018/8/19 下午9:25
@Author  : 北冥神君
@File    : security.py
@Software: PyCharm
"""


from Crypto.Hash import MD5


def loop_encrypt(pwd, n=10):
    # Salt encrypt and recursion 10 times.
    salt = 'jeremyjone'
    md5_obj = MD5.new()
    md5_obj.update((pwd + salt).encode())
    # print(n, md5_obj.hexdigest())
    if n == 1:
        return md5_obj.hexdigest()
    return loop_encrypt(md5_obj.hexdigest(), n - 1)
