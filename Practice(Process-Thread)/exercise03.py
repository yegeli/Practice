"""
    使用Process子类创建进程
"""

from multiprocessing import Process
import time
import os

class SubProcess(Process):
    def __init__(self, interval, name=''):
        super().__init__()
        self.interval = interval
        if name:
            self.name = name

    def run(self):
        print("子进程(%s) 开始执行，父进程为（%s）" % (os.getpid(), os.getpid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print("子进程(%s) 开始执行，执行时间为：'%0.2f'秒" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print("------------父进程开始-----------------")
    print("父进程PID: %s" % os.getpid())
    p1 = SubProcess(interval=1,name='mrsoft')
    p2 = SubProcess(interval=2)
    p1.start()
    p2.start()
    print("p1.is_alive = %s" %p1.is_alive())
    print("p2.is_alive = %s" %p2.is_alive())
    print("p1.name= %s" %p1.name)
    print("p1.pid= %s" %p1.pid)
    print("p2.name= %s" %p2.name)
    print("p2.pid= %s" %p2.pid)
    print("-----------等待子进程结束--------------")
    p1.join()
    p2.join()
    print("-----------父进程执行结束--------------")