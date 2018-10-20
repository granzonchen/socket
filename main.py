# -*-coding:utf-8-*-
from scapy import *
from scapy.layers.inet import *
from urllib import request, parse
from urllib.error import URLError
import zlib, socket, sys, struct, threading, time

# 服务器列表
server_list = ["172.16.20.60", "172.16.20.61", "172.16.20.62", "172.16.20.63", "172.16.20.64"]
PORT = ['80', '443', '880', '8080', '5555']
# PORT =80

# 数据包
# send_bag = {}
data = struct.pack("=BHI", 0x12, 20, 1000)
# data_01 = struct.pack('=#000000011504180808090022046518E990000C2', 0x12, 20, 1000)


# 发送包
# def send():
#     for server in server_list:
#         for port in PORT:
#             pkt = IP(src="172.16.20.64", dst=server) / UDP(sport=12345, dport=5555) / data
#             sendp(pkt, inter=1, count=1, return_packets=True)
#
#
# try:
#     i = 0
#     # 开启线程数目
#     tasks_number = 10
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

# 接收包
# receive = sniff(filter="udp and host 172.16.20.64")
# print(receive)

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_list[4], 8888))
s.send(data)
print(s)

with open('test.log', 'wb') as f:
    f.write(s)

# threading
#
# cliList = []
# # 创建socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 绑定地址和端口号
# s.bind(('0.0.0.0', 7786))
# # 开始监听
# s.listen(1000)
# while True:
#     # 接受一个新的连接:
#     sock, addr = s.accept()
#     # 将sock添加到列表中
#     cliList.append(sock)
