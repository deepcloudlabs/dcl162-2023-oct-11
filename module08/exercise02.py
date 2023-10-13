from mysql import connector
"""
mysql> create database banking;
Query OK, 1 row affected (0.00 sec)

mysql> use banking;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> show tables;
+-------------------+
| Tables_in_banking |
+-------------------+
| accounts          |
+-------------------+
1 row in set (0.00 sec)

mysql> desc accounts;
+---------+-----------------------------------+------+-----+---------+-------+
| Field   | Type                              | Null | Key | Default | Extra |
+---------+-----------------------------------+------+-----+---------+-------+
| iban    | varchar(40)                       | NO   | PRI | NULL    |       |
| balance | float                             | YES  |     | 1000    |       |
| status  | enum('ACTIVE','BLOCKED','CLOSED') | YES  |     | ACTIVE  |       |
+---------+-----------------------------------+------+-----+---------+-------+
3 rows in set (0.00 sec)"""
mysql_connection = connector.connect(
    host="localhost",
    user="root",
    password="Secret_123",
    database="banking"
)
mysql_cursor = mysql_connection.cursor()
mysql_cursor.execute("""
    create table accounts(
        iban varchar(40) primary key,
        balance float default 1000.0,
        status enum('ACTIVE', 'BLOCKED', 'CLOSED') default  'ACTIVE'
    )
""")