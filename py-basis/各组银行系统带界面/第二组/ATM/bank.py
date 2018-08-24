#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
"""
银行
类名：Bank
属性：用户列表     提款机
"""


class Bank(object):
    bank_name = "神马银行"

    def __init__(self):
        pass

    @classmethod
    def register(cls, file_name, **kwargs):
        print(kwargs, type(kwargs))
        if file_name == "card_data.txt":
            fil = open(file_name, "a", encoding="utf-8")
            if fil.tell() == 0:
                fil.write("%d %s %d %s" % (kwargs["card_number"], kwargs["card_id"],
                                           kwargs["balance"], kwargs["state"]))
            else:
                fil.write("\n%d %s %d %s" % (kwargs["card_number"], kwargs["card_id"],
                                             kwargs["balance"], kwargs["state"]))
            fil.close()
        elif file_name == "user_data.txt":
            fil = open(file_name, "a", encoding="utf-8")
            if fil.tell() == 0:
                fil.write("%s %s %s %d %d %s" % (kwargs["record_file_id"], kwargs["name"],
                                                 kwargs["id_number"], kwargs["phone_number"],
                                                 kwargs["card_number"], kwargs["address"]))
            else:
                fil.write("\n%s %s %s %d %d %s" % (kwargs["record_file_id"], kwargs["name"],
                                                   kwargs["id_number"], kwargs["phone_number"],
                                                   kwargs["card_number"], kwargs["address"]))
            fil.close()
        else:
            print("?")

    @staticmethod
    def update_data(data_name: str, data: dict):
        # data时一个人的数据字典  {"id_number": "", "name": "", "record_file_id": "", "phone_number": 0,
        # "card_number": [],"address": "", "settings": {"bg_color": "", "font_color": ""}
        # 数据库格式：{"id_number": {"name": "", "record_file_id": "", "phone_number": 0, "card_number": [],
        #  "address": "", "settings": {"bg_color": "", "font_color": ""}}, "id_number": {}}
        if data_name == "user":
            with open("users_data.txt", "wb+") as file:
                # old_data = pickle.load(file)
                old_data = {"150203199701122419": {}}
                id_number = data["id_number"]
                if id_number in old_data.keys():
                    old_data[id_number]["name"] = data["name"]
                    old_data[id_number]["record_file_id"] = data["record_file_id"]
                    old_data[id_number]["phone_number"] = data["phone_number"]
                    old_data[id_number]["card_number"] = data["card_number"]
                    old_data[id_number]["address"] = data["address"]
                    old_data[id_number]["settings"] = data["settings"]
                    pickle.dump(old_data, file)
                else:
                    old_data[id_number] = dict
                    old_data[id_number]["name"] = data["name"]
                    old_data[id_number]["record_file_id"] = data["record_file_id"]
                    old_data[id_number]["phone_number"] = data["phone_number"]
                    old_data[id_number]["card_number"] = data["card_number"]
                    old_data[id_number]["address"] = data["address"]
                    old_data[id_number]["settings"] = data["settings"]
                    pickle.dump(old_data, file)
                pass
        elif data_name == "card":
            with open("cards_data.txt", "wb+") as file:
                pass
            pass
        elif data_name == "atm":
            with open("atms_data.txt", "wb+") as file:
                pass
            pass
        pass

    @staticmethod
    def find_data(data_name: str, flag: str):
        if data_name == "user":
            with open("users_data.txt", "rb") as file:
                users = pickle.load(file)
                if flag in users.keys():
                    user = dict()
                    user["id_number"] = flag
                    user["name"] = users[flag]["name"]
                    user["record_file_id"] = users[flag]["record_file_id"]
                    user["phone_number"] = users[flag]["phone_number"]
                    user["card_number"] = users[flag]["card_number"]
                    user["address"] = users[flag]["address"]
                    user["settings"] = users[flag]["settings"]
                    return user
                else:
                    return None
                pass
            pass
        elif data_name == "card":
            pass
        elif data_name == "atm":
            pass

    @classmethod
    def update_card_data(cls, card_number, dict):
        f = open("card_data.txt", "r+")
        lines = f.readlines()
        for index, line in enumerate(lines):
            i = line.split(" ")
            if eval(i[0]) == card_number:
                i[0] = str(dict["card_number"])
                i[1] = dict["card_id"]
                i[2] = str(dict["balance"])
                i[3] = dict["state"]
                if index == (len(lines) - 1):
                    lines[index] = " ".join(i)
                else:
                    lines[index] = " ".join(i) + "\n"
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()
        pass

    @classmethod
    def get_empty_card_number(cls):
        tmp = 10000000
        while cls.find_card(tmp) is not None:
            tmp += 1
        return tmp
        pass

    @classmethod
    def find_card(cls, card_number):
        di = {}
        with open("card_data.txt", "r", encoding="utf-8") as fil:
            data = fil.read()
            data = data.split("\n")
            for index, item in enumerate(data):
                i = item.split(" ")
                if i[0] == str(card_number):
                    di["card_number"] = eval(i[0])
                    di["card_id"] = i[1]
                    di["balance"] = eval(i[2])
                    di["state"] = i[3]
                    return di, index
    @classmethod
    def find_user(cls, record_file_id: str=None, name: str=None, id_number: str=None,
                  phone_number: int=None, card_number: int=None, address: str=None):
        di = {}
        with open("user_data.txt", "r", encoding="utf-8") as fil:
            data = fil.read()
            data = data.split("\n")
            for index, item in enumerate(data):
                i = item.split(" ")
                if card_number is not None:
                    if i[4] == str(card_number):
                        di["record_file_id"] = i[0]
                        di["name"] = i[1]
                        di["id_number"] = i[2]
                        di["phone_number"] = eval(i[3])
                        di["card_number"] = eval(i[4])
                        di["address"] = i[5]
                        return di, index
                elif id_number is not None:
                    if i[2] == id_number:
                        di["record_file_id"] = i[0]
                        di["name"] = i[1]
                        di["id_number"] = i[2]
                        di["phone_number"] = eval(i[3])
                        di["card_number"] = eval(i[4])
                        di["address"] = i[5]
                        return di, index
                else:
                    return None


# 10000000 20595a895a68519c6516b19ff36021093a757192 100 normal
if __name__ == '__main__':
    bank = Bank()
    # print(bank.read_file("card_data.txt"))
    # bank.register("card_data.txt", card_number="1000000", card_id="aaaaaaaaaaa", balance=100, state="normal")
    # bank.register("user_data.txt",
    #               record_file_id="1234",
    #               name="吕兴东",
    #               id_number="150203199701122419",
    #               phone_number=12512581258,
    #               card_number=10000000,
    #               address="北京")
    # print(bank.find_user(id_number="150203199701122419"))
    # print(bank.find_user(card_number=10000000))
    # print(bank.find_card(10000000))
    # bank.update_card_data(10000001,
    #                       {"card_number": 10000001,
    #                        "card_id": "0baf990eb39626173e6f5b20de7e1fe5958ec777",
    #                        "balance": 10,
    #                        "state": "normal"})
    # print(bank.find_card(10000000))
    # user = {"id_number": "150203199701122419",
    #         "name": "吕兴东",
    #         "record_file_id": "007",
    #         "phone_number": 18738981757,
    #         "card_number": [10000000],
    #         "address": "北京",
    #         "settings": {"bg_color": "#696969", "font_color": "#DEB887"}}
    # bank.update_data("user", user)
    print(bank.find_data("user", "150203199701122419"))
