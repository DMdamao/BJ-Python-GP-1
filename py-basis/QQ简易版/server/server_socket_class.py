#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 服务端模块
@Time    : 2018/8/19 下午9:35
@Author  : 北冥神君
@File    : server_socket.py
@Software: PyCharm
"""


from socket import *
from threading import *
import os
import struct

from . import memory, login, chat_msg, manage_friend,\
    manage_group, register, common_handler



class QQ_Server(object):
    def __init__(self,IP,PORT):
        print('服务器正在初始化中...')
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口
        self.socket.bind((IP,int(PORT)))  # 绑定IP地址
        self.socket.listen(50)
        memory.server_socket = self.socket # 保存到memory

    def run(self):
        self.server_handler(self.distribute_handler,self.socket)


    def server_handler(self,distribute_handler,socket):
        '''
        循环监视器，接收数据，简单处理程序和分发 数据到不同的模块进行进一步处理。
        :param distribute_handler: 处理accept()返回的两个对象方法
        :param socket: socket对象
        :return: None
        '''
        print("服务已启动...")
        while True:
            try:
                clienSocket, clientAddr = socket.accept()
                print(clientAddr)
            except KeyboardInterrupt:
                os._exit(0)
            except Exception:
                continue

            th1 = Thread(target=distribute_handler, args=(clienSocket, clientAddr))
            th1.start()

    def distribute_handler(self,clienSocket, clientAddr):
        '''
        accept()等待客户端连接之后此函数负责处理服务请求，分别分发到不同的模块进行处理
        :param clienSocket: accept()返回的两个对象中包含数据的对象
        :param clientAddr: accept()返回的两个对象中包含客户端的信息的对象
        :return: None
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



if __name__ == "__main__":
    pass
