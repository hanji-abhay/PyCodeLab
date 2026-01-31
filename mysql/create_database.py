import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)
cursor = con.cursor()
cursor.execute("CREATE DATABASE mydatabase")
print("Database created successfully ✅")
con.close()
