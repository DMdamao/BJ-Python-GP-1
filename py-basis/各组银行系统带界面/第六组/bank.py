from singleton import singletonDeco

@singletonDeco
class Bank(object):
    def __init__(self):
        self.usersDict = {}



