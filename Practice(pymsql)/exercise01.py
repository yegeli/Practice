"""
pymysql使用流程：
    1. 创建数据库连接 db = pymsql.connect(host = 'localhost',port = 3306,user='root',password='123456',database='yege',charset='utf8')
    2. 创建游标，返回对象（用于执行数据库语句命令） cur=db.cursor()
    3. 执行sql语句   cur.execute(sql,list[])、cur.executemany(sql,[(元组)])
    4. 获取查询结果集：
        cur.fetchone()获取结果集的第一条数据，查到返回一个元组
        cur.fetchmany(n)获取前n条查找到的记录，返回结果为元组嵌套((记录1),(记录2))
        cur.fetchall()获取所有查找到的结果，返回元组

       提交到数据库执行 db.commit()
       回滚，用于commit()出错回复到原来的数据状态  db.rollback()
    5. 关闭游标对象 cur.close()
    6. 关闭连接 db.close()


    练习1:  从终端用input输入一个学生姓名,查看该学生的成绩
"""
import pymysql

db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password='1234',
                     database="yege",
                     charset="utf8")



cur = db.cursor()

l = [
    ("qiaoshang1",22,'w',99),
    ("xiaoming",43,'w',87),
    ("pp",29,'m',69),
]
# 写
# sql = "insert into cls(name,age,sex,score) values (%s,%s,%s,%s);"
# 查
sql = "select * from cls where name like 'qiaoshang%';"
cur.execute(sql)
print(cur.fetchmany(2))
# try:
#     cur.executemany(sql,l)
#     db.commit()
# except:
#     db.rollback()
cur.close()
db.close()
