# 客户端代码，环境Mac

# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
import socket
import time
import threading

# 定义初始值

HOST, PORT, SIZE = ['127.0.0.1', 8989, 1024]
e, r, t = [1, 2, 3]
# 创建socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# #  接收欢迎消息:
# print(s.recv(SIZE))
# s.send('begin to send')
# print('sending, please wait for a second ...')
# with open('./image.bmp', 'rb') as f:
#     for data in f:
#         s.send(data)
# print('sended !')
# s.close()
# print('connection closed')
#


# conn, addr = s.accept()
# s.send("#000000011504180808090022046518E990000C2".encode())
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


# 发送包
def send():
    s.send("000000011504180808090022046518E990000C2".encode())


# 按服务器地址和端口号发送包
# def send():
#     for server in server_list:
#         for port in PORT:
#             pkt = IP(src="172.16.20.64", dst=server) / UDP(sport=12345, dport=5555) / data
#             sendp(pkt, inter=1, count=1, return_packets=True)
#

# try:
#     i = 0
#     # 开启线程数目
#     tasks_number = 100
#     print('测试启动')
#     time1 = time.clock()
#     while i < tasks_number:
#         t = threading.Thread(target=send)
#         t.start()
#         i += 1
#     time2 = time.clock()
#     times = time2 - time1
#     print(times)
#     # print(times / tasks_number)
# except Exception as e:
#     print(e)
# #
# print("Connect %s:%d OK" % (HOST, PORT))

# 接收包
# data = s.recv(SIZE)
# print("Received:", data.decode())

# 关闭socket
s.close()
