import pymysql
db = pymysql.connect(host="localhost",port=3306,user='study',password='study', db='study',charset='utf8')

cursor = db.cursor()

sql = """
CREATE TABLE python(
    name varchar(20) NOT NULL,
    match int null,
    science int null,
    PRIMARY KEY (name)
)
"""
cursor.execute(sql)
db.commit()

sql = """
INSERT INTO python(
VALUES('홍길동',20,50)
VALUES('임꺽정',30,40)
)
"""
cursor.execute(sql)
db.commit()

sql = """
DELETE FROM python
WHERE name = '홍길동'
"""
cursor.execute(sql)
db.commit()

sql = """
SELECT *
FROM python
"""
cursor.execute(sql)
rs = cursor.fetchall()
print(rs)

cursor.close()
db.close()
