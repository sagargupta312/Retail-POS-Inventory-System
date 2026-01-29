import customtkinter as ctk
import time
from datetime import datetime
from tkinter import messagebox
import bill_save_db


def open_window(bill_items,aa):
    ctk.set_appearance_mode("light")

    app = ctk.CTk()
    app.geometry("780x520")
    app.title("Save Bill")
    app.configure(fg_color="#F1F5F9")
    app.resizable(False, False)

    # big box
    card = ctk.CTkFrame(app, width=680, height=420, fg_color="white", corner_radius=16)
    card.place(relx=0.5, rely=0.5, anchor="center")

    # title
    ctk.CTkLabel(card, text="Finalize Bill", font=("Segoe UI", 26, "bold")).place(x=250, y=20)
    ctk.CTkLabel(card, text="Fill details and save bill", font=("Segoe UI", 14), text_color="#64748B").place(x=235, y=60)

    # phone
    ctk.CTkLabel(card, text="Phone Number", font=("Segoe UI", 15, "bold")).place(x=60, y=110)
    phone_entry = ctk.CTkEntry(card, width=260, height=38)
    phone_entry.place(x=340, y=105)



    # bill id
    if aa == "":
        bill_id = f"dmm{int(time.time())}"
        ctk.CTkLabel(card, text="Bill ID", font=("Segoe UI", 15, "bold")).place(x=60, y=160)
        bill_entry = ctk.CTkEntry(card, width=260, height=38, state="disabled")
        bill_entry.place(x=340, y=155)
        bill_entry.configure(state="normal")
        bill_entry.insert(0, bill_id)
        bill_entry.configure(state="disabled")
    else:
        bill_id = aa
        ctk.CTkLabel(card, text="Bill ID", font=("Segoe UI", 15, "bold")).place(x=60, y=160)
        bill_entry = ctk.CTkEntry(card, width=260, height=38, state="disabled")
        bill_entry.place(x=340, y=155)
        bill_entry.configure(state="normal")
        bill_entry.insert(0, bill_id)
        bill_entry.configure(state="disabled")

    # payment type
    ctk.CTkLabel(card, text="Payment Type", font=("Segoe UI", 15, "bold")).place(x=60, y=210)

    payment_var = ctk.StringVar(value="")

    cash_cb = ctk.CTkCheckBox(card, text="Cash", variable=payment_var, onvalue="cash", offvalue="")
    online_cb = ctk.CTkCheckBox(card, text="Online", variable=payment_var, onvalue="online", offvalue="")
    card_cb = ctk.CTkCheckBox(card, text="Card", variable=payment_var, onvalue="card", offvalue="")

    cash_cb.place(x=340, y=210)
    online_cb.place(x=420, y=210)
    card_cb.place(x=520, y=210)

    # cash received
    ctk.CTkLabel(card, text="Cash Received", font=("Segoe UI", 15, "bold")).place(x=60, y=260)
    cash_entry = ctk.CTkEntry(card, width=260, height=38, state="disabled")
    cash_entry.place(x=340, y=255)

    # change to give
    ctk.CTkLabel(card, text="Change to Give", font=("Segoe UI", 15, "bold")).place(x=60, y=310)
    change_entry = ctk.CTkEntry(card, width=260, height=38, state="disabled")
    change_entry.place(x=340, y=305)

    # enable cash fields only for cash
    def payment_changed():
        if payment_var.get() == "cash":
            cash_entry.configure(state="normal")
        else:
            cash_entry.delete(0, "end")
            change_entry.delete(0, "end")
            cash_entry.configure(state="disabled")
            change_entry.configure(state="disabled")

    cash_cb.configure(command=payment_changed)
    online_cb.configure(command=payment_changed)
    card_cb.configure(command=payment_changed)

    # enter key flow
    phone_entry.bind("<Return>", lambda e: cash_entry.focus())

    def calculate_change():
        if payment_var.get() != "cash":
            return

        if not cash_entry.get().isdigit():
            messagebox.showerror("Error", "Cash must be number")
            return

        total = sum(float(i[6]) for i in bill_items)
        cash = float(cash_entry.get())

        if cash < total:
            messagebox.showerror("Error", "Cash is less")
            return

        change = cash - total
        change_entry.configure(state="normal")
        change_entry.delete(0, "end")
        change_entry.insert(0, f"{change:.2f}")
        change_entry.configure(state="disabled")

    cash_entry.bind("<Return>", lambda e: calculate_change())

    # save logic
    def ssave():
        if payment_var.get() == "":
            messagebox.showerror("Error", "Select payment type")
            return

        if payment_var.get() == "cash" and cash_entry.get() == "":
            messagebox.showerror("Error", "Enter cash")
            return

        total_mrp_amount = 0
        total_selling_amount = 0
        total_discount = 0

        for i in bill_items:
            product_id, _, quantity, mrp, _, discount, item_total = i

            bill_save_db.reduce_stock(product_id, int(quantity))

            total_mrp_amount += int(quantity) * float(mrp)
            total_selling_amount += float(item_total)
            total_discount += float(discount) * int(quantity)

            bill_save_db.save_bill_item(*([bill_id] + list(i)))

        phone = phone_entry.get()
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone looks wrong")
            return

        bill_save_db.get_customer(int(phone), int(total_selling_amount))
        bill_save_db.sav_bill(bill_id, datetime.now(), total_mrp_amount, total_discount, total_selling_amount,phone_entry.get())

        messagebox.showinfo("Done", "Bill saved")
        app.destroy()

    # save button
    ctk.CTkButton(card,text="Save Bill", width=220, height=42,font=("Segoe UI", 18, "bold"),command=ssave ).place(relx=0.5, y=380, anchor="center")

    app.after(200, phone_entry.focus)
    app.mainloop()
