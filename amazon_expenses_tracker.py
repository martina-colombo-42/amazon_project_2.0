import re, json, os, time, sys
from datetime import datetime

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

##########COLOURS FOR TEXT
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
##########

#############################start of functions

current_user = None

def registration():
    global current_user
    check_password = False
    pattern_password = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{6,20}"
    username_unchecked = True
    #make the user choose a username
    while username_unchecked == True:
        username = input("Choose your username (no spaces): ").strip()
    #if the username doesn't exist, it is created
        if username not in users:
            users[username] = {}
            current_user = username
            username_unchecked = False
    #if the username exists, prompt for a different one
        else:
            #check if the user has already registered with that name
            existing = input(RED + "Sorry, the username is already taken. Is that you? (y/n): " + RESET).strip()
            #if yes, prompt to login
            if existing == "y":
                username_unchecked = False
                current_user = username
                return log_in()
            #if not, tell it to choose another username
            elif existing == "n":
                print("Please choose another username.")
            else:
                print("")
                print(RED + "The operation selected is not valid." + RESET)
                print("")
    while check_password == False:
        password = input("Choose your password (no spaces): ").strip()
        #checks if the password is valid
        if re.search(pattern_password,password):
            check_password = True
            #saves it
            users[current_user]["password"] = password
            save_data()
            print(GREEN + "Valid password! Wait..." + RESET)
            time.sleep(2)
            print("")
            print(CYAN + "-"*28)
            print("| Registration successful! |")
            print("-"*28 + RESET)
            #checks for a valid phone number
            return phone_number_checker()
        else:
            print(RED + "Sorry, invalid password!\nIt must have:\n*At least one number\n*One uppercase and one lowercase\n*One special symbol\n*Between 6 and 20 characters\nTry again!" + RESET)
#the function saves the username after the input, and it also saves the password after checking if it is valid
    
def phone_number_checker():
    global current_user
    phone = False
    pattern_phone = r"^(\+49)[0-9]{8,12}$"
    while phone == False:
        phone_number = input("Enter phone number to continue (it must start with +49, no spaces): ").strip()
        #checks if the phone number is valid
        if re.search(pattern_phone,phone_number):
            #if the phone number is valid, it saves it
            phone = True
            users[current_user]["phone_number"] = phone_number
            #and creates a subdictionary for the future items
            users[current_user]["items"] = {}
            save_data()
            print(GREEN + "Valid phone number!" + RESET)
            #when everything works, it promps to the login
            return log_in()
        else:
            print(RED + "Invalid number... please try again" + RESET)
#the function saves the phone number after the input, if it is valid

def log_in():
    global current_user
    attempts = 2
    try_name = True
    print("")
    print(CYAN + "-"*10)
    print("| Log In |")
    print("-"*10 + RESET)
    print("")
    #checks for the username
    while try_name == True:
        username_log = input("Write your username: ").strip()
        #if the username is not found, asks the user if they are sure they are registered
        if username_log not in users:
                username_checking = True
                while username_checking == True:
                    registration_checking = input(RED + "There is nobody with that username, are you sure you have registered already? (y/n): " + RESET).lower().strip()
                    #if they are sure, it asks another time for the username
                    if registration_checking == "y":
                        username_checking = False
                    #if not, prompts the user to registration
                    elif registration_checking == "n":
                        print(CYAN + "Let's register to Amazon!" + RESET)
                        return registration()
                    else:
                        print("")
                        print(RED + "The operation selected is not valid: please choose from the available options." + RESET)
                        print("")
        #if the username is found, it asks for the password up to 3 times
        else:
            try_name = True
            current_user = username_log
            password_log = input("Write your password: ").strip()
            while attempts >= 0:
                #for the last attempt, it asks one more time after 5s
                if attempts == 0:
                    print(RED + "You are out of guesses! Wait 5 seconds..." + RESET)
                    time.sleep(5)
                    password_log = input("Write your password: ").strip()
                    #if it is again wrong, it exits the program
                    if password_log != users[current_user]["password"]:
                        print(RED + "Wrong again! Sorry, you have to restart the process." + RESET)
                        sys.exit()
                    #if it is right, goes on to options
                    else:
                        print(YELLOW + "")
                        print("*"*43)
                        print("*** Welcome to Amazon Expenses Tracker! ***")
                        print("*"*43 + RESET)
                        return options()
                #if the password is correct, options() follows
                elif password_log == users[current_user]["password"]:
                    print("")
                    print(YELLOW + "*"*43)
                    print("*** Welcome to Amazon Expenses Tracker! ***")
                    print("*"*43 + RESET)
                    return options()
                #if the pass is wrong but NOT the last attempt, it takes one away and asks again for the password
                else:
                    attempts -= 1
                    print(RED + "Wrong password... try again!" + RESET)
                    password_log = input("Write your password: ").strip()
#let the user login with the credential they just used to register themselves

def options():
    global current_user
    choices = True
    while choices == True:
        print("-"*60)
        print("What would you like to do?")
        choice = input("1. Enter a purchase\n2. Generate a report\n3. Quit\nYour choice: ").strip()
        if choice == "1":
            return register_item()
        elif choice == "2":
            return print_report()
        elif choice == "3":
            return exit_program()
        else:
            print("")
            print(RED + "The operation selected is not valid: please choose from the available options." + RESET)
            print("")
