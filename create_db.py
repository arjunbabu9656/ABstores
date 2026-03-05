import pymysql
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Arjunaju@02')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
    print("Database created successfully")
except Exception as e:
    print(f"Error creating database: {e}")
