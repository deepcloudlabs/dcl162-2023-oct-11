from mysql import connector

mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
accounts = [
    ("tr1", 1_000_000.0, 'ACTIVE'),
    ("tr2", 0.0, 'CLOSED'),
    ("tr3", 0.0, 'CLOSED'),
    ("tr4", 2_000_000.0, 'ACTIVE'),
    ("tr5", 3_000_000.0, 'ACTIVE'),
    ("tr6", 4_000_000.0, 'BLOCKED')
]
for account in accounts:
    mysql_cursor.execute(f"""
        insert into accounts values ('{account[0]}',{account[1]},'{account[2]}')
    """)
mysql_connection.commit()
