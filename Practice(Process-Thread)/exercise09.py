"""
    线程间通信
"""
from threading import Thread
import time

def plus():
    print("--------子进程1开始--------")
    global g_num
    g_num += 50
    print("g_num is %d"% g_num)
    print("--------子进程1结束--------")


def mins():
    time.sleep(1)
    print("--------子进程2开始--------")
    global g_num
    g_num -= 50
    print("g_num is %d"% g_num)
    print("--------子进程2结束--------")

g_num = 100
if __name__ == '__main__':
    print("--------主线程开始--------")
    print("g_num is %d" %g_num)
    t1= Thread(target=plus)
    t2= Thread(target=mins)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("--------主线程结束--------")


