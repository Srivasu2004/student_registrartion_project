# 🎓 Student Management System (Python + MySQL)

A simple **Student Management System** built using **Python (OOP Concepts)** and **MySQL Database Connectivity (mysql.connector)**.
This project allows students to **register, login, update details, insert new records, and delete records** using a command-line interface.

---

## 📌 Features

✅ Student Registration
✅ Student Login Authentication
✅ Add New Student Records
✅ Update Existing Student Details
✅ Delete Student Records
✅ MySQL Database Integration
✅ Object-Oriented Programming Structure

---

## 🛠️ Technologies Used

* **Python 3.x**
* **MySQL**
* **mysql.connector**
* **OOP Concepts**

---

## 📂 Project Structure

```bash
student_management/
│── main.py
│── README.md
```

---

## 🗄️ Database Configuration

Before running the project, create a MySQL database:

```sql
CREATE DATABASE student;
```

Update your database credentials inside Python file:

```python
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="student",
    password="your_password"
)
```

---

## 🧾 Table Structure

The project automatically creates the table:

```sql
student_1
```

### Columns:

| Column Name | Data Type                         |
| ----------- | --------------------------------- |
| id          | INT (Primary Key, Auto Increment) |
| name        | VARCHAR(50)                       |
| age         | INT                               |
| course      | VARCHAR(70)                       |
| password    | VARCHAR(50)                       |

---

## ▶️ How to Run

### Step 1: Install MySQL Connector

```bash
pip install mysql-connector-python
```

### Step 2: Run Python File

```bash
python main.py
```

---

## 💻 Menu Options

```text
1. Register
2. Login
```

### After Login Dashboard

```text
1. Delete Student
2. Update Student
3. Insert Student
4. Exit
```

---

## 🔐 Registration Flow

* Enter Name
* Enter Age
* Enter Course
* Set Password
* Confirm Password

If passwords match → Student registered successfully.

---

## 🔓 Login Flow

Enter:

* Student Name
* Password

If valid credentials match database → Dashboard opens.

---

## 📷 Sample Output

```text
______________welcome to the students ____________________

1.register
2.login

Enter the option :-- 1
Enter name of student:--- Vasu
Enter age: 22
Enter course: Python
Enter password
Confirm password

Student registered successfully
```

---

## 🧠 OOP Classes Used

| Class Name | Purpose              |
| ---------- | -------------------- |
| register   | Student Registration |
| login      | Student Login        |
| dashboard  | Menu After Login     |
| Delete     | Delete Student       |
| update     | Update Student       |
| insert     | Insert Student       |

---

## ⚠️ Improvements Recommended

Current code works, but can be enhanced with:

✅ Exception Handling
✅ Password Encryption
✅ Proper Login Validation
✅ Search Student Option
✅ View All Students
✅ Better UI using Tkinter / Streamlit
✅ Role-based Admin Login

---

## 🐞 Known Issues in Current Code

* Variable mismatch inside login class (`name`, `password`)
* No logout option
* Plain text password storage
* No duplicate user validation

---

## 🚀 Future Enhancements

* GUI Version using Tkinter
* Web App using Flask / Django
* Streamlit Dashboard
* Student Marks Management
* Attendance Module

---

## 👨‍💻 Author

Developed using **Python + MySQL** for learning **PDBC + OOP Concepts**.

---

## 📜 License

Free to use for educational purposes.

---

