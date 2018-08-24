#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 周末作业、终端打印歌词+播放音乐
@Time    : 2018/8/3 下午7:01
@Author  : 北冥神君
@File    : 歌词模拟器.py
@Software: PyCharm
"""
from pygame import mixer  # 多媒体播放模块   需要安装pip3 install pygame
import threading  # 多线程模块 自带模块无需安装
import time  # 时间模块
from color import Color
import random
# 配置音乐路径
PATH = '传奇.mp3'

musicLrc = """[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""


# 转换时间函数
def conversion_time(time='00:00.00'):
    """
    转换时间格式函数
    :param time: 时间字符串
    :return: 总秒数
    """
    time_list = time.split(':')
    minute = float(time_list[0])  # 分钟
    second = float(time_list[1])  # 秒
    seconds = minute * 60 + second  # 换算成秒
    return seconds


# 处理歌词数据函数
def translate_lrc(musicLrc=''):
    """
    处理歌词数据
    :param musicLrc:传入标准的lrc歌词
    :return: 歌词字典 key= time  value = 歌词
    """
    dict_lrc = {}  # 定义歌词字典  key= time  value = 歌词
    musicLrc = musicLrc.splitlines()
    for lrc_line in musicLrc:
        lrc_line.strip()
        lrc_list = lrc_line.split(']')

        # 处理时间和歌词
        for i in range(len(lrc_list) - 2, -1, -1):
            time = lrc_list[i][1:]
            time_key = conversion_time(time)  # 转换成时间key
            lrc = lrc_list[-1]  # 歌词
            dict_lrc[time_key] = lrc

    return dict_lrc

# 播放歌词函数
def play_lyrics(dict_lrc={}):
    """
    终端打印歌词
    :param dict_lrc:歌词字典
    :return: None
    """
    time_list = []  # 存放时间的列表
    # 从字典提取时间
    for key in dict_lrc.keys():
        time_list.append(key)
    # 排序时间列表
    time_list.sort()
    clr = Color()  #设置终端颜色

    clr.print_red_text_with_blue_bg('\n\n'+ 'BJ-Python-GP-1'.center(60))
    # 打印爱心
    clr.print_red_text_with_blue_bg('\n'.join([''.join([('BJPythonGP'[(x - y) % 10] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
        x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in
        range(15, -15, -1)]))
    print('\n'*5)
    # 播放歌词
    for i in range(len(time_list)):
        if i == 0:
            lrc = dict_lrc[time_list[0]]
            lrc_color = random.choice(['clr.print_red_text(lrc.center(54))', 'clr.print_green_text(lrc.center(54))',
                                 'clr.print_blue_text(lrc.center(54))'])
            sleep_time = time_list[0]
            time.sleep(sleep_time)
            eval(lrc_color) # 打印歌词
            print('\n')

        if i > 0:
            lrc = dict_lrc[time_list[i]]
            lrc_color = random.choice(['clr.print_red_text(lrc.center(54))', 'clr.print_green_text(lrc.center(54))',
                                       'clr.print_blue_text(lrc.center(54))'])
            sleep_time_1 = time_list[i - 1]  # 前一个时间
            sleep_time_2 = time_list[i]  # 当前时间
            sleep_time = sleep_time_2 - sleep_time_1  # 睡眠时间
            time.sleep(sleep_time)
            eval(lrc_color)  # 打印歌词  # 打印歌词
            print('\n')
        if i == len(time_list) - 1:
            clr.print_red_text_with_blue_bg('歌词播放结束，感谢你的收听'.center(54))


# 播放音乐函数
def playmusic(PATH):
    mixer.init()
    track = mixer.music.load(PATH)
    mixer.music.play()
    time.sleep(310)  # 从歌词字典查看最大秒数
    mixer.music.stop()

# 主函数
def main(PATH):
    dict_lrc = translate_lrc(musicLrc)
    threading.Thread(target=playmusic, args=[PATH, ]).start()
    threading.Thread(target=play_lyrics, args=[dict_lrc, ]).start()

if __name__ == '__main__':
    main(PATH)
