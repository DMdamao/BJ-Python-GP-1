#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 服务器全局变量配置
@Time    : 2018/8/19 下午9:35
@Author  : 北冥神君
@File    : memory.py
@Software: PyCharm
"""

from .DB_Handler import DB_Handler


# {connect: (username, IP, PORT)}
online_user = {}

server_socket = None

server_socket_listener = None

db = DB_Handler()

window = None
