"""
    放满10个水盆的任务，每次可以最多安放3个水盆接水，水盆水满后倒入到水桶中，
    放满9盆水后，系统会自动分配1个水盆接水
    apply_async[func[args]]:使用非阻塞方法调用func()函数(并行执行，阻塞方法必须等待上一个进程退出后才能执行下一个进程)
    apply_async[func[args]]:使用阻塞方法调用func()函数  args为传递给func()函数的参数列表
    close():关闭Pool，使其不再接受新的任务
    terminate():不管任务是否完成，立即终止
    join():主进程阻塞，等待子进程的退出，必须在close或terminage之后使用
"""
from multiprocessing import Pool
import os,time
def task(name):
    print("子进程(%s)执行task %s..."%(os.getpid(),name))
    time.sleep(1)

if __name__ == '__main__':
    print('父进程(%s).'%os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task,args=(i,))
    print("等待子进程结束....")
    p.close()
    p.join()
    print("所有子进程结束.")
