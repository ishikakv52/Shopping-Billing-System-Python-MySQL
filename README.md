# Shopping-Billing-System-Python-MySQL
A console-based shopping and billing system developed using Python and MySQL that calculates total bill, applies discounts, generates invoice files, and stores order details in a database.




# Shopping Billing System using Python & MySQL

A console-based Shopping and Billing System developed using **Python** and **MySQL**.  
This project allows users to purchase products, calculate total cost, apply discounts, generate invoice files, and store order details in a database.

---

## 🚀 Features
- Menu-driven shopping system
- Multiple product selection (Laptop, Mobile, Earbuds)
- Quantity selection and item removal
- Automatic total bill calculation
- Discount application based on bill amount
- Invoice generation in `.txt` format
- Order data storage in MySQL database
- Timestamped order records

---

## 🛠 Technologies Used
- Python
- MySQL
- mysql-connector-python
- File Handling
- datetime module

---

## 🔄 Workflow
1. User selects products and quantity
2. System calculates item-wise and total amount
3. Discount is applied based on total bill
4. Invoice is generated as a text file
5. Order details are saved into MySQL database

---

## 📦 Products Available
| Product | Price |
|-------|-------|
| Laptop | ₹100000 |
| Mobile | ₹15000 |
| Earbuds | ₹5000 |

---

## 💰 Discount Rules
- Above ₹10,000 → 20% discount
- Above ₹5,000 → 10% discount
- Otherwise → No discount

---

## ▶️ How to Run the Project

### 1️⃣ Install dependency
```bash
pip install mysql-connector-python
2️⃣ Setup MySQL Database

Create a database and table:

CREATE TABLE orders (
    order_id INT,
    customer_name VARCHAR(50),
    total_amount FLOAT,
    discount FLOAT,
    payable_amount FLOAT,
    order_time DATETIME
);
3️⃣ Update Database Credentials
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="YOUR_DATABASE"

4️⃣ Run the program
python shopping_billing.py
