from pygame.locals import *
import pygame
import sys
import time
import random


# 初始化窗口
class Window(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 刷新速度
        self.fpsClock = pygame.time.Clock()
        # 创建pygame显示层
        self.playSurface = pygame.display.set_mode((640, 480))
        # 设置标题
        pygame.display.set_caption('贪吃蛇')

    # 定义结束窗口
    def gameOver(self, color):
        # 设置字体
        gameOverFont = pygame.font.SysFont('Arial', 72)
        # 设置字体属性
        gameOverSurf = gameOverFont.render('Game Over', True, color)
        #
        gameOverRect = gameOverSurf.get_rect()
        # 设置字体位置
        gameOverRect.midtop = (320, 240)
        # 在窗口显示
        self.playSurface.blit(gameOverSurf, gameOverRect)
        # 刷新窗口
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()


# 定义snake类


class Snake(object):
    def __init__(self):
        # 初始化snake出现位置
        self.snakeHead = [100, 100]
        self.snakeBody = [[100, 100], [80, 100], [60, 100]]
        # 移动的方向
        self.direction = 'right'
        self.changeDirection = self.direction

    # 定义键盘事件
    def key_Event(self):
        # 检测键盘事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    self.changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    self.changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    self.changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    self.changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

    # 移动
    def move(self):

        # 判断是否输入了当前移动方向的反方向
        if self.changeDirection == 'right' and not self.direction == 'left':
            self.direction = self.changeDirection
        elif self.changeDirection == 'left' and not self.direction == 'right':
            self.direction = self.changeDirection
        elif self.changeDirection == 'up' and not self.direction == 'down':
            self.direction = self.changeDirection
        elif self.changeDirection == 'down' and not self.direction == 'up':
            self.direction = self.changeDirection

        # 根据方向移动蛇头的坐标
        if self.direction == 'right':
            self.snakeHead[0] += 20
        elif self.direction == 'left':
            self.snakeHead[0] -= 20
        elif self.direction == 'up':
            self.snakeHead[1] -= 20
        elif self.direction == 'down':
            self.snakeHead[1] += 20

    def eat(self, food):
        self.snakeBody.insert(0, list(self.snakeHead))
        # 判断是否吃掉了food
        if self.snakeHead[0] == food.raspberryPosition[0] and self.snakeHead[1] == food.raspberryPosition[1]:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            food.raspberryPosition = [int(x * 20), int(y * 20)]
        else:
            self.snakeBody.pop()


# 定义Food类


class Food(object):
    def __init__(self):
        # 出现位置
        self.raspberryPosition = [300, 300]

    #
    # 拓展
    #
    # 通过判断snakes的长度来调整游戏速度和food数量
    '''
    def add_food(self,obj1,obj2):
        num =len(obj2.snakeBody)
        if num>0 and  num<10:
            obj1.fpsClock.tick(5)
        if num>=10 and num <20:
            obj1.fpsClock.tick(10)
        if  num>=20:
            obj1.fpsClock.tick(13)
    '''


def main():
    # 定义颜色
    redColour = pygame.Color(255, 0, 0)
    blackColour = pygame.Color(0, 0, 0)
    whiteColour = pygame.Color(255, 255, 255)
    greyColour = pygame.Color(150, 150, 150)

    # 定义窗口，snake，food
    user_Interface = Window()
    snake = Snake()
    food = Food()
    # img=pygame.image.load(r'C:\Users\LAB\Desktop\1.jpg')
    while True:

        # 设置窗口背景色
        user_Interface.playSurface.fill(blackColour)
        # 设置snake和food的位置及颜色
        for position in snake.snakeBody:
            pygame.draw.rect(
                user_Interface.playSurface, whiteColour, Rect(
                    position[0], position[1], 20, 20))
            pygame.draw.rect(user_Interface.playSurface, redColour, Rect(
                food.raspberryPosition[0], food.raspberryPosition[1], 20, 20))

        # 键盘事件
        snake.key_Event()
        # 移动snake
        snake.move()
        # 吃食物
        snake.eat(food)

        # 判断是否死亡
        if snake.snakeHead[0] > 620 or snake.snakeHead[0] < 0 or snake.snakeHead[1] > 460 or snake.snakeHead[1] < 0:
            user_Interface.gameOver(greyColour)

        else:
            for snakeBody in snake.snakeBody[1:]:
                if snake.snakeHead[0] == snakeBody[0] and snake.snakeHead[1] == snakeBody[1]:
                    user_Interface.gameOver(greyColour)

        # 刷新界面
        pygame.display.flip()

        # food.add_food(user_Interface, snake)

        user_Interface.fpsClock.tick(5)


if __name__ == '__main__':
    main()
