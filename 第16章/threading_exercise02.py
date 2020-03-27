"""
    使用Thread子类创建进程

"""
import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "子线程" + self.name + "执行，i=" + str(i)
            print(msg)

if __name__ == "__main__":
    print("------主进程开始-------")
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("------主进程结束-------")