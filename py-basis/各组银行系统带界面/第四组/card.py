class Card():
    def __init__(self,num,passwd,money):
        self.num = num
        self.passwd = passwd
        self.money = money
        self.lock = False
        self.account_list = []

