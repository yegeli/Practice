from multiprocessing import Process
import time
import os


def child_1(interval):
    print("子进程（%s）开始执行，父进程（%s）" % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.02f'秒" % (os.getpid(), t_end - t_start))


def child_2(interval):
    print("子进程（%s）开始执行，父进程（%s）" % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.02f'秒" % (os.getpid(), t_end - t_start))

def child_3(interval):
    print("子进程（%s）开始执行，父进程（%s）" % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程（%s）执行时间为'%0.02f'秒" % (os.getpid(), t_end - t_start))

if __name__ == "__main__":
    print("------父进程开始执行---------")
    print("父进程PID: %s" % os.getpid())
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name='mrsoft', args=(2,))
    p3 = Process(target=child_2, args=(3,))
    p1.start()
    p2.start()
    p3.start()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p3.is_alive=%s" % p3.is_alive())
    print("p1.p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("p3.pid=%s" % p3.pid)
    print("p3.name=%s" % p3.name)

    print("--------等待子进程-----------")
    p1.join()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p3.is_alive=%s" % p3.is_alive())
    p2.join()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p3.is_alive=%s" % p3.is_alive())
    p3.join()
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    print("p3.is_alive=%s" % p3.is_alive())

    print("--------父进程执行结束-----------")
