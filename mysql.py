import mysql.connector
# package mysql.connector
conn=mysql.connector.connect(host='127.0.0.1',database='sudhir',user='root',password='')
#crete cursor with the help of conn obj
cursor=conn.cursor()
cursor.execute('insert into user values (04,"pratap","chilika");')
# insert values by using cursor
