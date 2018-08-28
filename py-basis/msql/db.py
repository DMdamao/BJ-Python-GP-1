#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 封装mysql的各种骚操作，建库、建表、删库、删表、删库跑路等。支持sql注入。
@Time    : 2018/8/27 下午6:24
@Author  : 北冥神君
@File    : db.py
@Software: PyCharm
"""

import pymysql
from setting import Stetting
from singleton import Singleton  # 单例


@Singleton
class MysqlClient(object):
    def __init__(self, host=Stetting.MYSQL_HOST.value,
                 port=Stetting.MYSQL_PORT.value,
                 user=Stetting.MYSQL_USER.value,
                 password=Stetting.MYSQL_PASSWDRD.value,
                 database=Stetting.MYSQL_DATABASE.value,
                 charset=Stetting.MYSQL_CHARSET.value):
        self.db = pymysql.connect(host=host,port=port,user=user,password=password,db=database,charset= charset)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor) # 获取游标,设置存储信息

    def execure_sql(self, sql):
        '''
        执行任意sql语句
        :param sql: sql语句
        :return:
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def show_databases(self):
        '''
        查看所有数据库
        :return: [dict]
        '''
        self.cursor.execute('show databases;')
        return self.cursor.fetchall()
    def show_use_database(self):
        '''
        查看正在使用的数据库
        :return:
        '''
        self.cursor.execute('select database();')
        return self.cursor.fetchone()

    def use_database(self,db_name):
        '''
        切换数据库
        :param db_name: 数据库名
        :return:
        '''
        self.cursor.execute('USE {0};'.format(db_name))


    def create_database(self,db_name, charset = 'utf8', collation = 'utf8_general_ci'):
        '''
        创建数据库
        :param db_name: 数据名
        :param charset: 编码
        :param collation: 排序规则
        :return:
        '''
        sql = 'create database {0} default charset utf8 collate {1};'.format(charset,collation)
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def drop_database(self, db_name):
        '''
        删除数据库
        :return:
        '''
        sql = 'drop database {0}'.format(db_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def show_tables(self):
        '''
        查看数据库所有表
        :return: [dict]
        '''
        self.cursor.execute('show tables;')
        return self.cursor.fetchall()

    def create_table(self,tb_name,tb_data ='',engine='innodb',AUTO_INCREMENT=0,charset='utf8'):
        '''
        创建表
        :param tb_name: 表名
        :param tb_data: 表数据
        :param engine: 存储引擎 myisam：不支持事物innodb：支持事物，原子性操作
        :param AUTO_INCREMENT: 自动编号初始值
        :param charset: 编码
        :return:
        '''

        sql = '''CREATE TABLE {0} (
              {1}
            ) ENGINE={2} AUTO_INCREMENT={3} DEFAULT CHARSET={4}
        '''.format(tb_name,tb_data,engine,AUTO_INCREMENT,charset)
        self.cursor.execute(sql)
        return self.cursor.fetchone()


    def drop_table(self, tb_name):
        '''
        删除表
        :param tb_name: 表名
        :return:
        '''
        self.cursor.execute('drop table {0}'.format(tb_name))
        return self.cursor.fetchone()

    def insert_table(self,tb_name,values,mode=1,field_name=()):
        '''
        表插入数据
        :param tb_name: 表名
        :param mode: 插入模式 1=全列插入 2=缺省插入 3=全列插入同时插入多条数据 4=缺省插入同时插入多条数据
        :param column_name: (column_name)
        :param values: [(数据1),(数据2),...] 数据=(值,值，..)
        :return:
        '''
        values = str(values)[1:-1] # 切片数据

        if mode==1:
            try:
                sql1 = 'insert into %s values %s;'
                self.cursor.execute(sql1,tb_name,values)
                self.db.commit()
            except:
                self.db.rollback()
        elif mode==2:
            try:
                sql2 = 'insert into %s%s values %s;'
                self.cursor.execute(sql2,tb_name,field_name,values)
                self.db.commit()
            except:
                self.db.rollback()
        elif mode==3:
            try:
                sql3 = 'insert into %s values %s;'
                self.cursor.execute(sql3,tb_name,values)
                self.db.commit()
            except:
                self.db.rollback()
        elif mode == 4:
            try:
                sql4 = 'insert into %s%s values %s;'
                self.cursor.execute(sql4,tb_name,field_name,values)
                self.db.commit()
            except:
                self.db.rollback()
        return self.cursor.fetchone()

    def select_table(self,tb_name,mode=1,field_name=(),condition=''):
        '''
        查询表数据
        :param tb_name: 表名
        :param mode: 查询模式 1=无条件查询且查询全部字段，2=带条件查询且查询全部字段，3=指定条件查询且指定字段
        :param field_name: 字段名，是一个元组
        :param condition:
        :return:
        '''
        field_name = str(field_name)[1:-1] # 换成字符串
        if mode ==1:
            sql1= 'select * from {0};'.format(tb_name)
            self.cursor.execute(sql1)
        elif mode ==2:
            sql2 = 'select * from {0} where {1};'.format(tb_name,condition)
            self.cursor.execute(sql2)
        elif mode ==3:
            sql3 = 'select {0} from {1} where {2};'.format(tb_name,field_name,condition)
            self.cursor.execute(sql3)
        return self.cursor.fetchone()

    def drop_table(self,tb_name):
        '''
        删除表
        :param tb_name: 表名
        :return:
        '''
        sql = 'drop table {0};'.format(tb_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def desc_table(self,tb_name):
        '''
        查看表结构，此方法没啥用。
        :param tb_name:表名
        :return:
        '''
        self.cursor.execute('desc {0}'.format(tb_name))
        return self.cursor.fetchall()

    def show_create_table(self, tb_name):
        '''
        查看建表语句，此方法没啥用
        :param tb_name: 表名
        :return:
        '''
        self.cursor.execute('show create table {0} \G'.format(tb_name))
        return self.cursor.fetchone()
    def rename_table(self, tb_old_name,tb_new_name):
        '''
        重命名表名
        :param tb_old_name: 旧表名
        :param tb_new_name: 新表名
        :return:
        '''
        self.cursor.execute('rename table {0} to {1};'.format(tb_old_name,tb_new_name))
        self.cursor.fetchone()

    def delete_table(self,tb_name,mode=1,condition=''):
        '''
        删除表数据
        :param tb_name: 表名
        :param mode: 删除模式  1=清空全部数据 2=条件清空数据
        :param condition:
        :return:
        '''
        if mode==1:
            try:
                self.cursor.execute('delete from %s;',tb_name)
                self.db.commit()
            except:
                self.db.rollback()
        elif mode==2:
            try:
                sql = 'delete from %s where %s;'
                self.cursor.execute(sql,tb_name,condition)
                self.db.commit()
            except:
                self.db.rollback()
        return self.cursor.fetchone()

    def alter_table(self,tb_name,stb_name=None,fk_name=None,fk_field_name=(),mode=1,field_name=(),default_value=None,type_data='int'):
        '''
        修改表
        :param tb_name: 表名
        :param stb_name: 从表名
        :param fk_name: 外键名
        :param fk_field_name: 外键字段名
        :param mode: 模式 1= 添加字段，2=删除字段，3=修改字段，4=添加主键，5=添加外键，6=删除外键，7=修改默认值，8=删除默认值
        :param field_name:字段名，只允许添加一个
        :param default_value: 默认值 为数字类型
        :param type_data: 数据类型
        :return:
        '''
        field_name = str(field_name)[1:-1]  # 换成字符串
        fk_field_name = str(fk_field_name)[1:-1]  # 换成字符串
        if mode==1:
            sql = 'alter table %s add %s %s;'
            self.cursor.execute(sql,tb_name,field_name,type_data)
        elif mode==2:
            sql = 'alter table %s drop column %s;'
            self.cursor.execute(sql,tb_name,field_name)
        elif mode==3:
            sql = 'alter table %s modify column %s %s'
            self.cursor.execute(sql,tb_name,field_name,type_data)
        elif mode==4:
            sql = 'alter table %s add primary key(%s);'
            self.cursor.execute(sql,tb_name,field_name)
        elif mode==5:
            sql = 'alter table %s add constraint %s foreign key %s(%s) references %s(%s);'
            self.cursor.execute(sql,stb_name,fk_name,stb_name,fk_name,fk_field_name,tb_name,field_name)
        elif mode==6:
            sql = 'alter table %s drop foreign key %s'
            self.cursor.execute(sql,tb_name,fk_name)
        elif mode==7:
            sql = 'alter table %s alter %s set default %s ;'
            self.cursor.execute(sql,tb_name,field_name,default_value)
        elif mode==8:
            sql = 'alter table %s alter %s drop default;'
            self.cursor.execute(sql,tb_name,field_name)

    def update_table(self,tb_name,mode=1,field_name_value={},condition=''):
        '''
        更新表数据
        :param tb_name: 表名
        :param mode: 模式 1= 全部字段名修改 2= 根据条件具体修改某些字段数据
        :param field_name_value: 要修改的列名 格式 key=列名、value=值
        :param condition: 条件 格式 字符串里面填条件 比如 'name=sunck or age=20'
        :return:
        '''
        # 处理field_name_value
        field_name_value = ['{0}={1}'.format(key,value)for key, value in field_name_value.items()]
        field_name_value = str(field_name_value)[1:-1]

        if mode ==1:
            try:
                sql = 'update %s set %s;'
                self.cursor.execute(sql,tb_name,field_name_value)
                self.db.commit()
            except:
                self.db.rollback()
        elif mode ==2:
            try:
                sql = "update %s set %s where %s;"
                self.cursor.execute(sql,tb_name,field_name_value,condition)
                self.db.commit()
            except:
                self.db.rollback()
        return self.cursor.fetchone()




if __name__ == '__main__':
    mysql_clicent =MysqlClient()



