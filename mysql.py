import mysql.connector
# package mysql.connector
conn=mysql.connector.connect(host='127.0.0.1',database='sudhir',user='root',password='')
cursor=conn.cursor()
cursor.execute('insert into user values (04,"pratap","chilika");')
