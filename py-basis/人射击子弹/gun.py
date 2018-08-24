# -*- coding:utf-8 -*-
class Gun(object):
    def __init__(self, box):
        self.box = box
    def shoot(self):
        if self.box.count == 0:
            print("没有子弹了")
        else:
            self.box.count -= 1
            self.box.bullets.pop()
            print("嘭！！！子弹剩余:%d发"%self.box.count)