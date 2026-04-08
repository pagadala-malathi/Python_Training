from database import Database
from models.user import User
from models.expense import Expense
from utils.calculators import *

db = Database()

def main():
    while True:
        print("\n===== Smart Expense Manager =====")
        print("1. Add User")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            user = User(db, name)
            user_id = user.save()
            print("User created with ID:", user_id)

        elif choice == "2":
            user_id = int(input("User ID: "))
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")

            exp = Expense(db, user_id, amount, category, desc, date)
            exp.save()
            print("Expense added!")

        elif choice == "3":
            user_id = int(input("User ID: "))
            expenses = db.get_expenses(user_id)

            print("\nAll Expenses:")
            for e in expenses:
                print(e)

            print("\nTotal:", calculate_total(expenses))

            print("\nCategory Wise:")
            cat_data = category_wise(expenses)
            print(cat_data)

            print("\nHighest Expense:")
            print(highest_expense(expenses))

            if "Food" in cat_data and cat_data["Food"] > 3000:
                print("⚠️ You are spending too much on Food!")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()