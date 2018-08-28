#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 配置一些全局变量，比如数据库信息。
@Time    : 2018/8/20 上午8:51
@Author  : 北冥神君
@File    : setting.py
@Software: PyCharm
"""

from enum import Enum


class Stetting(Enum):

    # mysql配置
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = 'qq8455682'  # 密码修改这里

    #server 配置
    SORKET_IP = '10.0.122.224'
    SORKET_PORT = '4444'
