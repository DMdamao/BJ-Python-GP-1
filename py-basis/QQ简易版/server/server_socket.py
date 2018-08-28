#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 填写本模块功能大致描述
@Time    : 2018/8/22 下午7:22
@Author  : 北冥神君
@File    : server_socket_function.py
@Software: PyCharm
"""



from socket import *
from threading import *
import os
import struct

from . import memory, login, chat_msg, manage_friend,\
    manage_group, register, common_handler


def server(IP, PORT):
    '''
    创建socket TCP
    :param IP: 本机ip
    :param PORT: 端口
    :return: server socket对象
    '''
    sk = socket(AF_INET, SOCK_STREAM)
    sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口
    sk.bind((IP, int(PORT)))
    sk.listen(50)
    memory.server_socket = sk # 保存到memory
    return sk


def distribute_handler(clienSocket, clientAddr):
    '''
    accept()等待客户端连接之后此函数负责处理服务请求，分别分发到不同的模块进行处理
    :param clienSocket:
    :param clientAddr:
    :return:
    '''

    while True:
        try:
            data = clienSocket.recv(4096)
            msg = common_handler.unpack_message(data)
            # Recv large file
            if msg[0] == common_handler.MessageType.large_file:
                msg_buffer += msg[1]
                if msg[2] == 0:
                    msg = msg_buffer
                    msg_buffer = None
                else:
                    continue

            if msg[0] == common_handler.MessageType.register:
                # Register
                print("接收到注册请求")
                register.register_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.login:
                # Login
                print("接收到登录请求")
                login.login_handler(clienSocket, clientAddr, msg)

            elif msg[0] == common_handler.MessageType.clientAddrd_friend:
                # clientAddrd friend
                print("接收到添加好友请求")
                manage_friend.clientAddrd_friend_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.confirm_friend_request:
                # confirm clientAddrd friend
                print("接收到确认添加好友请求")
                manage_friend.confirm_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.delete_friend:
                # delete friend
                print("接收到删除好友请求")
                manage_friend.del_friend_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.query_friend:
                # Get friend infomation
                print("接收到获取好友列表请求")
                manage_friend.get_friend_handler(clienSocket)

            elif msg[0] == common_handler.MessageType.send_message:
                # Chat message
                print("接收到发送消息请求")
                chat_msg.userchat_handler(msg)

            elif msg[0] == common_handler.MessageType.chatroom_message:
                # Chatroom message
                print("接收到聊天室信息请求")
                chat_msg.chatroom_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.broclientAddrcast:
                # BroclientAddrcast message
                print("接收到广播请求")
                chat_msg.broclientAddrcast_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.create_room:
                # Create chatroom
                print("接收到创建群聊请求")
                manage_group.chatroom_handler(clienSocket, msg)

            elif msg[0] == common_handler.MessageType.join_room:
                # User join/leave chatroom
                print("接收到加入/退出群聊请求")
                manage_group.user_join_leave_handler(clienSocket, msg, "join")

            elif msg[0] == common_handler.MessageType.leave_room:
                # User join/leave chatroom
                print("接收到加入/退出群聊请求")
                manage_group.user_join_leave_handler(clienSocket, msg, "leave")

            elif msg[0] == common_handler.MessageType.logout:
                # User logout
                print("接收到用户登出信号")
                login.logout_handler(clienSocket)

            elif msg[0] == common_handler.MessageType.query_room_users:
                print("收到用户请求刷新聊天室列表")
                manage_group.query_chatroom_user(clienSocket, msg)

        except struct.error:
            pass
        except ConnectionResetError as e:
            print(e)
            del memory.online_user[clienSocket]
            memory.window.clientAddrd_user_list()
        except OSError as e:
            pass
        # except Exception as e:
        #     print("服务器接收信息时遇到一个未知问题 >>", e)


def server_handler(sk):
    '''
    Loop monitor, receive data, simple handler and distribute
    data to different modules for further processing.
    '''
    print("Server is running...")
    while True:
        try:
            clienSocket, clientAddr = sk.accept()
            print(clientAddr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception:
            continue

        th1 = Thread(target=distribute_handler, args=(clienSocket, clientAddr))
        th1.start()


def run(IP, PORT):
    sk = server(IP, PORT)
    server_handler(sk)


if __name__ == '__main__':
    run()