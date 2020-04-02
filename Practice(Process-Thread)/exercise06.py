"""
    使用队列在进程间通信
"""

from multiprocessing import Process
from multiprocessing import Queue
import time


def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入：%s" % message)


def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取：%s" % q.get_nowait())


if __name__ == "__main__":
    print("父进程开始")
    q = Queue()
    p1 = Process(target=write_task, args=(q,))
    p2 = Process(target=read_task, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("父进程结束")
