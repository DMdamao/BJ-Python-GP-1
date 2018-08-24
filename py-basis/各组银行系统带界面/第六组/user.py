

class User(object):
    def __init__(self, name, idCard, phone):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.userInfoDict = {}

dict1 = {'8060': {'name': '张三', 'phone': '1', 'passwd': '1', 'money': 1.0, 'isLock': False, 'idCard': '1'},
        '4742': {'name': '张涛', 'phone': '1', 'passwd': '1', 'money': 1.0, 'isLock': False, 'idCard': '1'}}

# for value in dict.values():
#     print(value)
# new_cardId = "1234"
# pop = dict1.pop("8060")
# print(pop)
# dict1[new_cardId] = pop
# print(dict1)

