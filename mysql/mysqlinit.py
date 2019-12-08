import mysql.connector

conn = mysql.connector.connect (user='sword', password='password',
                               host='localhost',buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
for (databases) in cursor:
     print (databases)
