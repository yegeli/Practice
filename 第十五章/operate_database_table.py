import pymysql
db = pymysql.connect("localhost",'root','1234','mrsoft',charset='utf8')
cursor = db.cursor()

data = [("零基础学Python","Python",'79.80','2018-5-20'),
        ("Python从入门到精通","Python",'69.80','2018-6-18'),
        ("零基础学C语言","C语言",'68.67','2017-5-21'),
        ("PHP项目实战","PHP",'79.87','2016-5-11'),
        ("零基础学JAVA","JAVA",'56.55','2017-3-19'),
        ]

try:
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)",data)
    db.commit()

except:

    db.rollback()

db.close()