"""
1、创建数据库连接
2、使用cursor创建游标卡尺对象
3、cursor的执行语句过程
4、关闭数据库

"""

import pymysql

db = pymysql.connect("localhost",'root','1234','mrsoft')

cursor = db.cursor()
cursor.execute("select version()")

data = cursor.fetchone()
print("%s" % data)

db.close()


