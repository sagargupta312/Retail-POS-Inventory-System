import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SPgupta@123",
    database="store"  
)


cursor = conn.cursor()
print("Connected to existing DB")


def show_products():
    cursor.execute("SELECT * FROM bills")
    data = cursor.fetchall()
    a = data
    return a

def show_products_by_date(start_date, end_date):
    sql = "SELECT * FROM bills WHERE bill_date BETWEEN %s AND %s"
    cursor.execute(sql, (start_date, end_date))
    data = cursor.fetchall()
    a = data
    return a
