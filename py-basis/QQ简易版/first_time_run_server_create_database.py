#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 创建数据库，检测库是安装。
@Time    : 2018/8/19 下午9:51
@Author  : 北冥神君
@File    : first_time_run_server_create_database.py
@Software: PyCharm
"""

import pymysql
from Crypto.Hash import MD5
from server.setting import Stetting


def loop_encrypt(pwd, n=10):
    # Salt encrypt and recursion 10 times.
    salt = 'jeremyjone'
    md5_obj = MD5.new()
    md5_obj.update((pwd + salt).encode())
    # print(n, md5_obj.hexdigest())
    if n == 1:
        return md5_obj.hexdigest()
    return loop_encrypt(md5_obj.hexdigest(), n - 1)


class DB_Handler(object):
    def __init__(self):
        self.local = Stetting.MYSQL_HOST.value
        self.db_login_name = Stetting.MYSQL_USERNAME.value
        self.db_login_pswd = Stetting.MYSQL_PASSWORD.value
        self.userinfo = "userinfo"
        self.chatmsg = "chatmsg"
        self.userfriend = "userfriend"
        self.chatroom = "chatroom"
        self.chatroomuser = "chatroom_user"

    def connect_to_DB(self, sql_statment, db=None):
        '''
        Connect to database by base infomation and create database
        handler module, it can receive one SQL and execute.

        If operate successfully return OK, conversely return NG.
        '''
        self.db = db
        _ = None
        sql = pymysql.connect(self.local,
                              self.db_login_name,
                              self.db_login_pswd,
                              charset='utf8')

        # Create cursor
        cursor = sql.cursor()

        if self.db is not None:
            cursor.execute("use %s" % self.db)

        try:
            cursor.execute(sql_statment)
            sql.commit()
            _ = 'OK'
        except Exception as e:
            sql.rollback()
            print(e)
            _ = "NG"
        # close cursor
        cursor.close()
        # close database
        sql.close()
        return _

    def do_create(self):
        cdsql = 'create database chatroom;'

        ctsql1 = '''create table userinfo(
                    id int primary key auto_increment,
                    username varchar(50) unique not null,
                    password varchar(254) not null,
                    nickname varchar(50) not null,
                    reg_time timestamp not null,
                    isActive boolean not null)default charset=utf8;
                 '''

        ctsql2 = '''create table chatmsg(
                    id int primary key auto_increment,
                    user_id int not null,
                    send_time timestamp not null,
                    target_id int not null,
                    isRead boolean not null,
                    msg_type tinyint not null,
                    msg varchar(4096) not null,
                    isActive boolean not null)default charset=utf8;
                 '''

        ctsql3 = '''create table userfriend(
                    id int primary key auto_increment,
                    user_id int not null,
                    friend_id int not null,
                    add_time timestamp not null,
                    isActive boolean not null)default charset=utf8;
                 '''

        ctsql4 = '''create table chatroom(
                    id int primary key auto_increment,
                    chatroom_name varchar(30) unique not null,
                    create_time timestamp not null,
                    isActive boolean not null)default charset=utf8;
                 '''

        ctsql5 = '''create table chatroom_user(
                    id int primary key auto_increment,
                    chatroom_id int not null,
                    user_id int not null,
                    create_time timestamp not null,
                    isActive boolean not null)default charset=utf8;
                 '''

        self.connect_to_DB(cdsql)
        self.connect_to_DB(ctsql1, db="chatroom")
        self.connect_to_DB(ctsql2, db="chatroom")
        self.connect_to_DB(ctsql3, db="chatroom")
        self.connect_to_DB(ctsql4, db="chatroom")
        self.connect_to_DB(ctsql5, db="chatroom")

    def do_delete(self):
        deldatabase = 'drop database chatroom;'
        self.connect_to_DB(deldatabase)

    def do_insertdata(self):
        username = ["admin", "xiaomi", "robbin", "pony", "jackma"]
        password = [
            loop_encrypt("123"),
            loop_encrypt("123"),
            loop_encrypt("123"),
            loop_encrypt("123"),
            loop_encrypt("123")]
        nickname = ["马化腾", "雷军", "李彦宏", "马化腾", "马云"]
        for i in range(5):
            userinfo = "insert into userinfo (username, password, nickname, isActive) values ('%s', '%s', '%s', %d);" % (
                username[i], password[i], nickname[i], 1)
            self.connect_to_DB(userinfo, db="chatroom")


if sys.argv[1] == "1":
    DB_Handler().do_create()
elif sys.argv[1] == "2":
    DB_Handler().do_insertdata()
elif sys.argv[1] == "3":
    DB_Handler().do_delete()

