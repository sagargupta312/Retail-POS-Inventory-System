import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("DMM MANAGEMENT APP")
app.configure(fg_color="#F8FAFC")


top_frame = ctk.CTkFrame(app, height=70, fg_color="#F8FAFC", corner_radius=0)
top_frame.pack(fill="x")

title_label = ctk.CTkLabel(
    top_frame,
    text="D MEGA MART",
    font=("Segoe UI", 30, "bold"),
    text_color="#000000"
)
title_label.pack(pady=15)


blue_frame = ctk.CTkFrame(app, height=55, fg_color="#1E40AF", corner_radius=0)
blue_frame.pack(fill="x")

login_text = ctk.CTkLabel(
    blue_frame,
    text="Secure Login",
    font=("Segoe UI", 18, "bold"),
    text_color="white"
)
login_text.pack(pady=12)


card = ctk.CTkFrame(
    app,
    width=420,
    height=320,
    fg_color="#D2EBFF",
    corner_radius=20
)
card.place(relx=0.5, rely=0.58, anchor="center")
card.pack_propagate(False)

heading = ctk.CTkLabel(
    card,
    text="Welcome Back 👋",
    font=("Segoe UI", 26, "bold"),
    text_color="#1F2937"
)
heading.pack(pady=(30, 5))

subheading = ctk.CTkLabel(
    card,
    text="Login to continue",
    font=("Segoe UI", 16),
    text_color="#374151"
)
subheading.pack(pady=(0, 25))


login_id = ctk.CTkEntry( card,   placeholder_text="User ID",   width=260,   height=40,   font=("Segoe UI", 15))
login_id.pack(pady=10)

password = ctk.CTkEntry( card, placeholder_text="Password", show="*", width=260,   height=40,   font=("Segoe UI", 15))
password.pack(pady=10)


def submit():
    if login_id.get() == "" or password.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif login_id.get() == "sagar" and password.get() == "1234":
        messagebox.showinfo("Success", "Login successful")
        app.destroy()
        import home_page   # go to home dashboard
    else:
        messagebox.showerror("Error", "Wrong ID or Password")


login_btn = ctk.CTkButton( card,text="Login", font=("Segoe UI", 16, "bold"), width=200, height=42, fg_color="#2563EB", hover_color="#1D4ED8", cursor="hand2", command=submit)
login_btn.pack(pady=10)


footer = ctk.CTkLabel(app, text="© DMM Management System", font=("Segoe UI", 12), text_color="#6B7280")
footer.pack(side="bottom", pady=10)


password.bind("<Return>", lambda e: submit())
login_id.bind("<Return>", lambda e: password.focus())

app.mainloop()
