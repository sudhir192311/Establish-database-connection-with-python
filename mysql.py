import mysql.connector
# package mysql.connector
conn=mysql.connector.connect(host='127.0.0.1',database='sudhir',user='root',password='')
#crete cursor with the help of conn obj
cursor=conn.cursor()
cursor.execute('insert into user values (04,"pratap","chilika");')
# insert values by using cursor
cursor.execute("select * from user")
for i in cursor:
  print(i)
# print all data in user table  
#and fetcth all data 
result=cursor.fetchall()
or result=cursor.fetchone()
for i in result:
  print(i)
insert="insert into user(snno,username,address) values(%d,%s,%s)"
user=[(5,"rakesh","jajpur"),(6,"sambid","sambalpur"),(7,"ctc","bhg"),]
cursor.executemany(insert,user)
conn.commit()  
  
