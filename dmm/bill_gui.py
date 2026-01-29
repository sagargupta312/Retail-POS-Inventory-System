import customtkinter as ctk
from tkinter import ttk, messagebox
import inventory_db
import time
import bill_search_db
import importlib
from datetime import datetime


app = ctk.CTk()

app.configure(fg_color="#F8FAFC") 
app.geometry("1310x620")

app.title("DMM MANAGEMENT APP")
work_frame = ctk.CTkFrame(app, width=423, height=550, fg_color="#D2EBFF")
work_frame.place(x=2, y=98)


#label for left side
id_label = ctk.CTkLabel(work_frame, text="ID", font=("Segoe UI", 20), text_color="#1F2937")
id_label.place(x=20, y=135)
id_entry = ctk.CTkEntry(work_frame, width=200, fg_color="white", text_color="black")
id_entry.place(x=150, y=135)

item_label = ctk.CTkLabel(work_frame, text="Items Sold", font=("Segoe UI", 20), text_color="#1F2937")
item_label.place(x=20, y=185)
item_entry = ctk.CTkEntry(work_frame, width=200, fg_color="white", text_color="black")
item_entry.place(x=150, y=185)

quantity_label = ctk.CTkLabel(work_frame, text="Quantity", font=("Segoe UI", 20), text_color="#1F2937")
quantity_label.place(x=20, y=235)
quantity_entry = ctk.CTkEntry(work_frame, width=200, fg_color="white", text_color="black")
quantity_entry.place(x=150, y=235)

mrp_label = ctk.CTkLabel(work_frame, text="MRP", font=("Segoe UI", 20), text_color="#1F2937")
mrp_label.place(x=20, y=285)
mrp_entry = ctk.CTkEntry(work_frame, width=200, fg_color="white", text_color="black")
mrp_entry.place(x=150, y=285)

price_label = ctk.CTkLabel(work_frame, text="Price", font=("Segoe UI", 20), text_color="#1F2937")
price_label.place(x=20, y=335)
price_entry = ctk.CTkEntry(work_frame, width=200, fg_color="white", text_color="black")
price_entry.place(x=150, y=335)


#automatically fill
def auto():
    a = id_entry.get()
    for i in inventory_db.show_products():
        if str(i[0]) == a:
            item_entry.delete(0, "end")
            item_entry.insert(0, i[1])

            quantity_entry.delete(0, "end")
            quantity_entry.insert(0, "1")

            mrp_entry.delete(0, "end")
            mrp_entry.insert(0, i[3])

            price_entry.delete(0, "end")
            price_entry.insert(0, i[2])
            break
    else:
            messagebox.showwarning("Warning", "Product ID not found")
            id_entry.focus()
            id_entry.delete(0, "end")
            

#button
grand_total = 0
total_label = ctk.CTkLabel(app, text=f"Total:{grand_total}" , font=("Segoe UI", 26, "bold"), text_color="#1F2937")
total_label.place(x=1000, y=570)
search_product_label = ctk.CTkLabel(work_frame, text="Enter Product ID to Auto Fill", font=("Segoe UI", 26, "bold"), text_color="#000000")
search_product_label.place(x=35, y=35)
items_list_label = ctk.CTkLabel(app, text="Items List", font=("Segoe UI", 26, "bold"), text_color="#000000")
items_list_label.place(x=450, y=130)
design = ctk.CTkLabel(work_frame, text="-------------------------------------------------", font=("Segoe UI", 20), text_color="#1F2937")
design.place(x=18, y=80)
search_bill_id_label = ctk.CTkLabel(app, text="Bill Id", font=("Segoe UI", 20, "bold"), text_color="#000000")
search_bill_id_label.place(x=720, y=140)

search_bill_id_entry = ctk.CTkEntry(app, width=150, fg_color="white", text_color="black", font=("Segoe UI", 10))
search_bill_id_entry.place(x=800, y=140)




