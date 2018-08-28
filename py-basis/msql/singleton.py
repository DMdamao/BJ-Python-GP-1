#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 单例
@Time    : 2018/8/27 下午6:24
@Author  : 北冥神君
@File    : singleton.py
@Software: PyCharm
"""
# 实际项目中，可能会在多个不同的方法中使用MySQL链接，如果每次都新建、关闭连接，
# 当访问量高时可能会造服务器崩溃无法访问等问题，而单例模式可以很好的解决这个问题。

def Singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance