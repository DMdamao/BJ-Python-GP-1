# -*- coding:utf-8 -*-

'''

人：Person
属性：枪
行为：开火    装弹

枪：Gun
属性：弹夹
行为：射击

弹夹：BulletBox
属性：子弹列表  子弹数量
行为：


子弹：Bullet
'''
from person import Person
from gun import Gun
from box import Box
from bullet import Bullet



def main():
    bullets = [Bullet(), Bullet(), Bullet(), Bullet(), Bullet()]
    box = Box(bullets, 5)
    gun = Gun(box)
    per = Person(gun)


    #开枪
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.fire()
    per.changeBox(5)
    per.fire()


if __name__ == "__main__":
    main()


