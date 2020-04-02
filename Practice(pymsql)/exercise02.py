"""
练习：创建数据库dict 创建数据库表words(id word mean)
      将单词本中的单词存入到数据表中
"""

import pymysql
import re
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user='root',
                     password='1234',
                     database='dict',
                     charset='utf8')

cur = db.cursor()
sql = "insert into words (word,mean) values(%s,%s);"
f = open('dict.txt')
l=[]
for line in f:
    t = re.findall(r"(\w+)\s+(.*)",line)
    l.append(t[0])

    # [('zesty', 'having or characterized by keen enjoyment')]

try:
    cur.executemany(sql,l)
    db.commit()
except:
    db.rollback()

