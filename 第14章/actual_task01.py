"""
记录用户登录日志:
    创建一个登录界面，每次登录时，将用户的登录日志写入到文件中 ，并且可以在程序中查看用户的登录日志

"""
import time


def info():
    print('''提示菜单：
    0：退出
    1：查看登录日志 ·
    ''')

def write_log(username):
    """
    将用户名，及登录时间写入文件中
    :return:
    """
    with open("log.txt",'a',encoding='utf-8') as f:
        string = "用户名：%s\t登录时间：%s" %(username,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
        f.write(string)

def read_log():
    """
    将用户名，从文件中每行读取出来：
    :return:
    """
    with open('log.txt','r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':
                break  # 跳出循环
            print(line)  # 输出一行内容

if __name__ =='__main__':
    print('''用户登录日志:
   每次登录时，将用户的登录日志写入到文件中 ，并且可以在程序中查看用户的登录日志。
    ''')
    username = input("输入用户名：")
    while len(username) < 2:
        print("用户名长度必须大于2位")
        username = input("请重新输入用户名：")
    password = input("输入密码：")
    while len(password) < 6:
        print("密码长度必须大于6位")
        password = input("请重新输入密码：")
    print("登录成功")
    write_log(username)
    info()
    num = input("输入提示数字，执行相应操作：")
    while True:
        if num == 0:
            print('退出成功')
            break
        elif num == 1:
            print('查看登录日志')
            read_log()
            info()
            num = int(input('输入操作数字:'))
        else:
            print('您输入的数字有误')
            info()
            num = int(input('输入操作数字:'))

