# -*- coding:utf-8 -*-
'''
定义ATM机
   属性：钱数、账号、密码、是否可用
   行为：检验卡信息、取款、存款、转账、改密、锁卡、解锁、挂失、销户、开户

'''

class ATM(object):
    #初始化***********************************************************
    def __init__(self):
        self.money = 0
        self.isActive = True


    # 检验登陆信息*****************************************************
    def check_login(self, db, card_id, passwd):
        if card_id != "" and passwd != "":
            c = db.cursor()
            res1 = c.execute("select count() from card where id=%s" % card_id)
            if res1.fetchone()[0] != 1:
                return "卡号不存在"
            else:
                res2 = c.execute("select * from card where id=%s" % card_id)
                res2_info = res2.fetchone()
                if res2_info[3] > 0:  # 判断卡的状态
                    if passwd == res2_info[1]:  # 如果密码正确
                        return "1:" + str(res2_info[0]) + ":" + str(res2_info[1]) + ":" + str(res2_info[2]) + ":" + str(
                            res2_info[3])
                    else:
                        c.execute("update  card set status = status-1 where id=%s" % res2_info[0])
                        db.commit()  # 别忘了这一步
                        return "密码错误，还有%d次输入机会" % (int(res2_info[3]) - 1)
                else:
                    return "卡被锁定"
        else:
            return "请输入内容"


    # 取款/存款********************************************************
    def Withdraw_money(self, db, card_id, money, type1):
        if card_id != "" and money != "":
            c = db.cursor()
            # 取款
            if type1 == 1:
                res1 = c.execute("select money from card where id = %s" % card_id)
                all_money = res1.fetchone()[0]  # 获取查到的钱数
                if all_money >= money:
                    res2 = c.execute("UPDATE card set money = money -%d where id=%s" % (money, card_id))
                    db.commit()
                    if res2.rowcount != 1:  # 返回执行成功的行数
                        return "操作失败"
                else:
                    return "余额不足"
            # 存款
            elif type1 == 2:
                res2 = c.execute("UPDATE card set money = money +%d where id=%s" % (money, card_id))
                db.commit()
                if res2.rowcount != 1:  # 返回执行成功的行数
                    return "操作失败"
            # 把记录插入到日志
            c.execute("insert into loginfo(cardId,type,money) values ('%s','%s','%s')" % (card_id, type1, money))
            db.commit()
            return 1

        return "输入有误"


    # 转账************************************************************
    def Transfer_money(self, db, card_id1, card_id2, money):
        if card_id1 != "" and money != "" and card_id2 != "":
            c = db.cursor()
            # 取款
            res1 = c.execute("select money from card where id = %s" % card_id1)
            all_money = res1.fetchone()[0]  # 获取查到的钱数
            if all_money >= money:
                res2 = c.execute("UPDATE card set money = money -%d where id=%s" % (money, card_id1))
                db.commit()
            else:
                return "余额不足"
            # 存款
            res2 = c.execute("UPDATE card set money = money +%d where id=%s" % (money, card_id2))
            db.commit()
            if res2.rowcount != 1:  # 返回执行成功的行数
                return "转账失败"
            # 把记录插入到日志
            c.execute("insert into loginfo(cardId,type,money) values ('%s',3,'%s')" % (card_id1, money))
            db.commit()
            return 1

        return "输入有误"


    # 改密************************************************************
    def Repasswd(self, db, card_id, new_passwd):
        if new_passwd != "":
            c = db.cursor()
            res1 = c.execute("update card set passwd = %s where id =%s" % (new_passwd, card_id))
            db.commit()
            if res1.rowcount == 1:  # 返回执行成功的行数
                return "修改成功"
            else:
                return "修改失败"
        return "输入有误"


    # 锁卡、挂失*******************************************************
    def Lock_card(self, db, card_id):
        if card_id != "":
            c = db.cursor()
            res1 = c.execute("update card set status = 0 where id =%s" % card_id)
            db.commit()
            if res1.rowcount == 1:  # 返回执行成功的行数
                return "操作成功"
            else:
                return "操作失败"
        return "卡号不能为空"


    # 销户************************************************************
    def delete_card(self, db, card_id):
        if card_id != "":
            c = db.cursor()
            res1 = c.execute("delete from card where id =%s" % card_id)
            db.commit()
            if res1.rowcount == 1:  # 返回执行成功的行数
                return "操作成功"
            else:
                return "操作失败"
        return "卡号不能为空"


    # 开户************************************************************
    def add_user(self, db, username, idcard, tel, passwd):
        if username != "" and idcard != "" and tel != "" and passwd != "":
            c = db.cursor()
            res1 = c.execute("select count() from user where Idcard =%s" % idcard)
            if res1.rowcount != 1:  # 如果数据库中没有用户,就把信息插进去
                c.execute("insert into user (name,Idcard,tel) values('%s','%s','%s')" % (username, idcard, tel))
                db.commit()
            # 注册新卡
            res2 = c.execute("insert into card(passwd,money) values (%s,0)" % passwd)
            db.commit()
            if res2.rowcount == 1:
                res3 = c.execute("select id from card ORDER BY id desc limit 1")
                return res3.fetchone()[0]

        return "信息不能为空"


    # 解锁************************************************************
    def re_clock(self, db, username, idcard, tel, cardid):
        if username != "" and idcard != "" and tel != "" and cardid != "":
            c = db.cursor()
            res = c.execute("select * from user where idcard = %s" % idcard)
            info = res.fetchone()
            if info != None:
                # print(info[1],info[3])
                # print(username,tel)
                if info[1] == username and info[3] == tel:
                    res2 = c.execute("update card set status=3 where id=%s" % cardid)
                    db.commit()
                    if res2.rowcount != 1:
                        return "操作失败"
                    else:
                        return "验证通过，解锁成功"
                else:
                    return "信息不匹配，解锁失败"
            else:
                return "用户不存在"

        return "信息不能为空"
