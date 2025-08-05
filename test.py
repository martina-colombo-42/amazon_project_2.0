import re
import time

user_info = {
    "username": "Larka",
    "password": "FenrirLoves99Bats!",
    "phone_number": ""
}

items = {
    "date": "",
    "item": "",
    "total": "",
    "weight": "",
    "quantity": ""
}

def user_options():
    choices = True
    while choices == True:
        print("What would you like to do?")
        choice = input("1. Enter a purchase\n2. Generate a report\n3. Quit")
        if choice == 1:
            items["date"] = input("Enter the date of the purchase (YYYY/MM/DD): ")
            items["item"] = input("Enter the item purchased (at least 3 characters): ")
            cost = float(input("Enter the cost of the item in Euro: "))
            items["weight"] = float(input("Enter the weight of the item in kg: "))
            items["quantity"] = int(input("Enter the quantity purchased: "))
            items["total"] = cost * items["weight"] * items["quantity"]
        elif choice == 2:
            print("Generating report...")
            time.sleep(2)
            print(" "*24,"-"*29)
            print(" "*24,"|   Amazon Expense Report   |")
            print(" "*24,"-"*29)

        elif choice == 3:
            print(f"Thank you for your visit, {user_info["username"]}. Goodbye!")
            choices = False
        else:
            return "The operation selected is not valid: please choose from the available options"

user_options()