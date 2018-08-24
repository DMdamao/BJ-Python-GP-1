# -*- coding:utf-8 -*-
import sqlite3

from Views.view_win1 import MyApp

'''
第一次运行先执行以下 Model/sqlite_datas.py文件
'''


if __name__ == '__main__':

    db = sqlite3.connect('Model/bank.db')  # 连接到sqlite3

    app = MyApp(db)  # 实例化主窗口对象

    app.mainloop()

    db.close()  # 关闭连接
