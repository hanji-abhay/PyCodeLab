import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "your_password",
    database = "your_database"
)
cursor = conn.cursor()
a = input("Enter query to search for the table from e_commerce DATABASE: ")
cursor.execute(a)
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
