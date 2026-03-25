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
    print("Please select an option:")
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


def user_register():


if __name__ == "__main__":
    main()


#Fully completed 24/03/26 (break during exam time)