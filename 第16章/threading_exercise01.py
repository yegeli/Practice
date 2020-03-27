"""
threading模块创建线程

"""

import threading, time


def process():
    for i in range(4):
        time.sleep(1)
        print("Thread name is %s" % threading.current_thread().name)



if __name__ == '__main__':
    print("-----主线程开始------")
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        t.start()
    for i in threads:
        i.join()
    print("------主线程结束-----")
