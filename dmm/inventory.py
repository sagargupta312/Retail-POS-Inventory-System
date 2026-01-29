import customtkinter as ctk
from tkinter import ttk, messagebox
import inventory_db
from datetime import datetime
import sys


app = ctk.CTk()





#SHOW DATA TREE
def show_data():
    a = inventory_db.show_products()
    for i in range(len(a)-1,-1,-1):
        tree.insert("", "end", values=a[i])

def logout():
    app.destroy()

app_title = ctk.CTkLabel(app, text="Inventory Management System", font=("Segoe UI", 32, "bold"), text_color="#0F172A")
app_title.place(x=420, y=5)

app_subtitle = ctk.CTkLabel( app, text="Manage products, categories and stock easily", font=("Segoe UI", 14), text_color="#475569")
app_subtitle.place(x=450, y=45)

app.configure(fg_color="#F8FAFC") 
app.geometry("1200x600")
app.title("DMM MANAGEMENT APP")

frame = ctk.CTkFrame(app, width=400, height=500, fg_color="#F8FAFC")
frame.place(x=20, y=120)

frame.grid_propagate(False)


heading = ctk.CTkLabel(frame, text="Add Product", font=("Segoe UI", 26, "bold"), text_color="#1F2937")
heading.grid(row=0, column=0, columnspan=2, pady=10)

label_font = ("Segoe UI", 20)
label_color = "#3D3D3E"

# Category
category_label = ctk.CTkLabel(frame, text="Category", font=label_font, text_color=label_color)
category_label.grid(row=1, column=0, padx=20, pady=8, sticky="w")

grocery_categories = ["Fruits","Vegetables","Dairy","Bakery","Grains & Cereals","Pulses & Lentils","Spices & Masalas","Edible Oils","Snacks","Beverages","Instant & Ready Foods","Frozen Foods","Sweets & Confectionery","Personal Care","Household Cleaning","Baby Care","Pet Care","Health & Wellness","Stationery","Puja & Festival Items","General Merchandise"]
category_combo = ctk.CTkComboBox(frame, values=grocery_categories, width=180, fg_color="white", text_color="black")
category_combo.grid(row=1, column=1, padx=10, pady=8)

# Product ID
id_label = ctk.CTkLabel(frame, text="Product ID", font=label_font, text_color=label_color)
id_label.grid(row=2, column=0, padx=20, pady=8, sticky="w")

id_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
id_entry.grid(row=2, column=1, padx=10, pady=8)

# Product
product_label = ctk.CTkLabel(frame, text="Product", font=label_font, text_color=label_color)
product_label.grid(row=3, column=0, padx=20, pady=8, sticky="w")

product_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
product_entry.grid(row=3, column=1, padx=10, pady=8)

# Selling Price
sp_label = ctk.CTkLabel(frame, text="Selling Price", font=label_font, text_color=label_color)
sp_label.grid(row=4, column=0, padx=20, pady=8, sticky="w")

sp_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
sp_entry.grid(row=4, column=1, padx=10, pady=8)

# Cost Price
cp_label = ctk.CTkLabel(frame, text="MRP", font=label_font, text_color=label_color)
cp_label.grid(row=5, column=0, padx=20, pady=8, sticky="w")

cp_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
cp_entry.grid(row=5, column=1, padx=10, pady=8)

# Unit
unit_label = ctk.CTkLabel(frame, text="Quantity", font=label_font, text_color=label_color)
unit_label.grid(row=6, column=0, padx=20, pady=8, sticky="w")

unit_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
unit_entry.grid(row=6, column=1, padx=10, pady=8)

# Distributor
dist_label = ctk.CTkLabel(frame, text="Distributor", font=label_font, text_color=label_color)
dist_label.grid(row=7, column=0, padx=20, pady=8, sticky="w")

dist_entry = ctk.CTkEntry(frame, width=180, fg_color="white", text_color="black")
dist_entry.grid(row=7, column=1, padx=10, pady=8)

id_entry.bind("<Return>", lambda e: ( product_entry.focus()))
product_entry.bind("<Return>", lambda e: sp_entry.focus())
sp_entry.bind("<Return>", lambda e: cp_entry.focus())
cp_entry.bind("<Return>", lambda e: unit_entry.focus())
unit_entry.bind("<Return>", lambda e: dist_entry.focus())
dist_entry.bind("<Return>", lambda e:  save_btn.invoke())

# save button
def save():
    a = id_entry.get()
    b = product_entry.get()
    d = sp_entry.get()
    e = cp_entry.get()
    f = unit_entry.get()
    g = dist_entry.get()
    z = category_combo.get()

    if "" in ( a, b, d, e, f, g, z):
        messagebox.showerror("Error", "All fields are required")
    else:
        inventory_db.add_product(a, b, d, e, f, g,z)
        tree.insert("", "end", values=inventory_db.show_last_product())
        messagebox.showinfo("Success", "Product Added")
        id_entry.delete(0, "end")
        product_entry.delete(0, "end")
        sp_entry.delete(0, "end")
        cp_entry.delete(0, "end")
        unit_entry.delete(0, "end")
        dist_entry.delete(0, "end")



