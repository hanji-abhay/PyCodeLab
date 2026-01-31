import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_sql_password",
    database = "your_database"
)
cursor = conn.cursor()
class data:
    def info(self):
        get_info = '''SELECT * FROM record'''
        cursor.execute(get_info)
        got_info = cursor.fetchall()
        for information in got_info:
            print(information)
d= data()
d.info()
conn.commit()
conn.close()
