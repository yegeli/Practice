"""
    使用multiprocessing模块创建进程
"""
from multiprocessing import Process

def dd(interval):
    print("我是子进程")

def main():
    print("我是父进程")
    p = Process(target=dd,args=(1,))
    p.start()
    print("主进程结束")


if __name__ == '__main__':
    main()

