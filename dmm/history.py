import customtkinter as ctk
from tkinter import ttk
import history_db

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("1100x650")
app.title("Bill History")
app.configure(fg_color="#F8FAFC")


top_frame = ctk.CTkFrame(app, height=110, fg_color="#D2EBFF")
top_frame.pack(fill="x", padx=10, pady=10)

# Start Date
ctk.CTkLabel( top_frame,  text="Start Date (YYYY-MM-DD)",  font=("Segoe UI", 15, "bold")).place(x=20, y=10)

start_date_entry = ctk.CTkEntry(top_frame, width=170, height=36)
start_date_entry.place(x=20, y=45)

# End Date
ctk.CTkLabel(  top_frame,text="End Date (YYYY-MM-DD)",  font=("Segoe UI", 15, "bold")).place(x=220, y=10)

end_date_entry = ctk.CTkEntry(top_frame, width=170, height=36)
end_date_entry.place(x=220, y=45)

# Bill ID
ctk.CTkLabel(top_frame,text="Bill ID",font=("Segoe UI", 15, "bold")).place(x=420, y=10)

bill_id_entry = ctk.CTkEntry(top_frame, width=200, height=36)
bill_id_entry.place(x=420, y=45)

# Customer
ctk.CTkLabel( top_frame, text="Customer", font=("Segoe UI", 15, "bold")).place(x=640, y=10)

customer_entry = ctk.CTkEntry(top_frame, width=220, height=36)
customer_entry.place(x=640, y=45)




table_frame = ctk.CTkFrame(app)
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("bill_id", "bill_date", "total_amount", "discount", "final_total", "customer")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=16
)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Segoe UI", 14, "bold"))
style.configure("Treeview", font=("Segoe UI", 13), rowheight=30)

# Headings
tree.heading("bill_id", text="Bill ID")
tree.heading("bill_date", text="Bill Date & Time")
tree.heading("total_amount", text="Total Amount")
tree.heading("discount", text="Discount")
tree.heading("final_total", text="Final Total")
tree.heading("customer", text="Customer")

# Column widths
tree.column("bill_id", width=150, anchor="center")
tree.column("bill_date", width=220, anchor="center")
tree.column("total_amount", width=150, anchor="center")
tree.column("discount", width=140, anchor="center")
tree.column("final_total", width=150, anchor="center")
tree.column("customer", width=200, anchor="center")

tree.pack(fill="both", expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


bottom_frame = ctk.CTkFrame(app, height=70)
bottom_frame.pack(fill="x", padx=10, pady=10)

total_sales_label = ctk.CTkLabel(bottom_frame,text="Total Sales: 0",font=("Segoe UI", 22, "bold"))
total_sales_label.pack(side="right", padx=20)


for item in tree.get_children():
    tree.delete(item)

data = history_db.show_products()

global grand_total
grand_total = 0

for row in range(len(data)-1, -1, -1):
    tree.insert("", "end", values=data[row])
    grand_total += float(data[row][4])

total_sales_label.configure(text=f"Total Sales: {grand_total}")


def on_select(event):
    selected = tree.selection()
    if not selected:
        return

    values = tree.item(selected[0])["values"]

    bill_id_entry.delete(0, "end")
    bill_id_entry.insert(0, values[0])

    customer_entry.delete(0, "end")
    customer_entry.insert(0, values[5])

tree.bind("<<TreeviewSelect>>", on_select)


def searcho(): 
    start_date = start_date_entry.get().strip()
    end_date = end_date_entry.get().strip()
    bill_id = bill_id_entry.get().strip()
    customer = customer_entry.get().strip()

    # Clear table
    for item in tree.get_children():
        tree.delete(item)

    data = history_db.show_products()

    if  start_date == end_date == bill_id == customer =="":
        filtered_data = data
    elif bill_id:
        filtered_data = [row for row in data if str(row[0]) == bill_id]

    elif customer:
        filtered_data = [ row for row in data if customer.lower() in str(row[5]).lower()]

    # Date filter
    else:
        filtered_data = history_db.show_products_by_date(start_date, end_date)

    # Calculate total
    global grand_total
    grand_total = 0

    for row in filtered_data:
        tree.insert("", "end", values=row)
        grand_total += float(row[4])

    total_sales_label.configure(text=f"Total Sales: {grand_total}")

search_btn = ctk.CTkButton( top_frame, text="Search", width=120, height=36, font=("Segoe UI", 15, "bold"), command=searcho)
search_btn.place(x=900, y=45)



customer_entry.bind("<Return>", lambda e: searcho())
bill_id_entry.bind("<Return>", lambda e: searcho())
end_date_entry.bind("<Return>", lambda e: searcho())




app.mainloop()
