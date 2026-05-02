import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="student",
    password="Vasu@2004" 
)
conn=db.cursor()
class register:
    def __init__(self,n,a,c):
        query="""create table if not exists student_1(
        id int primary key auto_increment,
        name varchar(50) not null,
        age int not null,
        course varchar(70)not null,
        password varchar(50) not null)"""
        conn.execute(query)
        p=input("Enter the paswword here:---")
        cp=input("Enter the confirm password here:---")
        if p == cp:
            q="insert into student_1(name,age,course,password) values (%s,%s,%s,%s)"
            d=(n,a,c,p)  
            conn.execute(q,d)
            db.commit() 
            print("the student register successfully")
class Delete:
    def __init__(self, n):
        q = "DELETE FROM student_1 WHERE name=%s"
        d = (n,)

        conn.execute(q, d)
        db.commit()

        if conn.rowcount > 0:
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")
class update:
    def __init__(self, n, a, p, i):
        q = "UPDATE student_1 SET name=%s, age=%s, password=%s WHERE id=%s"
        d = (n, a, p, i)

        conn.execute(q, d)
        db.commit()

        if conn.rowcount > 0:
            print("Student Updated Successfully")
        else:
            print("Student Not Found")
class insert:
    def __init__(self,n,a,c,p):
        q="insert into student_1(name,age,course,password) values(%s,%s,%s,%s)"
        d=(n,a,c,p)
        conn.execute(q,d)
        db.commit()
        if conn.rowcount > 0:
            print("student insert successfully")
        else:
            print("not provide valid info")

class dashboard:
    def __init__(self,i):
        print("dashboard")
        print(i,"successfully login by student")
        while True:
            print("------------change the credanals-----------")
            print("1.delete")
            print("2.update")
            print("3.insert")
            print("4.exit")
            o=int(input("choose the above options:--"))
            if o == 1:
                name=input("Enter the name of student:--")
                Delete(name)

                print("sucessfully delete")
            elif o == 2:
               id = int(input("Enter Student id: "))
               name = input("Enter New Name: ")
               age = int(input("Enter New Age: "))
               password = input("Enter New Password: ")

               update(name, age, password, id)
            elif o == 3:
               name = input("Enter New Name: ")
               age = int(input("Enter New Age: "))
               course= input("Enter New course: ")
               password=input("ENter the password of person:--")
               insert(name,age,course,password)
            elif o == 4:
                print("exit from the student dashboard")
                break
class login:
    def __init__(self,n,p):
        q="select * from student_1 where name = %s and password = %s"
        v=(name,password)
        conn.execute(q,v)
        abc=conn.fetchall()
        for i in abc:
            if name == n and password == p:
                dashboard(i)
            else:
                print("not founded")


while True:
  print("______________welcome to the students ____________________")
  print("1.register")
  print("2.login")
  
  o=int(input("Enter the option :--"))
  if o == 1:
      id=int(input("Enter the id of student:--"))
      name=input("enter name of student:---")
      age=int(input("Enter the age of the person:--"))
      course=input("Enter the course of the student:--")
      o=register(name,age,course)
  elif o == 2:
      name=input("Enter the name of the student:--")
      password=input("Enter the password:--")
      o=login(name,password)
