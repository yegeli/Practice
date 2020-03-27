"""
    python 操作数据库的通用流程：
        1、开始
        2、创建connection
        3、获取cursor 游标对象
        4、执行sql语句，处理数据结果
        5、关闭cursor
        6、关闭connection

"""



import pymysql

db = pymysql.connect("localhost", 'root', '1234', 'mrsoft')
cursor = db.cursor()
cursor.execute("drop table if exists books")
sql = """
create table books (
    id int(8) not null auto_increment,
    name varchar(50) not null ,
    category varchar(50) not null ,
    price decimal(10,2) default null ,
    publish_time date default null ,
    primary key(id)
)   engine=MyISAM auto_increment=1 default charset=utf8;

"""
cursor.execute(sql)

db.close()
