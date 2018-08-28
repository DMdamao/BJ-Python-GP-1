#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 检测是否安装依赖，没有安装则提示安装。
@Time    : 2018/8/20 上午8:29
@Author  : 北冥神君
@File    : install_pymysql_pycrypto.py
@Software: PyCharm
"""
import os


def install_package(package_name):
    # 下载pip fake_useragent 包时  包名是:fake-useragent
    package_name = package_name.replace("_", "-")
    p = os.popen("pip list --format=columns")  # 获取所有包名 直接用 pip list 也可获取
    pip_list = p.read()  # 读取所有内容
    print(pip_list)
    if package_name in pip_list:
        print("已经安装{}".format(package_name))
        return True
    else:
        print("没有安装{}!即将自动安装,请稍后".format(package_name))
        p = os.popen("pip install {}".format(package_name))
        if "Success" in p.read():
            print("安装{}成功!".format(package_name))
            return True if "Success" in p.read() else False

# 调用执行检测 如果没安装 则自动安装


def main():
    install_package('PyMySQL')
    install_package('pycrypto')


if __name__ == '__main__':
    main()
