import re, json, os
from datetime import time, datetime
###JSON FILES FUNCTIONS

DATA_FILE = "user_data.json"

users = {}

def load_data():
    global users
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

##########

#############################start of functions

def registration():
    check_password = False
    pattern_password = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,20}"
    print("*"*25)
    print("*** Welcome to Amazon ***")
    print("*"*25)
    print("")
    username = input("Enter your username (no spaces): ").strip()
    users["username"] = username
    while check_password == False:
        password = input("Enter your password (no spaces): ").strip()
        if re.search(pattern_password,password):
            check_password = True
            users["password"] = password
            save_data()
            print("Valid password! Wait...")
            time.sleep(2)
            print("")
            print("-"*28)
            print("| Registration successful! |")
            print("-"*28)
            return ""
        else:
            print("Sorry, invalid password!\nIt must have:\n*At least one number\n*One uppercase and one lowercase\n*One special symbol\n*Between 6 and 20 characters\nTry again!")
#the function saves the username after the input, and it also saves the password after checking if it is valid
    
def phone_number_checker():
    phone = False
    pattern_phone = r"^(\+49)[0-9]{8,12}$"
    while phone == False:
        phone_number = input("Enter phone number to continue (it must start with +49, no spaces): ").strip()
        if re.search(pattern_phone,phone_number):
            phone = True
            users["phone_number"] = phone_number
            users["items"] = {}
            save_data()
            return "Valid phone number!" 
        else:
            print("Invalid number... please try again")
#the function saves the phone number after the input, if it is valid

def log_in():
    attempts = 2
    try_name = False
    print("")
    print("-"*10)
    print("| Log In |")
    print("-"*10)
    print("")
    while try_name == False:
        username_log = input("Write your username: ").strip()
        if username_log != users["username"]:
            print("Wrong username, try again!")
        else:
            try_name = True
            password_log = input("Write your password: ").strip()
            while attempts >= 0:
                if attempts == 0:
                    print("You are out of guesses! Wait 5 seconds...")
                    time.sleep(5)
                    password_log = input("Write your password: ").strip()
                    if password_log != users["password"]:
                        print("Wrong again! Sorry, you have to register again")
                        break
                    else:
                        print("")
                        print("*"*43)
                        print("*** Welcome to Amazon Expenses Tracker! ***")
                        print("*"*43)
                        return ""
                elif password_log == users["password"]:
                    print("")
                    print("*"*43)
                    print("*** Welcome to Amazon Expenses Tracker! ***")
                    print("*"*43)
                    return ""
                else:
                    attempts -= 1
                    print("Wrong... try again")
                    password_log = input("Write your password: ").strip()
#let the user login with the credential they just used to register themselves

def user_options():
    choices = True
    while choices == True:
        new_key = "item"+str(len(users["items"])+1)
        new_item = {}
        print("-"*60)
        print("What would you like to do?")
        choice = input("1. Enter a purchase\n2. Generate a report\n3. Quit\nYour choice: ").strip()
        if choice == "1":
            try_date = False
            try_name = False
            try_cost = False
            try_weight = False
            try_quantity = False
            while try_date == False:
                try:
                    new_date = input("Enter the date of the purchase (YYYY/MM/DD): ").strip()
                    formatted_date = datetime.strptime(new_date, "%Y/%m/%d").date()
                    if formatted_date <= datetime.now().date():
                        new_item["date"] = new_date
                        try_date = True
                    else:
                        print("The date cannot be in the future. Try again!")
                except ValueError:
                    print("Invalid date format. Try again!")
            while try_name == False:
                new_name = input("Enter the item purchased (at least 3 characters): ").strip()
                if len(new_name) >= 3:
                    new_item["name"] = new_name
                    try_name = True
                else:
                    print("The name is too short. Try again!")
            while try_cost == False:
                try:
                    new_cost = float(input("Enter the cost of the item in Euro: "))
                    new_item["cost"] = new_cost
                    try_cost = True
                except ValueError:
                    print("That's not a number. Try again!")
            while try_weight == False:
                try:
                    new_weight = float(input("Enter the weight of the item in kg: "))
                    new_item["weight"] = new_weight
                    try_weight = True
                except (ValueError):
                    print("That's not a number. Try again!")
            while try_quantity == False:
                try:
                    new_quantity = int(input("Enter the quantity purchased (1 or more): "))
                    if new_quantity >= 1:
                        new_item["quantity"] = new_quantity
                        try_quantity = True
                    else:
                        print("Quantity must be at least 1.")
                except ValueError:
                    print("Invalid value. Try again!")
            users["items"][new_key] = new_item
            save_data()
        elif choice == "2":
            print("Generating report...")
            time.sleep(2)
            print(" "*24,"-"*29)
            print(" "*24,"|   Amazon Expense Report   |")
            print(" "*24,"-"*29)
            print("")
            print("-"*60)
            print("")
            if not users["items"]:
                print("Sorry, no items registered yet")
                print("")
            else:
                print(" "*15,"-"*29)
                print(" "*15,"|   Amazon Expense Report   |")
                print(" "*15,"-"*29)
                print(f"name: {users["username"]}"," "*4,
                    "password: ***"," "*4,
                    "Tel: +49***"+users["phone_number"][-2:])
                print(f"Date:", datetime.datetime.today().date())
                print("-"*60)
                print("DELIVERY CHARGES", " "*6, "TOTAL ITEM COST")
                total_delivery_cost = sum(item["weight"] for item in users["items"].values())
                total_items_cost = sum(item["cost"] for item in users["items"].values())
                print(" "*2, f"{total_delivery_cost:.2f}", "EURO", " "*13, f"{total_items_cost:.2f}", "EURO")
                print("")
                print("MOST EXPENSIVE", " "*6, "LEAST EXPENSIVE")
                most_expensive_item = max(users["items"].values(), key=lambda item : item["cost"])
                name_most_expensive = most_expensive_item["name"]
                least_expensive_item = min(users["items"].values(), key=lambda item : item["cost"])
                name_least_expensive = least_expensive_item["name"]
                print(" "*2, name_most_expensive, " "* 17, name_least_expensive)
                print(" "*2, f"cost: {most_expensive_item["cost"]:.2f}"," "*10, f"cost: {least_expensive_item["cost"]:.2f}")
                print("")
                average_cost_item = (sum(item["cost"] for item in users["items"].values())) / len(users["items"])
                print(f"AVERAGE COST OF ITEM PER ORDER: {average_cost_item:.2f} EURO")
                print("PURCHASE DATE RANGE: ")
                print("-"*10)
                if (total_delivery_cost + total_items_cost) <= 500:
                    print("Note: You have not exceeded the spending limit of 500 EURO")
                else:
                    print("Note: You have exceeded the spending limit of 500 EURO")
        elif choice == "3":
            print("Quitting program...")
            time.sleep(2)
            choices = False
            print(f"Thank you for your visit, {users["username"]}. Goodbye!")
        else:
            print("")
            print("The operation selected is not valid: please choose from the available options.")
            print("")
#let the user choose between adding items, printing a report, or quitting the program

#############################end of functions

def main ():
    load_data()
    print(registration())
    print(phone_number_checker())
    print(log_in())
    user_options()


main()