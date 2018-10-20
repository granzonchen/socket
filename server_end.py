# 服务端代码，环境Linux
# !/usr/bin/env python
#  -*- coding: UTF-8 -*-

# 导入库
import socket
import threading
import os
import datetime
import struct
HOST, PORT, SIZE = ['0.0.0.0', 8989, 1024]
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
s.bind((HOST, PORT))
# 监听参数为允许客户端数量
s.listen(1000)

#  检查当前目录下是否有等下要命名的图片,有的话删除之
# def check_file():
#     list = os.listdir('.')
#     for iterm in list:
#         if iterm == 'image.bmp':
#             os.remove(iterm)
#             print("remove")
#         else:
#             pass


# # 接受数据线程
# def tcp_link(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send('Welcome from server!')
#     print('receiving, please wait for a second ...')
#     while True:
#         data = sock.recv(SIZE)
#         if not data:
#             print('reach the end of file')
#             break
#         elif data == 'begin to send':
#             print('create file')
#             # check_file()
#             with open('./image.bmp', 'wb') as f:
#                 pass
#         else:
#             with open('./image.bmp', 'ab') as f:
#                 f.write(data)
#     sock.close()
#     print('receive finished')
#     print('Connection from %s:%s closed.' % addr)
#
#

# print('Waiting for connection...')
# while True:
#     sock, addr = s.accept()
#     # 建立一个线程用来监听收到的数据
#     t = threading.Thread(target=tcp_link, args=(sock, addr))
#     # 线程运行
#     t.start()

# 接收数据
while True:
    conn, addr = s.accept()
    print("Client %s connected" % str(addr))
    # dt = datetime.datetime.now()
    # message = "Current time is " + str(dt)
    # conn.send(message.encode())
    # data = s.recv(SIZE)
    data=conn.recv(SIZE)
    # print("Sent:", message)
    print("Receive:", data.decode())
    conn.close()
