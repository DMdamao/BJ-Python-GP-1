from singleton import singletonDeco

@singletonDeco
class ATM(object):
    def __init__(self):
        self.account = "1"
        self.passwd = "1"
        self.money = 1000.00
        self.isActive = True


