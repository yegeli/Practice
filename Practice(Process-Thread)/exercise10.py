"""
    互斥锁：
        mutex = threading.Lock() # 创建锁
        mutex.acquire([blocking]) # 锁定
        mutex.release() # 释放锁
    全局变量是多个线程都共享的数据，为了防止数据混乱，通常使用互斥锁
"""

from threading import Thread,Lock
import time
n = 100

def task():
    global n
    mutex.acquire()  # 锁定
    # temp = n
    time.sleep(0.1)
    n -= 1
    print("购买成功，剩余%d张电影票"%n)
    mutex.release()  # 释放锁

if __name__ == "__main__":
    mutex = Lock()
    t_1 = []
    for i in range(100):
        t = Thread(target=task)
        t_1.append(t)
        t.start()
    for i in t_1:
        i.join()
