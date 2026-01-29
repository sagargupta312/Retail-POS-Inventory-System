import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SPgupta@123",
    database="store"  
)

cursor = conn.cursor()
print("Connected to existing DB")

def sav_bill(bill_id, bill_date, total_amount, discount, final_amount, customer):
    sql = "INSERT INTO bills ( bill_id, bill_date, total_amount, discount, total, customer) VALUES (%s,%s, %s, %s, %s,%s)"
    cursor.execute(sql, ( bill_id, bill_date, total_amount, discount, final_amount, customer))
    conn.commit()

def save_bill_item(bill_id,id, product_name, quantity, mrp, price,discount, item_total):
    sql = """
    INSERT INTO bill_items (bill_id, id, product_name, quantity, mrp, price,discount, item_total)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (bill_id,id, product_name, quantity, mrp, price,discount, item_total))
    conn.commit()

def reduce_stock(id, quantity_sold):
    sql = """
    UPDATE inventory
    SET unit = unit - %s
    WHERE id = %s
    """
    cursor.execute(sql, (quantity_sold, id))
    conn.commit()


#customer database
#list of all p_numbers




def get_customer(p_number, t_bill):
    # get only phone numbers (fast & clean)
    cursor.execute("SELECT p_number FROM customer")
    data = cursor.fetchall()
    complete_data = [item[0] for item in data]

    if p_number in complete_data:
        # update existing customer
        sql = """
        UPDATE customer
        SET t_bill = t_bill + %s,
            last_bill_date = %s
        WHERE p_number = %s
        """
        cursor.execute(sql, (t_bill, date.today(), p_number))
        conn.commit()

    else:
        # insert new customer
        sql = """
        INSERT INTO customer (p_number, t_bill, last_bill_date)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (p_number, t_bill, date.today()))
        conn.commit()

        