def save_data():
    if float(quantity_entry.get())<=inventory_db.get_product_quantity(id_entry.get())[0][0]:
        global grand_total
        discount = float(mrp_entry.get()) - float(price_entry.get())
        total = float(quantity_entry.get()) * float(price_entry.get())
        grand_total += total
        a = (id_entry.get(), item_entry.get(), quantity_entry.get(), mrp_entry.get(), price_entry.get(), discount, total)
        tree.insert("", "end", values=a)
        id_entry.delete(0, "end")
        item_entry.delete(0, "end")
        quantity_entry.delete(0, "end")
        mrp_entry.delete(0, "end")
        price_entry.delete(0, "end")
        id_entry.focus()
        total_label.configure(text=f"Total:{grand_total}")
    else:
        messagebox.showwarning("Warning", "Insufficient stock")



    
    
    print("Saving Data...")
#button for left side
enter_btn = ctk.CTkButton(work_frame,width=260, text="Enter", cursor="hand2", font=("Segoe UI", 26, "bold"), text_color="#F6F6F6", command= save_data)
enter_btn.place(x=100 ,y=440)

id_entry.bind("<Return>", lambda e: (auto(), quantity_entry.focus()))
item_entry.bind("<Return>", lambda e: quantity_entry.focus())
quantity_entry.bind("<Return>", lambda e: mrp_entry.focus())
mrp_entry.bind("<Return>", lambda e: price_entry.focus())
price_entry.bind("<Return>", lambda e: enter_btn.invoke())


#margin
line = ctk.CTkFrame(app,width=2,height=1000,fg_color="#CBD5E1")
line.place(x = 427, y = 100)


#right side frame

table_frame = ctk.CTkFrame(app, width=770, height=550, fg_color="#BCDFFC")
table_frame.place(x=432, y=200)


#table

columns = ("id", "items", "quantit", "mrp", "price", "discount", "total")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=20
)
style = ttk.Style()

style.configure("Treeview.Heading",font=("Segoe UI", 14, "bold"),padding=(10, 10))
# heading product view ka
tree.heading("id", text="ID" )
tree.heading("items", text="Items")
tree.heading("quantit", text="Quantity")
tree.heading("mrp", text="MRP") 
tree.heading("price", text="Price")
tree.heading("discount", text="Discount")
tree.heading("total", text="Total")

# column hai
tree.column("id", width=150, anchor="center")
tree.column("items", width=220)
tree.column("quantit", width=120, anchor="center")
tree.column("mrp", width=120, anchor="center")
tree.column("price", width=120, anchor="center")
tree.column("discount", width=120, anchor="center")
tree.column("total", width=120, anchor="center")


style = ttk.Style()
style.configure(
    "Treeview",
    font=("Segoe UI", 11)  
)

# SCROLLBAR
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)
total_label.lift()
# #show data
# tree.insert("", "end", values=i)


#delete button
def delete_data():
    global grand_total
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0])["values"]
    grand_total -= float(values[6])
    total_label.configure(text=f"Total:{grand_total}")
    tree.delete(selected[0])

    print("Deleting Data...")
delete_btn = ctk.CTkButton(app, text="Delete", cursor="hand2", width = 75, font=("Segoe UI", 12, "bold"), command= delete_data)
delete_btn.place(x=1230, y=400)

#delete all button
def delete_all_data():
    for item in tree.get_children():
        tree.delete(item)
    print("Deleting All Data...")
    global grand_total
    grand_total = 0
    total_label.configure(text="Total:0")
delete_all_btn = ctk.CTkButton(app, text="Delete All", cursor="hand2",width = 75, font=("Segoe UI", 12, "bold"), command= delete_all_data)
delete_all_btn.place(x=1230, y=340)


#update button
def update_data():
    global grand_total
    
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0])["values"]

    id_entry.delete(0, "end")
    id_entry.insert(0, values[0])

    item_entry.delete(0, "end")
    item_entry.insert(0, values[1])

    quantity_entry.delete(0, "end")
    quantity_entry.insert(0, values[2])

    mrp_entry.delete(0, "end")
    mrp_entry.insert(0, values[3])

    price_entry.delete(0, "end")
    price_entry.insert(0, values[4])

    delete_data()


    print("Updating Data...")
