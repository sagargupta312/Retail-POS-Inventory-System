# DMM Management System

A desktop-based **Retail POS, Inventory, and Customer Management System** built using **Python, CustomTkinter, and MySQL**.

This project simulates a real-world shop workflow including billing, stock management, customer tracking, and bill history. It was developed during my **first semester** to understand how GUI applications, databases, and business logic work together.

---

## Features

* **Inventory Management** – Add, update, delete products with real-time stock tracking
* **Billing / POS** – Auto-fill products, validate stock, calculate discounts, keyboard shortcuts
* **Customer Management** – Auto-create customers, track total spend and last visit
* **Bill History** – Search bills by date, bill ID, or customer with total sales summary

---

## Tech Stack

* **Language:** Python
* **GUI:** CustomTkinter, Tkinter (Treeview)
* **Database:** MySQL
* **Architecture:** Modular (UI and DB logic separated)

---

## How to Run the Program

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/DMM-Management-System.git
   cd DMM-Management-System
   ```

2. Install required Python packages

   ```bash
   pip install -r requirements.txt
   ```

3. Install and start MySQL server

4. Create the database and tables:

   ```sql
   SOURCE database/schema.sql;
   ```

5. Update MySQL credentials in the DB config files (host, user, password)

6. Run the application:

   ```bash
   python login_gui.py
   ```

---

## Database Setup

The database schema is provided in:

```
/database/schema.sql
```

Run it in MySQL before starting the application.

---

## Screenshots

> Screenshots of major application flows are shown below.

### Login Screen

<img width="1120" height="780" alt="Screenshot 2026-01-29 115833" src="https://github.com/user-attachments/assets/7326bfe9-81f8-496b-8d4a-2bfb32a377ce" />


### Home Dashboard

<img width="1122" height="783" alt="Screenshot 2026-01-29 115853" src="https://github.com/user-attachments/assets/9c262487-ad0c-433b-8b04-378b980c4c85" />


### Inventory Management
<img width="1492" height="786" alt="Screenshot 2026-01-29 120900" src="https://github.com/user-attachments/assets/74361032-519b-462c-8885-74abc0699720" />

###  Billing / POS

<img width="1632" height="809" alt="Screenshot 2026-01-29 121023" src="https://github.com/user-attachments/assets/a847c621-ee15-4631-82bd-2bea11d372f4" />

###  Save Bill
<img width="969" height="676" alt="Screenshot 2026-01-29 121214" src="https://github.com/user-attachments/assets/29caba95-9b0d-4471-8ff4-018936508911" />

###  Customer Management

<img width="1113" height="680" alt="Screenshot 2026-01-29 121345" src="https://github.com/user-attachments/assets/caf7bf90-cdc7-4129-98d7-fea75c806f64" />

###  Bill History


---<img width="1364" height="842" alt="Screenshot 2026-01-29 121413" src="https://github.com/user-attachments/assets/a2e94622-e044-4080-bf17-3f5138841105" />


##  How the System Works (Short)

1. **Login** – User logs in to access the dashboard.
2. **Inventory Setup** – Products are added with price, MRP, quantity, category, and distributor.
3. **Billing Process** – Enter Product ID to auto-fill details, add items to the bill, and calculate totals.
4. **Stock Update** – Product stock is automatically reduced after saving a bill.
5. **Customer Tracking** – Customer is identified using phone number and total purchase is updated.
6. **Bill Storage** – Bill and bill items are saved in the database.
7. **History & Reports** – Bills can be searched by date, bill ID, or customer, with total sales shown.

md

<img width="1635" height="807" alt="Screenshot 2026-01-29 121446" src="https://github.com/user-attachments/assets/e22877b3-2344-4d03-be2c-9aa0a1732aff" />



# Use of AI Assistance


AI tools (ChatGPT) were used as a **development assistant**, mainly for:
- UI layout ideas (button placement, spacing)
- Improving code readability
- Debugging small issues




---


⚠️ Known Limitations


- No role-based authentication
- No transaction rollback handling
- Desktop-only application


---

> This project represents my learning journey and is intended to evolve over time.

**Note:** *DMM* refers to **D Mega Mart**, a retail store used as the context for this project.  
Reference link: https://share.google/mhjDfRAQyUuNqbT6c

