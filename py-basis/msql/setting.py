#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 配置全局变量模块
@Time    : 2018/8/27 下午6:33
@Author  : 北冥神君
@File    : setting.py
@Software: PyCharm
"""
from enum import Enum


class Stetting(Enum):

    MYSQL_HOST = 'localhost'  # ip

    MYSQL_PORT = 3306  # 端口

    MYSQL_USER = 'root'  # 用户名

    MYSQL_PASSWDRD = ''  # 密码

    MYSQL_DATABASE = 'mydb'  # 数据库

    MYSQL_CHARSET = 'utf8' # 连接编码

if __name__ == '__main__':
    print(Stetting.MYSQL_HOST.value)
