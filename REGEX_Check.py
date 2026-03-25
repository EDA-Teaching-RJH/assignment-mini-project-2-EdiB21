import re
import time


def name_format():
    name_patt = r'^[a-zA-Z]+$'              ##only letter capital or not are allowed
    name_check = re.compile(name_patt)
    print("Only enter the first name please!")
    print("-" * 50)
    time.sleep(0.4)

    while True:
        name = input("Enter: ").strip().lower()
        name = re.sub(r'\s+', '', name)
        if name_check.match(name):
            return name
        else:
            print("Invalid Name Entry")
            time.sleep(0.3)
            print("Try Again")


def email_format():
    email_patt = r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$'          ##most domains are covered, but would be only local ones
    print("Please enter  email address")
    print("-" * 50)
    time.sleep(0.4)
    
    while True:
        email = input("Enter: ").strip().lower()
        email = re.sub(r'\s+', '', email)
        if re.match(email_patt, email):
            return email
        else:
            print("Invalid Email Entry")
            time.sleep(0.3)
            print("Try Again")


def password_format():

    pass_patt = r'^(?=.*[a-zA-Z])(?=.*\d)\w{5,20}$'     ##print below explains, but only letters and digits are allowed but limited to 20 max, 5 min
    print("Passwords Must:\n] Contain 5-20 characters \n] Include atleast one letter and one number\n] Not include any special characters(Only _ Accepted)")
    print("-" * 50)
    time.sleep(0.4)

    while True:
        password = input("Enter: ").strip()
        password = re.sub(r'\s+', '', password)
        if re.match(pass_patt, password):
            return password
        else:
            print("Invalid Password Entry, Please refer to previous instructions!")
            time.sleep(0.3)
            print("Try Again")


#Fully completed on 11/03/26