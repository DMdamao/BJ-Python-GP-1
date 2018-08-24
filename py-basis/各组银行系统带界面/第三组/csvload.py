# -*- coding:gbk -*-
import csv
from functools import reduce

class Person:
    def __init__(self, name, cards, pwd, score, id, flag):
        self.name = name   #����
        self.cards = cards  #����
        self.__pwd = pwd      #����
        self.__score = score  #���
        self.__id = id        #���֤��
        self.__flag = flag    #����״̬

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


li = []   #�����б�


#���б�ת��Ϊ�ַ���
def Turn( li ):
    def add(x, y):
        return x + "," + y
    words = reduce(add, li)    #��reduce���е���
    return words.strip()

def loading():     #��������
    with open('Bank.csv', 'r', encoding='gbk', errors="ignore") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            li.append(Person(row[0], row[1], row[2], row[3], row[4], row[5]))
    csvfile.close()

def Writing():   #�洢����
    outfile = open('Bank.csv', 'w',encoding='gbk', newline='')
    writer = csv.writer(outfile)
    for i in li:
        li2 = [i.name, i.cards, i.getPwd(), i.getScore(), i.getId(), i.getFlag()]
        writer.writerow(li2)# ������д���ļ�
    outfile.close()

def isPerson(cards, pwd):     #�жϿ��ź������Ƿ����
    for i in li:
        if i.cards == cards and i.getPwd() == pwd:
            return i   #���ض���
    return False

def Lock(me, id, flag):   #����������flagΪ0��ʾ������1��ʾ����
    if me.getId() == id:
        for i in li:
            if i == me:
                if flag == 1:
                    i.setFlag("����")
                elif flag == 0:
                    i.setFlag("δ����")
                return i
    else:
        return False

def saveScore(me, score, flag):   #��ȡ��
    if me.getFlag() == "����":
        return False
    for i in li:
        if i == me:
            if flag == "+":
                i.setScore(str(int(i.getScore()) + int(score)))
            elif flag == "-":
                temp = int(i.getScore()) - int(score)
                if temp < 0:
                    return "����"
                else:
                    i.setScore(str(temp))
            return i

def changePwd(me, old, new):   #�޸�����
    for i in li:
        if i == me:
            if old == i.getPwd():
                i.setPwd(new)
                return i
            else:
                return False

def reInfo(cards):     #���سֿ�����Ϣ
    for i in li:
        if i.cards == cards:
            return i.name
    return False

def toScore(me, cards, money):   #ת��
    if me.getFlag() == "����":
        return False
    for i in li:
        if i == me:
            temp = int(me.getScore()) - int(money)
            if temp < 0:
                return "����"
            else:
                me.setScore(str(temp))
    for i in li:
        if i.cards == cards:
            i.setScore(str(int(i.getScore()) + int(money)))
            return me
