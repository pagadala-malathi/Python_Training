staff_records = []

def add_staff():
    nm = input("Name: ")
    ag = int(input("Age: "))
    rl = input("Role: ")
    sal = int(input("Salary: "))
    staff_records.append({"name": nm, "age": ag, "role": rl, "salary": sal})
    print("Employee added!\n")

def update_staff():
    target = input("Enter name to update: ")
    for rec in staff_records:
        if rec["name"] == target:
            rec["age"] = int(input("New age: "))
            rec["role"] = input("New role: ")
            rec["salary"] = int(input("New salary: "))
            print("Updated!\n")
            return
    print("Employee not found!\n")

def delete_staff():
    target = input("Enter name to delete: ")
    global staff_records
    staff_records = [rec for rec in staff_records if rec["name"] != target]
    print("Deleted (if existed)\n")

def display_staff():
    if not staff_records:
        print("No records\n")
    else:
        for rec in staff_records:
            print(rec)
        print()

while True:
    print("1. Add\n2. Update\n3. Delete\n4. Display\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_staff()
    elif choice == "2":
        update_staff()
    elif choice == "3":
        delete_staff()
    elif choice == "4":
        display_staff()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")


def student_report():
    stu_name = input("Student Name: ")
    m1 = int(input("Subject 1: "))
    m2 = int(input("Subject 2: "))
    m3 = int(input("Subject 3: "))

    total_marks = m1 + m2 + m3
    avg_marks = total_marks / 3

    if avg_marks >= 90:
        grd = "A"
    elif avg_marks >= 75:
        grd = "B"
    elif avg_marks >= 50:
        grd = "C"
    else:
        grd = "Fail"

    print(f"\nReport Card\nName: {stu_name}\nTotal: {total_marks}\nAverage: {avg_marks:.2f}\nGrade: {grd}")
student_report()

cart_bucket = []

def add_product():
    pname = input("Product: ")
    prc = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart_bucket.append({"item": pname, "price": prc, "qty": qty})
    print("Item added!\n")

def remove_product():
    pname = input("Remove item: ")
    global cart_bucket
    cart_bucket = [p for p in cart_bucket if p["item"] != pname]
    print("Item removed (if existed)\n")

def show_cart():
    if not cart_bucket:
        print("Cart is empty\n")
        return

    total_bill = 0
    for p in cart_bucket:
        cost = p["price"] * p["qty"]
        total_bill += cost
        print(f"{p['item']} - {p['qty']} x {p['price']} = {cost}")
    print("Total:", total_bill, "\n")


while True:
    print("1. Add Product\n2. Remove Product\n3. Show Cart\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        show_cart()
    elif choice == "4":
        break
    else:
        print("Invalid choice\n")


visitor_set = set()

def add_visitor():
    vname = input("Enter visitor name: ")
    visitor_set.add(vname)
    print("Visitor added!\n")

def show_visitors():
    print("\nTotal Unique Visitors:", len(visitor_set))
    print("Visitors:", visitor_set, "\n")

while True:
    print("1. Add Visitor")
    print("2. Show Visitors")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_visitor()
    elif choice == "2":
        show_visitors()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")

user_db = {"admin": "1234", "user": "abcd"}

def login_check():
    uname = input("Username: ")
    pwd = input("Password: ")

    if uname in user_db and user_db[uname] == pwd:
        print("Login Successful\n")
    else:
        print("Invalid Credentials\n")

while True:
    print("1. Login")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        login_check()
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")

def format_tool():
    person_nm = input("Enter your name: ")
    product_nm = input("Enter product: ")

    print(f"\n{person_nm} purchased {product_nm}\n")

    print("Left aligned : ", person_nm.ljust(20, "-"))
    print("Right aligned: ", person_nm.rjust(20, "-"))
    print("Center aligned:", person_nm.center(20, "-"))

format_tool()

bank_info = {"holder": "", "balance": 0}

def create_account():
    bank_info["holder"] = input("Enter name: ")
    bank_info["balance"] = float(input("Enter initial balance: "))
    print("Account created!\n")

def deposit_money():
    amt_add = float(input("Enter deposit amount: "))
    bank_info["balance"] += amt_add
    print("Money deposited!\n")

def withdraw_money():
    amt_sub = float(input("Enter withdraw amount: "))
    if amt_sub <= bank_info["balance"]:
        bank_info["balance"] -= amt_sub
        print("Money withdrawn!\n")
    else:
        print("Insufficient balance!\n")

def check_balance():
    print("Current Balance:", bank_info["balance"], "\n")


while True:
    print("1.Create\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Exit")
    opt = input("Choose: ")

    if opt == "1":
        create_account()
    elif opt == "2":
        deposit_money()
    elif opt == "3":
        withdraw_money()
    elif opt == "4":
        check_balance()
    elif opt == "5":
        break
    else:
        print("Invalid choice\n")


vote_data = {"A": 0, "B": 0, "C": 0}

def cast_vote():
    choice = input("Vote (A/B/C): ").upper()
    if choice in vote_data:
        vote_data[choice] += 1
        print("Vote added!\n")
    else:
        print("Invalid candidate!\n")

def show_result():
    print("\nVotes:", vote_data)
    winner = max(vote_data, key=vote_data.get)
    print("Winner:", winner, "\n")

while True:
    print("1.Vote\n2.Result\n3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        cast_vote()
    elif ch == "2":
        show_result()
    elif ch == "3":
        break
    else:
        print("Invalid choice\n")

student_data = {}

def add_student():
    stu_nm = input("Student name: ")
    course_list = input("Enter courses (comma separated): ").split(",")
    student_data[stu_nm] = course_list
    print("Student added!\n")

def update_student():
    stu_nm = input("Enter student name: ")
    if stu_nm in student_data:
        course_list = input("Enter new courses: ").split(",")
        student_data[stu_nm] = course_list
        print("Updated!\n")
    else:
        print("Student not found!\n")

def display_students():
    for k, v in student_data.items():
        print(k, "->", v)
    print()


while True:
    print("1.Add\n2.Update\n3.Display\n4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        update_student()
    elif ch == "3":
        display_students()
    elif ch == "4":
        break
    else:
        print("Invalid choice\n")

def number_tool():
    num_val = int(input("Enter number: "))

    print("Binary:", bin(num_val))
    print("Octal :", oct(num_val))
    print("Hex   :", hex(num_val))

    print("With commas:", f"{num_val:,}")
    print("Scientific :", f"{num_val:.2e}")

number_tool()