save_btn = ctk.CTkButton(frame, text="Save", command=save, width=200, height=50)
save_btn.grid(row=8, column=0, columnspan=2, pady=25)
save_btn.bind("<Return>", lambda e: id_entry.focus())
#safed frame
safed_frame = ctk.CTkFrame(app, width=1300, height = 50, fg_color="#F8FAFC")
safed_frame.place(x=0, y=0)
safed_frame.lift()
shop_name = ctk.CTkLabel(safed_frame, text = "D MEGA MART", font=("Segoe UI", 26, "bold"), text_color="black")
shop_name.place(x = 500, y = 10)
#blue frame
blue_frame = ctk.CTkFrame(app, width=1300, height = 50, fg_color="blue")
blue_frame.place(x=0, y=48)

logout_btn = ctk.CTkButton(blue_frame, text = "Home", font=("Segoe UI", 16, "bold"), width= 80, height= 40, fg_color= "#0D0D61", command= logout)
logout_btn.place(x=1115, y=5)

#margin
line = ctk.CTkFrame(app,width=2,height= 900,fg_color="#CBD5E1")
line.place(x = 375, y = 120)

#right side table
product_entryy = ctk.CTkEntry(app, placeholder_text= "Search Products/Category..",font=("Segoe UI", 15), fg_color="white",  width=200, text_color="black")
product_entryy.place(x=640, y=120)

# categories = ["Search all", "Fruits","Vegetables","Dairy","Bakery","Grains & Cereals","Pulses & Lentils","Spices & Masalas","Edible Oils","Snacks","Beverages","Instant & Ready Foods","Frozen Foods","Sweets & Confectionery","Personal Care","Household Cleaning","Baby Care","Pet Care","Health & Wellness","Stationery","Puja & Festival Items","General Merchandise"]
filter_box = ctk.CTkComboBox(app,values=["Search all" ,"Category", "Distributor", "Product", "id"],width=180, fg_color="white", text_color="black")
filter_box.place(x=850, y=120)


def search_products():
    filterr = filter_box.get()
    productt = product_entryy.get()
    for item in tree.get_children():
            tree.delete(item)
    if filterr == "Search all":
        show_data()  
    else:
        for i in inventory_db.search(filterr, productt):
            tree.insert("", "end", values=i)
        
search_btn = ctk.CTkButton(app, text = "Search", command=search_products)
search_btn.place(x=1040, y=120)

#margin
line = ctk.CTkFrame(app,width=1000,height=2,fg_color="#CBD5E1")
line.place(x = 385, y = 10)
#right side text
headingg = ctk.CTkLabel(app, text="Product Catalog & Editor", font=("Segoe UI", 20, "bold"), text_color="#1F2937")
headingg.place(x = 390, y = 120)

# grame for the table
table_frame = ctk.CTkFrame(app, width=800, height=350)
table_frame.place(x=390, y= 170)

# IMPORTANT: allow tkinter widgets inside
table_frame.pack_propagate(False)

# tree view chat gpt sein 
columns = ("id", "product", "sp", "cp", "unit", "distributor")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)
style = ttk.Style()

style.configure("Treeview.Heading",font=("Segoe UI", 14, "bold"),padding=(10, 10))
# heading product view ka
tree.heading("id", text="ID" )
tree.heading("product", text="Product")
tree.heading("sp", text="Selling Price")
tree.heading("cp", text="MRP")
tree.heading("unit", text="Quantity")
tree.heading("distributor", text="Distributor")

# column hai
tree.column("id", width=100, anchor="center")
tree.column("product", width=150)
tree.column("sp", width=120, anchor="center")
tree.column("cp", width=120, anchor="center")
tree.column("unit", width=80, anchor="center")
tree.column("distributor", width=150)


style = ttk.Style()
style.configure(
    "Treeview",
    font=("Segoe UI", 11) 
)


# ---------- SCROLLBAR ----------
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)




show_data()





#buttttons





def update_product():
    selected = tree.selection()
    if not selected:
        return

    values = tree.item(selected[0])["values"]

    # Fill form entries
    id_entry.delete(0, "end")
    id_entry.insert(0, values[0])

    product_entry.delete(0, "end")
    product_entry.insert(0, values[1])

    sp_entry.delete(0, "end")
    sp_entry.insert(0, values[2])

    cp_entry.delete(0, "end")
    cp_entry.insert(0, values[3])

    unit_entry.delete(0, "end")
    unit_entry.insert(0, values[4])

    dist_entry.delete(0, "end")
    dist_entry.insert(0, values[5])

    delete_product()
    
ctk.CTkButton(app, text="Update Product", command=update_product, width=160, height=50).place(x=520, y=545)




#delete
def delete_product(): 
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0])["values"]
    inventory_db.delete(values[0])
    for item in tree.get_children():
        tree.delete(item)
    show_data()


ctk.CTkButton(app, text="Delete Product", command=delete_product, width=160, fg_color="#DC2626", hover_color="#B91C1C", height=50).place(x=700, y=545)

#delete all button
def delete_all_products(): 
    answer = messagebox.askyesno("Confirm", "Do you want to continue?")
    if answer:
        inventory_db.delete_all()
        for item in tree.get_children():
            tree.delete(item)

ctk.CTkButton(app, text="Delete All", command=delete_all_products, width=160, fg_color="#7C2D12", hover_color="#9A3412", height=50).place(x=880, y=545)




def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000, update_time)

time_label = ctk.CTkLabel(app, text="",font=("Segoe UI", 14), text_color="#6B7280"   )

time_label.place(x=20, y=12)
update_time()
app.mainloop()