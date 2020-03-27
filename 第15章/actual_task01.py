'''
记录用户登录日志（数据库版本)
'''

import time
import pymysql

def show_info():
    print('''输入提示数字，执行相应操作
0：退出
1：查看登录日志
    ''')

def init_mysql():
    db = pymysql.connect("localhost", "root", "1234", "mrsoft",charset='utf8')
    cursor = db.cursor()
    return cursor,db


def save_data(username,password):
    """
    存入MySQL数据库
    :param username: 用户名
    :param password: 密码
    """
    cursor,db = init_mysql()
    try:
        create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        cursor.execute("insert into login(username,password,create_time) values( % s, % s, % s)" ,(username,password,create_time))
        db.commit()
    except:
        db.rollback()
    db.close()

def get_loginfo():
    cursor, db = init_mysql()
    cursor.execute('select username,create_time from login')
    results = cursor.fetchall()
    db.close()
    return results

if __name__ == "__main__":
    # 输入用户名
    username = input('请输入用户名：')
    # 检测用户名
    while len(username) < 2 :
        print('用户名长度应不少于2位')
        username = input('请输入用户名：')
    # 输入密码
    password = input('请输入密码：')
    # 检测密码
    while len(password) < 6 :
        print('密码长度应不少于6位')
        password = input('请输入密码：')

    print('登录成功')
    save_data(username,password)      # 写入日志
    show_info()                       # 提示信息
    num = int(input('输入操作数字:')) # 输入数字

    # 菜单功能
    while True:
        if num == 0:
            print('退出成功')
            break
        elif num == 1:
            print('查看登录日志')
            results = get_loginfo()
            for result in results:
                print("用户名：{} 登录时间：{}\r".format(result[0],result[1]))
            show_info()
            num = int(input('输入操作数字:'))
        else:
            print('您输入的数字有误')
            show_info()
            num = int(input('输入操作数字:'))