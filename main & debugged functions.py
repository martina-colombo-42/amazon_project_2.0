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

def registration():
    check_password = False
    pattern_password = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,20}"
    username = input("Please enter your username: ")
    user_info["username"] = username
    while check_password == False:
        password = input("Please enter your password: ")
        if re.search(pattern_password,password):
            check_password = True
            user_info["password"] = password
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
        phone_number = input("Please enter phone number to continue: ")
        if re.search(pattern_phone,phone_number):
            phone = True
            user_info["phone_number"] = phone_number
            return "Valid phone number!" 
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
                print("")
                print("*"*43)
                print("*** Welcome to Amazon Expenses Tracker! ***")
                print("*"*43)
                print("Welcome to the Amazon Expense Tracker!")
                return ""
        elif username_log == user_info["username"] and password_log == user_info["password"]:
            print("")
            print("*"*43)
            print("*** Welcome to Amazon Expenses Tracker! ***")
            print("*"*43)
            return ""
        else:
            attempts -= 1
            print("Wrong... try again")
            password_log = input("Please enter your password: ")
#log in works    

def user_options(choice):
    #if choice == 1:
    pass

#############################end of functions

def main ():
    print("*"*25)
    print("*** Welcome to Amazon ***")
    print("*"*25)
    print("")
    print(registration())
    print(phone_number_checker())
    print("")
    print("-"*10)
    print("| Log In |")
    print("-"*10)
    print("")
    username_log = input("Write your username: ")
    password_log = input("Write your password: ")
    print(log_in(username_log,password_log))
    return "So far, it works!"


print(main())