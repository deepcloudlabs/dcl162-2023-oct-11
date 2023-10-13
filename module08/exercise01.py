from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="world"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("show tables")
for table_name in mysql_cursor:
    print(table_name[0])
