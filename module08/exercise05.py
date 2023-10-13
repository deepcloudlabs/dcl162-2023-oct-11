from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""
    update accounts
    set balance = balance - 150
    where status = 'ACTIVE'
""")
mysql_connection.commit()
print(f"{mysql_cursor.rowcount} accounts are updated!")
