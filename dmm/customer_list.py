import customtkinter as ctk
from tkinter import ttk
import inventory_db

# ---------------- APP ----------------
app = ctk.CTk()
app.configure(fg_color="#EAF4FF")
app.geometry("900x520")
app.title("customer")

# ---------------- SEARCH FRAME ----------------
search_frame = ctk.CTkFrame(app, width=860, height=110, fg_color="#D2EBFF", corner_radius=12)
search_frame.place(x=20, y=15)

ctk.CTkLabel(search_frame, text="Phone Number", text_color="#1F2937").place(x=20, y=20)
phone_entry = ctk.CTkEntry(search_frame, width=180, fg_color="white", text_color="black")
phone_entry.place(x=140, y=20)

ctk.CTkLabel(search_frame, text="From Date", text_color="#1F2937").place(x=360, y=20)
from_date_entry = ctk.CTkEntry(search_frame, width=130, placeholder_text="YYYY-MM-DD", fg_color="white", text_color="black")
from_date_entry.place(x=440, y=20)

ctk.CTkLabel(search_frame, text="To Date", text_color="#1F2937").place(x=360, y=60)
to_date_entry = ctk.CTkEntry(search_frame, width=130, placeholder_text="YYYY-MM-DD", fg_color="white", text_color="black")
to_date_entry.place(x=440, y=60)

# ---------------- TABLE STYLE ----------------
style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 13))
style.configure("Treeview.Heading", font=("Segoe UI", 14, "bold"))

# ---------------- TABLE FRAME ----------------
table_frame = ctk.CTkFrame(app, width=860, height=360, fg_color="#FFFFFF", corner_radius=12)
table_frame.place(x=20, y=140)

columns = ("phone", "total_bill", "last_date")

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=25)

tree.heading("phone", text="Phone Number")
tree.heading("total_bill", text="Total Bill")
tree.heading("last_date", text="Last Bill Date")

tree.column("phone", width=450, anchor="center")
tree.column("total_bill", width=300, anchor="center")
tree.column("last_date", width=300, anchor="center")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True, padx=10, pady=10)

# ---------------- FUNCTIONS ----------------
def show_data():
    tree.delete(*tree.get_children())
    for row in inventory_db.show_customer():
        tree.insert("", "end", values=row)

def search():
    tree.delete(*tree.get_children())

    phone = phone_entry.get().strip()
    from_date = from_date_entry.get().strip()
    to_date = to_date_entry.get().strip()

    if not phone and not from_date and not to_date:
        show_data()
        return

    data = inventory_db.search_customer(phone, from_date, to_date)
    for row in data:
        tree.insert("", "end", values=row)

# ---------------- SEARCH BUTTON ----------------
search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    width=120,
    height=36,
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    command=search
)
search_btn.place(x=650, y=38)

# ---------------- INITIAL LOAD ----------------
show_data()

app.mainloop()
