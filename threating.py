# -*- coding: utf-8 -*-
import requests
import threading
import time


class PostRequests:
    def __init__(self):
        self.url = 'http://www.baidu.com'
        # self.files = {'unknown_image': open('成长天地问题.png', 'rb')}
        self.files = {"hello"}

    def get(self):
        try:
            r = requests.get(self.url)
            # print(r.text)
        except Exception as e:
            print(e)

    def post(self):
        try:
            # r = requests.post(self.url, files=self.files)
            r = requests.post(self.url, "hello")
            # print(r.text)
        except Exception as e:
            print(e)


def login():
    login = PostRequests()
    return login.get()


# if __name__ == '__main__':
#     login()


try:
    i = 0
    # 开启线程数目
    tasks_number = 1000
    print('测试启动')
    time1 = time.clock()
    while i < tasks_number:
        t = threading.Thread(target=login)
        t.start()
        i += 1
    time2 = time.clock()
    times = time2 - time1
    print(times)
    print(times / tasks_number)
except Exception as e:
    print(e)
