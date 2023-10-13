from mysql import connector
"""
isolation levels:
set session transaction isolation level read uncommitted
set session transaction isolation level read committed
set session transaction isolation level repeatable read
set session transaction isolation level serializable
"""

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""
set session transaction isolation level repeatable read
                     """)

