"""
    生成日志与读取日志
        模拟生成20个日志对象文件，增加四个线程分别读取这些日志文件，读取结果保存至one.txt文件中
"""

import threading
import time
flist =[]
for i in range(20):
    log = "log" + str(i+1) + ".log"
    file = open(log,'w')
    wrlist = str(time.strftime("%Y.%m.%d" "   %H:%M:%S", time.localtime())) + "     " + (str(i + 1) * 8)
    file.write(wrlist)
    file.close()

def process(inti):
    time.sleep(1)

    for j in range(1,6):
        log = "log" + str(j +5*inti) +".log"
        f = open(log)
        fline =f.read()
        flist.append("\n"+fline)
        f.close()

if __name__ =='__main__':
    print("-------主线程开始------")

    threads = [threading.Thread(target=process(i)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    logadd = "one.txt"
    file1 =open(logadd,'w')
    file1.write("\n".join(flist))
    file1.close()
    print("------主线程结束-----")