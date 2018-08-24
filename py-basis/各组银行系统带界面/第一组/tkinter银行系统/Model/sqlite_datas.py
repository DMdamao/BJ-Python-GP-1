# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('bank.db')  #默认创建在当前目录
c = conn.cursor()

#创建用户信息表
c.execute('''CREATE TABLE user
       (id INTEGER PRIMARY  KEY     NOT NULL,
       name           VARCHAR(20)   NOT NULL,
       Idcard         CHAR(18)      NOT NULL,
       tel            CHAR(11)      NOT NULL);''')


#创建银行卡信息表
c.execute('''CREATE TABLE card
       (id INTEGER PRIMARY  KEY     NOT NULL,
       passwd           VARCHAR(20) NOT NULL,
       money            int       NOT NULL,
       status           int      DEFAULT 3);''')


#创建操作日志表
c.execute('''CREATE TABLE loginfo
       (id INTEGER PRIMARY  KEY   NOT NULL,
        cardId           int      NOT NULL,
        type             int      NOT NULL,
        money            int    NOT NULL,
        insert_time      datetime  DEFAULT (datetime('now','localtime')));''')


# #插入测试数据
c.execute("INSERT INTO card (id,passwd,money) \
      VALUES ('100000', 123456,1000)")
conn.commit()


print("执行完成")
conn.close()