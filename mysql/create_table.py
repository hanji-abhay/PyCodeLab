import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)
cursor = con.cursor()
query = """
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50)
)
"""
cursor.execute(query)
print("Table created successfully ✅")
con.close()
