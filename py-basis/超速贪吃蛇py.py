#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 超速贪吃蛇
@Time    : 2018/8/13 下午8:47
@Author  : 北冥神君
@File    : 超速贪吃蛇.py
@Software: PyCharm
"""

import time
import random
import threading
import os
from tkinter import *
import tkinter.messagebox as messagebox

# 核心模块


class Core():
    row = 40			# 面板格子行数
    column = 40			# 面板格子列数
    score = 0			# 分数
    interval = 0.08		# 速度

    # 反方向
    negative_Direction = {
        'Up': 'Down',
        'Down': 'Up',
        'Right': 'Left',
        'Left': 'Right'
    }

    # 蛇身
    snake = {
        'direction': 'Right', 	# 目前方向
        'food': (None, None), 	# 食物位置
        'snake': [(30, 20), (30, 21), (30, 22), (30, 23)], 	# 蛇身队列 (尾-头)
        'tail': (30, 19)		# 需要被删除的蛇尾
    }

    # 初始化
    def __init__(self):
        self.food()		# 生成第一颗食物

    # 生成食物
    def food(self):
        food = self.snake['snake'][0]
        while food in self.snake['snake']:  # 避免生成在蛇身上
            food = (
                random.randint(1, self.row - 2),
                random.randint(1, self.column - 2)
            )
        self.snake['food'] = food

    # 依据运动方向生成下一个点坐标
    def nextDot(self, direction):
        dot = None
        lenght = len(self.snake['snake'])
        if direction == 'Up':  # 上
            dot = (
                self.snake['snake'][lenght - 1][0] - 1,
                self.snake['snake'][lenght - 1][1]
            )
        elif direction == 'Left':  # 左
            dot = (
                self.snake['snake'][lenght - 1][0],
                self.snake['snake'][lenght - 1][1] - 1
            )
        elif direction == 'Down':  # 下
            dot = (
                self.snake['snake'][lenght - 1][0] + 1,
                self.snake['snake'][lenght - 1][1]
            )
        elif direction == 'Right':  # 右
            dot = (
                self.snake['snake'][lenght - 1][0],
                self.snake['snake'][lenght - 1][1] + 1
            )

        return dot

    # 检测点的位置是否合法
    def CheckIsValid(self, dot):
        if dot in self.snake['snake']:  # 是否在撞到自身
            return False
        if dot[0] < 0 or dot[0] > self.row - 1 or \
                dot[1] < 0 or dot[1] > self.column - 1:  # 是否撞到墙 (边界)
            return False
        else:
            return True

    # 移动函数
    def move(self, direction):
        operationInfo = {
            'Lose': False, 	# 是否输了
            'win': False 	# 是否赢了
        }

        # 反方向过滤
        if direction == self.negative_Direction[self.snake['direction']]:
            return operationInfo

        nextDot = self.nextDot(direction)
        if self.CheckIsValid(nextDot):
            self.snake['direction'] = direction 	# 更新方向
            self.snake['snake'].append(nextDot)

            # 没有吃到食物则将蛇尾弹出队列
            if nextDot != self.snake['food']:
                self.snake['tail'] = self.snake['snake'].pop(0)
            else:
                self.score += 1
                if self.score >= 500:  # 达到 500 分判赢
                    operationInfo['win'] = True
                self.food()		# 刷新食物位置
        else:
            operationInfo['Lose'] = True  # 输

        return operationInfo


# 图像模块
class Graph():

    # 窗体对象
    panel = Tk()
    panel.title("超速贪吃蛇")		# 标题
    panel.geometry("640x480")			# 窗口大小
    panel.resizable(width=False, height=False)  # 窗体大小不可变

    core = None				# 用于存放核心对象
    graphMatrix = []		# 图像面板矩阵

    dotSize = 10			# 点的宽度 (像素为单位)
    stopThread = False		# 暂停标识符

    # 主画布
    cv = Canvas(
        panel,
        bg='black',
        width=640,
        height=480
    )

    gameWindow = None		# 用于存放游戏界面
    gameCv = None			# 用于存放游戏界面画布

    def __init__(self, core):

        # 初始化
        self.core = core
        self.initGraph()
        self.initGraphMatrix()

        # 显示蛇身
        self.draw()

        # 监听键盘事件
        self.panel.bind('<KeyPress>', self.onKeyboardEvent)

        # 建立运动线程
        self.autoRun = threading.Thread(target=self.Run, args=())
        self.autoRun.setDaemon(True)
        self.autoRun.start()

        # 进入消息循环
        self.panel.mainloop()

    # 界面初始化
    def initGraph(self):
        self.createGameWindow()		# 游戏界面初始化
        self.cv.pack()

    # 图像面板矩阵初始化
    def initGraphMatrix(self):
        for i in range(self.core.row):
            self.graphMatrix.append([])
            for j in range(self.core.column):
                rectangle = self.gameCv.create_rectangle(
                    40 + j * self.dotSize,
                    40 + i * self.dotSize,
                    40 + self.dotSize + j * self.dotSize,
                    40 + self.dotSize + i * self.dotSize,
                    outline='black',  # 间隔颜色
                    fill='purple',  # 紫色蛇身
                    state=HIDDEN
                )
                self.graphMatrix[i].append(rectangle)

    # 创建游戏界面
    def createGameWindow(self):

        # 游戏界面画布
        self.gameCv = Canvas(
            self.panel,
            bg='black',
            width=640,
            height=480
        )

        # 双线主方框
        self.gameCv.create_rectangle(
            36, 36, 44 + 20 * 20, 44 + 20 * 20,
            outline='lightgray',
            fill='white' # 墙体的颜色
        )
        self.gameCv.create_rectangle(
            39, 39, 41 + 20 * 20, 41 + 20 * 20,
            outline='lightgray',
            fill='black'
        )
        self.gameWindow = self.cv.create_window(
            320, 240,
            window=self.gameCv,
            state=NORMAL
        )

        # 记分板
        self.gameCv.create_rectangle(
            500, 40, 600, 90,
            outline='white',
            fill='black'
        )
        self.gameCv.create_text(
            525, 50,
            text='分数:',
            fill='red'
        )
        self.scoreText = self.gameCv.create_text(
            575, 50,
            text=self.core.score,
            fill='white'
        )

    # 将蛇身画到图像面板矩阵
    def draw(self):
        lenght = len(self.core.snake['snake'])
        head = self.core.snake['snake'][lenght - 1]
        tail = self.core.snake['tail']

        # 更新蛇头
        self.gameCv.itemconfig(
            self.graphMatrix[head[0]][head[1]],
            state=NORMAL
        )

        # 删除蛇尾
        self.gameCv.itemconfig(
            self.graphMatrix[tail[0]][tail[1]],
            state=HIDDEN
        )

        # 显示食物
        food = self.core.snake['food']
        self.gameCv.itemconfig(
            self.graphMatrix[food[0]][food[1]],
            state=NORMAL
        )

        # 显示分数
        self.showScore()

    # 显示分数
    def showScore(self):
        self.gameCv.itemconfig(
            self.scoreText,
            text=self.core.score,
            fill='white'
        )

    # 键盘事件处理函数
    def onKeyboardEvent(self, event):

        # 方向控制
        if event.keysym == 'Up' or \
                event.keysym == 'Down' or \
                event.keysym == 'Left' or \
                event.keysym == 'Right':
            operationInfo = self.core.move(event.keysym)
            if operationInfo['win']:
                messagebox.showinfo('Message', '游戏胜利!!!')
                os._exit(0)
            if not operationInfo['Lose']:
                self.draw()
            else:
                messagebox.showinfo('Message', '游戏失败了!')
                os._exit(0)

        # 暂停
        elif event.keysym == 'p' or \
                event.keysym == 'P':
            if not self.stopThread:
                self.stopThread = True
            else:
                self.stopThread = False

    # 自动运动函数
    def Run(self):
        while True:
            if not self.stopThread:
                operationInfo = self.core.move(self.core.snake['direction'])
                if operationInfo['win']:
                    messagebox.showinfo('Message', '游戏胜利!!!')
                    os._exit(0)
                if not operationInfo['Lose']:
                    self.draw()
                else:
                    messagebox.showinfo('Message', '游戏失败了!')
                    os._exit(0)
                time.sleep(self.core.interval)
            else:
                time.sleep(0.001)


Graph(Core())
