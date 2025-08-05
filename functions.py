import re

def registration(username,password):     #saves username and registration in user_info
    user_info["username"] = username
    user_info["password"] = password
    return

def password_checker(password):
    pattern_password = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,20}"
    if re.search(pattern_password,password):
        print("Nice! Now please enter a phone number: ")
        return #next function
    else:
        return "Sorry, try again... "
    
def phone_number_checker(phone_number):
    phone = False
    pattern_phone = r"^(+49)[0-9]{9,9}"
    while phone == False:
        if re.search(pattern_phone,phone_number):
            phone = True
            return #enter next function
        else:
            print("Invalid number... please try again")

#3 attemps with delay when incorrect (5 sec)
#after that, register again and exit
def log_in(username_log,password_log):
    #attempts = 2
    #while attempts > 0:
    #    if username_log == username and password_log == password:
    pass

def user_options(choice):
    #if choice == 1:
    pass