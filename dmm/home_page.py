import customtkinter as ctk
import time

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("DMM MANAGEMENT APP")
app.configure(fg_color="#F8FAFC")

#safed
top_frame = ctk.CTkFrame(app, height=60, fg_color="#F8FAFC", corner_radius=0)
top_frame.pack(fill="x")

title_label = ctk.CTkLabel(
    top_frame,
    text="D MEGA MART",
    font=("Segoe UI", 28, "bold"),
    text_color="#000000"
)
title_label.pack(pady=10)

#blue frame
nav_frame = ctk.CTkFrame(app, height=50, fg_color="#1E40AF", corner_radius=0)
nav_frame.pack(fill="x")


home_label = ctk.CTkLabel( nav_frame, text="Home Dashboard", font=("Segoe UI", 18, "bold"), text_color="white")
home_label.place(x=20, y=10)

#time
time_label = ctk.CTkLabel( nav_frame, font=("Segoe UI", 14, "bold"), text_color="white")
time_label.place(relx=0.5, rely=0.5, anchor="center")

def update_time():
    current_time = time.strftime("%d %b %Y | %I:%M:%S %p")
    time_label.configure(text=current_time)
    app.after(1000, update_time)

update_time()

#logout button
def logout():
    app.destroy()
    import home_page   

#frame code by chatgpt
logout_btn = ctk.CTkButton( nav_frame, text="Logout",    width=90, height=36, font=("Segoe UI", 14, "bold"), fg_color="#0D0D61", hover_color="#020617", cursor="hand2", command=logout)
logout_btn.place(relx=0.92, rely=0.5, anchor="center")


main_frame = ctk.CTkFrame( app, width=520, height=380, fg_color="#D2EBFF", corner_radius=20)
main_frame.place(relx=0.5, rely=0.58, anchor="center")
main_frame.pack_propagate(False)

welcome_label = ctk.CTkLabel( main_frame, text="Welcome 👋", font=("Segoe UI", 26, "bold"), text_color="#1F2937")
welcome_label.pack(pady=(25, 5))

subtitle_label = ctk.CTkLabel( main_frame, text="Lets Goooo", font=("Segoe UI", 16), text_color="#374151")
subtitle_label.pack(pady=(0, 25))


def open_inventory():
    import sys
    if "inventory" in sys.modules:
        del sys.modules["inventory"]
    import inventory

def open_billing():
    import sys
    if "bill_gui" in sys.modules:
        del sys.modules["bill_gui"]
    import bill_gui

def open_customer():
    import sys
    if "customer_list" in sys.modules:
        del sys.modules["customer_list"]
    import customer_list

def open_history():
    import sys
    if "history" in sys.modules:
        del sys.modules["history"]
    import history

# btn_style = {font: ("Segoe UI", 17, "bold"), width: 300, height: 48, cursor: "hand2",}

ctk.CTkButton(main_frame, text="Inventory Management", font = ("Segoe UI", 17, "bold"), width= 300, height= 48, cursor="hand2",fg_color="#2563EB",  hover_color="#1D4ED8", command=open_inventory).pack(pady=10)

ctk.CTkButton( main_frame,text="Billing System", font = ("Segoe UI", 17, "bold"), width= 300, height= 48, cursor="hand2",fg_color="#16A34A",hover_color="#15803D", command=open_billing).pack(pady=10)

ctk.CTkButton(main_frame, text="Customer Management",  font = ("Segoe UI", 17, "bold"), width= 300, height= 48, cursor="hand2",fg_color="#9333EA", hover_color="#7E22CE", command=open_customer).pack(pady=10)

ctk.CTkButton( main_frame, text="Bill History", font = ("Segoe UI", 17, "bold"), width= 300, height= 48, cursor="hand2", fg_color="#EA580C", hover_color="#C2410C", command=open_history).pack(pady=10)



footer_label = ctk.CTkLabel( app, text="© DMM Management System", font=("Segoe UI", 12), text_color="#6B7280")
footer_label.pack(side="bottom", pady=10)

app.mainloop()
