# All parts of the code had been completed on a serpate folder of files as i cannot run my code on cloned repositories but i have uploaded the 
# code in order of what i had comepleted first so it is still chronologically correct.
# I will also include time stamps from when i completed each file seperately




import tkinter
import csv
import time
import REGEX_Check
import User_Levels
import cowsay
import random
import pyjokes


def main():
    login_screen()


def login_screen():
    print("Welcome To The Awesome App!")
    time.sleep(0.3)
    print("Please select an option:")   #simple opening screen with two options
    print("--------------------")
    print("Login ----- Register")
    print("--------------------")
    
    while True:
        use_input = input(": ").lower().strip()

        if use_input == "login":
            user_login()
            return False
        elif use_input == "register":
            user_register()
            return False
        else:
            print("Invalid Option please pick again.")
            continue


def user_login():
    print("Welcome Back, Please enter your Email and Password!")

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:

        email = REGEX_Check.email_format()      #only checks email and password like most other apps
        time.sleep(0.3)
        password = REGEX_Check.password_format()
        time.sleep(0.3)
        print("Checking Data Base..")
        time.sleep(0.2)
        print("...")
        time.sleep(0.6)

        with open("User_Data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if not row:
                    continue
                if row[1] == email and row[2] == password:
                    print(f"Welcome back, {row[0].title()}!")  # uses the csv rows to check if the account has the correct role and then gives the correct menu options from the correct class for it
                    if row[3] == "admin":
                        user = User_Levels.Admin(row[0], row[1], row[2])
                    elif row[3] == "reader":
                        user = User_Levels.Reader(row[0], row[1], row[2])
                    elif row[3] == "user":
                        user = User_Levels.User(row[0], row[1], row[2])
                    user_menu(user)
                    return

        attempts += 1
        print("Credentials Do Not Match..")
        print(f"{max_attempts - attempts} Attempts Remaining.")
        time.sleep(0.3)

    print("Too many failed attempts. Returning to Login...")
    login_screen()


def user_register():
    print("Welcome! Please enter your name, email and a password!")

    role = "user"

    name = REGEX_Check.name_format()        #all inputs here and in the login function use the regex formatting to make sure that inputs are valid
    time.sleep(0.4)                         # also used since they already have while loops to allow for multiple attempts and not accept invalid ones
    print("Saving..")
    time.sleep(0.4)
    email = REGEX_Check.email_format()
    time.sleep(0.4)
    print("Saving..")
    time.sleep(0.4)
    password = REGEX_Check.password_format()
    time.sleep(0.4)
    print("Saving")
    time.sleep(0.4)

    with open("User_Data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,email,password,role])
    
    print("Registration Complete!")
    user = User_Levels.User(name, email, password)  #user variable saves the different parts after writing to make it easier to open the correct menu
    user_menu(user)
    time.sleep(0.2)
    print("sending to menu..")
    time.sleep(0.2)


def user_menu(user):


    
if __name__ == "__main__":
    main()


#Fully completed 24/03/26 (break during exam time)