import re, time

user_info = {
    "username": "",
    "password": "",
    "phone_number": ""
}

items = {
    "date": "",
    "item": "",
    "total": "",
    "weight": "",
    "quantity": ""
}

#############################start of functions

def registration(username,password):     #saves username and registration in user_info
    user_info["username"] = username
    user_info["password"] = password
    return
#registration works

def password_checker(password):
    pattern_password = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,20}"
    if re.search(pattern_password,password):
        print("Registration successful!")
    else:
        return "Sorry, invalid password: try again... "
#password checker works
    
def phone_number_checker(phone_number):
    phone = False
    pattern_phone = r"^(\+49)[0-9]{8}$"
    while phone == False:
        if re.search(pattern_phone,phone_number):
            phone = True
            user_info["phone_number"] = phone_number
            return "Valid phone number" 
        else:
            print("Invalid number... please try again")
#phone number checker works, but the for loop is to fix

def log_in(username_log,password_log):
    attempts = 2
    while attempts >= 0:
        if attempts == 0:
            print("You are out of guesses! Wait 5 seconds...")
            time.sleep(5)
            password_log = input("Please enter your password: ")
            if username_log != user_info["username"] or password_log != user_info["password"]:
                print("Wrong again! Sorry, you have to register again")
                break
            else:
                print("Welcome to the Amazon Expense Tracker!")
        elif username_log == user_info["username"] and password_log == user_info["password"]:
            return "Welcome to the Amazon Expense Tracker!"
        else:
            attempts -= 1
            print("Wrong... try again")
            password_log = input("Please enter your password: ")
#log in works    

def user_options(choice):
    #if choice == 1:
    pass

#############################end of functions

#1.Accept username and password for registration and save them in user_info
print("*"*42)
print("*** Welcome to Amazon Expenses Tracker ***")
print("*"*42)
username = input("Please enter your username: ")
password = input("Please enter your password: ")
registration(username,password)

#2.See if the password is valid and save it
print(password_checker(password))

#3.Ask the user for a phone number until it's right
phone_number = str(input("Please enter phone number to continue:" ))
print(phone_number_checker(phone_number))

#4.The program asks the user to log in (username and password)
username_log = input("Write your username: ")
password_log = input("Write your password: ")
print(log_in(username_log,password_log))

#5.After a successful login, print a welcome message
print(f"Hello, {user_info["username"]}! Welcome to the Amazon Expense Tracker!")

#6.Give 3 options to users that they need to pick from
#1.enter a purchase 2.generate a report 3.quit