#let the user choose between adding items, printing a report, or quitting the program

def register_item():
    new_key = "item"+str(len(users[current_user]["items"])+1)
    new_item = {}
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
                print(RED + "The date cannot be in the future. Try again!" + RESET)
        except ValueError:
            print(RED + "Invalid date format. Try again!" + RESET)
    while try_name == False:
        new_name = input("Enter the item purchased (at least 3 characters): ").strip()
        if len(new_name) >= 3:
            new_item["name"] = new_name
            try_name = True
        else:
            print(RED + "The name is too short. Try again!" + RESET)
    while try_cost == False:
        try:
            new_cost = float(input("Enter the cost of the item in Euro: "))
            if new_cost > 0:
                new_item["cost"] = new_cost
                try_cost = True
            else:
                print(RED + "Sorry, it needs to be more than 0." + RESET)
        except ValueError:
            print(RED + "That's not a number. Try again!" + RESET)
    while try_weight == False:
        try:
            new_weight = float(input("Enter the weight of the item in kg: "))
            if new_weight > 0:
                new_item["weight"] = new_weight
                try_weight = True
            else:
                print(RED + "Sorry, it needs to be more than 0." + RESET)
        except (ValueError):
            print(RED + "That's not a number. Try again!" + RESET)
    while try_quantity == False:
        try:
            new_quantity = int(input("Enter the quantity purchased (1 or more): "))
            if new_quantity >= 1:
                new_item["quantity"] = new_quantity
                try_quantity = True
            else:
                print(RED + "Quantity must be at least 1." + RESET)
        except ValueError:
            print(RED + "Invalid value. Try again!" + RESET)
    users[current_user]["items"][new_key] = new_item
    save_data()
    options()
#it allows the user to put one item at a time

def print_report():
    global current_user
    print("Generating report...")
    time.sleep(2)
    print("")
    print(YELLOW + " "*15,"-"*29)
    print(" "*15,"|   Amazon Expense Report   |")
    print(" "*15,"-"*29 + RESET)
    print("")
    print("-"*60)
    print("")
    if not users[current_user]["items"]:
        print("Sorry, no items registered yet")
        print("")
        return options()
    else:
        print(f"NAME: {current_user}"," "*5,
            f"PASSWORD: ***"," "*5,
            f"TEL: +49***"+users[current_user]["phone_number"][-2:])
        print(f"DATE:", datetime.today().date())
        print("-"*60)
        print("DELIVERY CHARGES", " "*6, "TOTAL ITEM COST")
        total_delivery_cost = sum(item["weight"] * item["quantity"] for item in users[current_user]["items"].values())
        total_items_cost = sum(item["cost"] * item["quantity"] for item in users[current_user]["items"].values())
        print(" "*2, f"{total_delivery_cost:.2f}", "EURO", " "*13, f"{total_items_cost:.2f}", "EURO")
        print("")
        print("MOST EXPENSIVE", " "*6, "LEAST EXPENSIVE")
        most_expensive_item = max(users[current_user]["items"].values(), key=lambda item : item["cost"])
        name_most_expensive = most_expensive_item["name"]
        least_expensive_item = min(users[current_user]["items"].values(), key=lambda item : item["cost"])
        name_least_expensive = least_expensive_item["name"]
        print(" "*2, name_most_expensive, " "* 15, name_least_expensive)
        print(" "*2, f"cost: {most_expensive_item["cost"]:.2f}"," "*8, f"cost: {least_expensive_item["cost"]:.2f}")
        print("")
        average_cost_item = (sum(item["cost"] for item in users[current_user]["items"].values())) / len(users[current_user]["items"])
        print(f"AVERAGE COST OF ITEM PER ORDER: {average_cost_item:.2f} EURO")
        dates = [datetime.strptime(item["date"], "%Y/%m/%d").date() for item in users[current_user]["items"].values()]
        biggest_date = max(dates)
        lowest_date = min(dates)
        if biggest_date != lowest_date:
            print(f"PURCHASE DATE RANGE: {lowest_date} - {biggest_date}")
        else:
            print(f"ALL ITEMS PURCHASED ON: {lowest_date}")
        print("-"*60)
        if (total_delivery_cost + total_items_cost) <= 500:
            print(CYAN + "Note: You have not exceeded the spending limit of 500 EURO" + RESET)
        else:
            print(CYAN + "Note: You have exceeded the spending limit of 500 EURO" + RESET)
        return options()
#it allows the user to pring a report, or a message when there are no registered items

def exit_program():
    print("Quitting program...")
    time.sleep(2)
    print(f"{CYAN}Thank you for your visit, {current_user}. Goodbye!{RESET}")
    sys.exit()
#exits the program

#############################end of functions

def main ():
    load_data()
    print("")
    print(YELLOW + "*"*25)
    print("*** Welcome to Amazon ***")
    print("*"*25 + RESET)
    print("")
    print("First, we'd like to know if you are a new customer, or a returning one.")
    register_login = True
    while register_login == True:
        access = input("Do you want to login, or to register? (l/r): ").strip()
        if access == "r":
            register_login = False
            registration()
        elif access == "l":
            log_in()
            register_login = False
        else:
            print("Invalid input. Please choose between y/n")
    options()

main()