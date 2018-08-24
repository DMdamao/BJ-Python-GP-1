
class Card(object):
    def __init__(self, cardId, passwd, money):
        self.cardId = cardId
        self.passwd = passwd
        self.money = money
        self.isLock = False
