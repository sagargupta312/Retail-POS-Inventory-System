import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SPgupta@123",
    database="store"  
)

cursor = conn.cursor()
print("Connected to existing DB")


def search_bill_items(bill_id):
    sql = "SELECT * FROM bill_items WHERE LOWER(bill_id) LIKE %s"
    cursor.execute(sql, (f"%{bill_id.lower()}%",))
    data = cursor.fetchall()
    return data
    