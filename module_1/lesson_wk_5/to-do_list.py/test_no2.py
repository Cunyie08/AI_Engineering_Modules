import csv
from pathlib import Path
from datetime import datetime
import random

workspace = Path("newfile")
workspace.mkdir(exist_ok=True)
file_path = workspace/ "expenses.txt"
file_path

fieldnames = ["Date", "Category", "Amount", "Item", "Product ID"]

# Define a csv_file that collects details of the store
def save_expenses(file_path, expenses):
    if type(expenses) == dict:
        expenses = [expenses]
        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerows(expenses)
            print("Expenses added successfully")

    else:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
    print("Expenses stored in csv successfully.")


def load_expenses():
    with open(file_path, "r", encoding="utf-8")as f:
        load_expenses = csv.reader(f)

        for row_number, row in enumerate(load_expenses):
            if row_number == 0:
                print(f"Headers: {"|".join(row)}")
                print("-"*40)
            else:
                date, category, amount, item = row
                print(f"{date}\t{category}\t{amount}\t{item}")

# Function to delete a task from the list
def product_id():
    import random
    return f"Product ID:{random.randint(1000, 9999)}"






def main():
    while True:
        print("Welcome to NCC store")
        print("1. Add expenses")
        print("2. View expenses")
        print("3. Delete expenses")
        print("4. Exit program")

        
        try:
            choice = input("Please enter a selection: ")
            date = datetime.today().strftime("%Y-%m-%d")
            Product_id = product_id()
            if choice == '1':
                category = input("Enter the category of the item: ")
                amount = float(input("Please enter the amount: "))
                item = input("Enter the description of the item: ")
                expenses = {"Date": date, "Category": category, "Amount": amount, "Item": item, "Product ID": Product_id}
                save_expenses(file_path, expenses)
            elif choice =='2':
                print("These are your recorded expenses")
                load_expenses()
            elif choice == '3':
                delete_exp = input("Enter the product to delete: ")
                try:
                    with open(file_path, "r", encoding="utf-8")as f:
                        rows = f.readlines()
                    updated_row = [row for row in rows if delete_exp not in row]
                    if len(updated_row) == len(rows):
                        print(f"{delete_exp} not found in file")
                    else:
                        with open(file_path, "w", encoding="utf=-8")as f:
                            f.writelines(updated_row)
                            print(f"{delete_exp} has been removed")
                except FileNotFoundError:
                    print("Expenses not yet found!")

                    # for delete_exp in file_path:
                #     file_path.remove(delete_exp)
                #     print(f"{delete_exp} has been removed")
                # else:
                #     print('Activity not found!')
            elif choice =='4':
                break
            else:
                raise ValueError("You have entered an invalid option")
            update_expenses = input("Do you want to perform another operation? yes or no: ").lower().strip()
            if update_expenses == 'yes':
                continue
            else:

                print("You have exited the program")
                break
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
                