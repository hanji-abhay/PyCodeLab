import mysql.connector

# Step 1: Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password"
    )
    cursor = conn.cursor()
    print("Connected to MySQL ✅")
except Exception as e:
    print("Connection failed:", e)
    exit()

# Step 2: Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS DataBase_name")
conn.database = 'DataBase_name'

# Step 3: Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS table_name(
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    c_marks INT,
    cpp_marks INT,
    python_marks INT,
    total INT,
    percentage FLOAT,
    result VARCHAR(10)
)
""")

# Step 4: Take user input
roll_no = int(input("Enter Roll No: "))
name = input("Enter Name: ")
c_marks = int(input("Enter C Marks: "))
cpp_marks = int(input("Enter C++ Marks: "))
python_marks = int(input("Enter Python Marks: "))
total = c_marks + cpp_marks + python_marks
percentage = (total / 300) * 100
result = "Pass" if percentage >= 33 else "Fail"

# Insert into database
insert_query = """
INSERT INTO table_name (roll_no, name, c_marks, cpp_marks, python_marks, total, percentage, result)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
values = (roll_no, name, c_marks, cpp_marks, python_marks, total, percentage, result)
cursor.execute(insert_query, values)
conn.commit()

# Step 5: Save result to text file
file_name = f"{roll_no}.txt"
with open(file_name, "w") as f:
    f.write(f"-------- STUDENT --------\n\n")
    f.write(f"Roll No : {roll_no}       |    Name: {name} \n\n")
    f.write(f"-------- MARKS --------\n\n")
    f.write(f"C Marks: {c_marks}        |     C++ Marks: {cpp_marks}      |      Python Marks: {python_marks}\n\n")
    f.write(f"---------- RESULT ----------\n\n")
    f.write(f"Total Marks: {total}      |     Percentage: {percentage}    |      Final Result: {result}")  
print(f"Result saved to {file_name} ✅")

conn.close()
