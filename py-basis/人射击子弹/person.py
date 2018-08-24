# -*- coding:utf-8 -*-

from bullet import Bullet

class Person(object):
    def __init__(self, gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()

    def changeBox(self, count):
        for i in range(count):
            self.gun.box.bullets.append(Bullet())
        self.gun.box.count = count
        print("换弹")