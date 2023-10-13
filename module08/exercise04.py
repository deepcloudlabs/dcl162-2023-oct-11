from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""
    select iban,balance,status
    from accounts
    limit 0,25
""")
for row in mysql_cursor:
    print(f"iban: {row[0]}, balance: {row[1]}, status: {row[2]}")
