# -*- coding:gbk -*-
import csv
from functools import reduce

class Person:
    def __init__(self, name, cards, pwd, score, id, flag):
        self.name = name   #姓名
        self.cards = cards  #卡号
        self.__pwd = pwd      #密码
        self.__score = score  #余额
        self.__id = id        #身份证号
        self.__flag = flag    #锁定状态

    def setPwd(self, pwd):
        self.__pwd = pwd
    def getPwd(self):
        return self.__pwd

    def setScore(self,score):
        self.__score = score
    def getScore(self):
        return self.__score

    def getId(self):
        return self.__id

    def setFlag(self,flag):
        self.__flag = flag
    def getFlag(self):
        return self.__flag


li = []   #对象列表


#将列表转化为字符串
def Turn( li ):
    def add(x, y):
        return x + "," + y
    words = reduce(add, li)    #用reduce进行迭代
    return words.strip()

def loading():     #载入数据
    with open('Bank.csv', 'r', encoding='gbk', errors="ignore") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            li.append(Person(row[0], row[1], row[2], row[3], row[4], row[5]))
    csvfile.close()

def Writing():   #存储数据
    outfile = open('Bank.csv', 'w',encoding='gbk', newline='')
    writer = csv.writer(outfile)
    for i in li:
        li2 = [i.name, i.cards, i.getPwd(), i.getScore(), i.getId(), i.getFlag()]
        writer.writerow(li2)# 将数据写入文件
    outfile.close()

def isPerson(cards, pwd):     #判断卡号和密码是否存在
    for i in li:
        if i.cards == cards and i.getPwd() == pwd:
            return i   #返回对象
    return False

def Lock(me, id, flag):   #锁定操作，flag为0表示解锁，1表示锁定
    if me.getId() == id:
        for i in li:
            if i == me:
                if flag == 1:
                    i.setFlag("锁定")
                elif flag == 0:
                    i.setFlag("未锁定")
                return i
    else:
        return False

def saveScore(me, score, flag):   #存取款
    if me.getFlag() == "锁定":
        return False
    for i in li:
        if i == me:
            if flag == "+":
                i.setScore(str(int(i.getScore()) + int(score)))
            elif flag == "-":
                temp = int(i.getScore()) - int(score)
                if temp < 0:
                    return "负数"
                else:
                    i.setScore(str(temp))
            return i

def changePwd(me, old, new):   #修改密码
    for i in li:
        if i == me:
            if old == i.getPwd():
                i.setPwd(new)
                return i
            else:
                return False

def reInfo(cards):     #返回持卡人信息
    for i in li:
        if i.cards == cards:
            return i.name
    return False

def toScore(me, cards, money):   #转账
    if me.getFlag() == "锁定":
        return False
    for i in li:
        if i == me:
            temp = int(me.getScore()) - int(money)
            if temp < 0:
                return "负数"
            else:
                me.setScore(str(temp))
    for i in li:
        if i.cards == cards:
            i.setScore(str(int(i.getScore()) + int(money)))
            return me
