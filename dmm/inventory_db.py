import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SPgupta@123",
    database="store"  
)

cursor = conn.cursor()
print("Connected to existing DB")

def add_product( id, pro, sp, cp, unit, distrinutar,category):
    sql = "INSERT INTO inventory ( id, Product, Selling_Price, Cost_Price, Unit,Distributor,category) VALUES (%s, %s, %s, %s,%s, %s, %s)"
    cursor.execute(sql, ( id, pro, sp, cp, unit, distrinutar,category))
    conn.commit()

def show_products():
    cursor.execute("SELECT * FROM inventory")
    data = cursor.fetchall()

    a = data
    return a
#customer
def show_customer():
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()

    a = data
    return a

def show_last_product():
    cursor.execute("SELECT * FROM inventory")
    data = cursor.fetchall()
    return data[len(data)-1]


def delete_all():
    sql = "DELETE FROM inventory WHERE id>0"
    cursor.execute(sql)
    conn.commit()

def search(filter, product):
    sql = f"SELECT * FROM inventory WHERE LOWER({filter}) LIKE %s"
    cursor.execute(sql, (f"%{product.lower()}%",))
    data = cursor.fetchall()
    return data

def search_customer(p_number="", from_date="", to_date=""):
    sql = "SELECT * FROM customer WHERE 1=1"
    params = []

    if p_number:
        sql += " AND p_number LIKE %s"
        params.append(f"%{p_number}%")

    if from_date and to_date:
        sql += " AND last_bill_date BETWEEN %s AND %s"
        params.extend([from_date, to_date])

    cursor.execute(sql, tuple(params))
    return cursor.fetchall()


def delete(id):
    sql = "DELETE FROM inventory WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()

#for billing page
def get_product_quantity(id):
    sql = "SELECT unit FROM inventory WHERE id = %s"
    cursor.execute(sql, (id,))
    data = cursor.fetchall()
    return data

    

    



