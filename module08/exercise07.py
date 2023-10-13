from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""
    delete from accounts
    where status = 'CLOSED' OR status = 'BLOCKED'
""")
mysql_connection.commit()
print(f"{mysql_cursor.rowcount} accounts are removed!")
