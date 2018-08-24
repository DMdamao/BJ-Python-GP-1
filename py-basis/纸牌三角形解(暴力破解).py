#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 纸牌三角形解法
@Time    : 2018/8/1 上午10:21
@Author  : 北冥神君
@File    : 纸牌三角形解(暴力破解).py
@Software: PyCharm
"""


# 把三角形的三条边分别拿出来，分别进行排列组合。
sum = 0
for x1 in range(1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                for x5 in range(1, 10):
                    for x6 in range(1, 10):
                        for x7 in range(1, 10):
                            for x8 in range(1, 10):
                                for x9 in range(1, 10):
                                    if(x1 + x2 + x3 + x4 == x4 + x5 + x6 + x7 == x7 + x8 + x9 + x1
                                        and x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x1 != x8 and x1 != x9
                                        and x2 != x3 and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x2 != x8 and x2 != x9
                                        and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7 and x3 != x8 and x3 != x9
                                        and x4 != x5 and x4 != x6 and x4 != x7 and x4 != x8 and x4 != x9
                                        and x5 != x6 and x5 != x7 and x5 != x8 and x5 != x9
                                        and x6 != x7 and x6 != x8 and x6 != x9
                                        and x7 != x8 and x7 != x9
                                        and x8 != x9
                                       ):
                                        sum += 1
                                        print('第%s个三角形为：' % sum, end='\n')
                                        print('', '', '', '', x1)
                                        print('', '', x2, '', '', x9)
                                        print('', x3, '', '', '', '', x8)
                                        print(x4, '', x5, '', x6, '', x7)
print('将一个等边三角形旋转，旋转中心应选在平面内任意一点，旋转角度为120度，固旋转一共有三种旋转对称图形')
print('过等边三角形三边做高，沿着等边三角形的高上放一面镜子，一共有三个符合条件的镜面对称图像')
print('故总三角形一共有3+3=6种是同一种的图形，所以总数／6即可')
print('所有纸牌三角形共有%s' % sum, '去除镜面对称和旋转后一共有：', sum / 6)