update_btn = ctk.CTkButton(app, text="Update", cursor="hand2", width = 75, font=("Segoe UI", 12, "bold"), command= update_data)
update_btn.place(x=1230, y=280)

def history_data():
    import sys
    if "history" in sys.modules:
        del sys.modules["history"]
    import history
history_btn = ctk.CTkButton(app, text="History", cursor="hand2", width = 75, font=("Segoe UI", 12, "bold"), command= history_data)
history_btn.place(x=1230, y=465)

#save button
def save_bill():
    bill_items = []

    for item in tree.get_children():
        values = tree.item(item)["values"]
        bill_items.append(values)

    if not bill_items:
        messagebox.showwarning("Warning", "No items in bill")
        return

    import save_bill
    aa = search_bill_id_entry.get()
    save_bill.open_window(bill_items,aa)
    app.destroy()


save_btn = ctk.CTkButton(app, text="Save Bill (ctrl+F1)", cursor="hand2", font=("Segoe UI", 20, "bold"), command= save_bill)
save_btn.place(x=750, y=575)

price_entry.bind("<F1>", lambda e: save_btn.invoke())
price_entry.bind("<F2>", lambda e: update_btn.invoke())
price_entry.bind("<F3>", lambda e: delete_all_btn.invoke())
price_entry.bind("<F4>", lambda e: delete_btn.invoke())


#sajavwat

#safed frame
safed_frame = ctk.CTkFrame(app, width=1300, height = 50, fg_color="#F8FAFC")
safed_frame.place(x=0, y=0)
safed_frame.lift()
shop_name = ctk.CTkLabel(safed_frame, text = "D MEGA MART", font=("Segoe UI", 26, "bold"), text_color="black")
shop_name.place(x = 500, y = 10)
#blue frame
blue_frame = ctk.CTkFrame(app, width=1400, height = 50, fg_color="blue")
blue_frame.place(x=-10, y=48)

def home_page():
    app.destroy()
    import home_page
logout_btn = ctk.CTkButton(blue_frame, text = "Home", font=("Segoe UI", 16, "bold"), width= 80, height= 40, fg_color= "#0D0D61", command= home_page)
logout_btn.place(x=1220, y=5)

def cust():
    import sys
    if "customer_list" in sys.modules:
        del sys.modules["customer_list"]
    import customer_list
customer_btn = ctk.CTkButton(blue_frame, text = "Customer", font=("Segoe UI", 16, "bold"), width= 80, height= 40, fg_color= "#212181", command= cust)
customer_btn.place(x=980, y=5)

def inn():          
    import sys
    if "inventory" in sys.modules:
        del sys.modules["inventory"]
    import inventory
inventory_btn = ctk.CTkButton(blue_frame, text = "Inventory", font=("Segoe UI", 16, "bold"), width= 80, height= 40, fg_color= "#212181", command= inn)
inventory_btn.place(x=1100, y=5)



def search_bill():
    global grand_total
    bill_id = search_bill_id_entry.get()
    data = bill_search_db.search_bill_items(bill_id)

    if not data:
        messagebox.showwarning("Not Found", "Bill not found")
        return

    for item in tree.get_children():
        tree.delete(item)

    grand_total = 0
    for i in data:
        a = (i[1], i[2], i[3], i[4], i[5], i[6], i[7])
        grand_total += float(i[7])
        tree.insert("", "end", values=a) 

    total_label.configure(text=f"Total:{grand_total}")
    print("done")


search_bill_id_btn = ctk.CTkButton(app, text="Search", cursor="hand2", width = 75, font=("Segoe UI", 12, "bold"),command = search_bill)
search_bill_id_btn.place(x=960, y=140)

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000, update_time)

time_label = ctk.CTkLabel(safed_frame, text="",font=("Segoe UI", 20), text_color="#6B7280"   )
time_label.place(x=5, y=2)

update_time()




app.mainloop()