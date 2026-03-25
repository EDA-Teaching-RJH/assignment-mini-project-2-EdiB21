import csv
import time 
import REGEX_Check


class User:

    ROLE = "user"
    PERMS = {"view_self"}

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.role = self.ROLE


    def has_permission(self, perm):
        return perm in self.PERMS


    def menu_options(self):
        return("--Menu--"
        "\n1. Show animals"
        "\n2. Jokester"
        "\n3. Log Out"
        "\n4. View User Information")


    def view_data_u(self):

        print("Collecting Information...")
        time.sleep(0.2)

        print("-" * 35 + "|")
        print(f"Name: {self.name.title()}"
        f"\nEmail: {self.email}"
        f"\nPassword: {self.password}")
    
        print("-" * 35 + "|")


class Admin(User):

    ROLE = "admin"
    PERMS = {"view_self", "view_users", "manage_users"}

    def __init__(self, name, email, password):
        super().__init__(name, email, password)


    def menu_options(self):                             ##admin more options
        return("--Menu--"
        "\n1. Show animals"
        "\n2. Jokester"
        "\n3. Log Out"
        "\n-- DATABASE --"
        "\n4. View User Information"
        "\n-- MANAGEMENT --"
        "\n5. Add User"
        "\n6. Remove User"
        "\n7. Update User Role")


    def add_user(self):

        users_f = "User_Data.csv"
        
        print("Adding User")
        print("-" * 50)
        
        user_na = REGEX_Check.name_format()
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        user_em = REGEX_Check.email_format()
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        user_pa = REGEX_Check.password_format()
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        user_ro = input("What is the role for the user: ").strip()
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.2)

        with open(users_f, "a", newline="") as file:        #used to have a dictwriter for csv but that had continuously made new headers and didnt write on an empty row and overlapped an exsiting one, so it was replaced with 'writer'
            user_a = csv.writer(file)
            user_a.writerow([user_na, user_em, user_pa, user_ro])       #write to csv file on a new row (with statement uses 'a' to append)

        print("User has been added!")
        time.sleep(0.2)
        print("New user database: ")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)

        with open(users_f, newline="") as file:
            file_read = csv.DictReader(file)

            print(f"{'Name':<15} {'Email':<45} {'Password':<30} {'Role':<10}")
            print("-" * 100 + "|")

            for row in file_read:
                print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30} {(row['role'].title()):<10}")      #make an organised table

            print("-" * 100 + "|")


    def remove_user(self):

        users_f = "User_Data.csv"
        admin_code = 2426
        print("Removing User")
        print("-" * 60)

        user_em = input("Please enter the email of the user to remove: ").strip().lower()

        with open(users_f, newline="") as file:
            file_read = csv.DictReader(file)
            a_rows = list(file_read)                    #this one saves the current rows in csv into a variable

        all_emails = [row["email"] for row in a_rows]   #saves all emails in each row of the csv

        print("FINDING USER...")
        for i in range(1,5):
            time.sleep(0.5)
            print("." * i)

        if user_em not in all_emails:
            print("USER NOT FOUND")
            time.sleep(0.2)
            return

        print("USER FOUND")

        tries = 0
        removed = False

        while tries < 2:

            admin_co = int(input("Please enter admin code: "))

            if admin_co != admin_code:
                tries += 1
                if tries == 2:
                    print("NO ATTEMPTS REMAINING")
                    print("RETURNING TO MENU")
                    return
                print("INCORRECT ADMIN CODE")
                print("ONE ATTTEMPT REMAINING")
            else:
                print("User is being removed")

                for i in range(1,3):
                    time.sleep(0.5)
                    print("." * i)
                 
                new_rows = [row for row in a_rows if row["email"] != user_em]   #this is going through the rows and saving only the rows which dont
                                                                                 #have the same email as our inputted one and then saving that as new rows 
                with open(users_f, "w", newline="") as file:
                    user_a = csv.DictWriter(file, fieldnames = ["name", "email", "password", "role"])
                    user_a.writeheader()
                    user_a.writerows(new_rows)              #re writes the entire file with our current new set of rows that doesnt include the one
                print("User has been removed")              # we want to remove 
                removed = True
                break
        if removed:            #if removed == True
            print("New user database: ")
            time.sleep(0.3)
            print("...")
            time.sleep(0.3)

            with open(users_f, newline="") as file:
                file_read = csv.DictReader(file)

                print(f"{'Name':<15} {'Email':<45} {'Password':<30} {'Role':<10}")
                print("-" * 100 + "|")

                for row in file_read:
                    print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30} {(row['role'].title()):<10}")
                print("-" * 100 + "|")


    def upd_user(self):

        users_f = "User_Data.csv"
        admin_code = 2426
        print("Updating User")
        print("-" * 60)
        time.sleep(0.5)

        user_em = input("Please enter the email of the user to update: ").strip().lower()

        with open(users_f, newline="") as file:
            file_read = csv.DictReader(file)
            a_rows = list(file_read)        #same premise as before saving all csv rows

        all_emails = [row["email"] for row in a_rows]   #holds all the rows emails

        print("FINDING USER...")
        for i in range(1,5):
            time.sleep(0.5)
            print("." * i)

        if user_em not in all_emails:       #cross checks our input is in the emails
            print("USER NOT FOUND")
            time.sleep(0.2)
            return

        print("USER FOUND")

        tries = 0
        updated = False

        while tries < 2:

            admin_co = int(input("Please enter admin code: "))

            if admin_co != admin_code:
                tries += 1
                if tries == 2:
                    print("NO ATTEMPTS REMAINING")
                    print("RETURNING TO MENU")
                    return
                print("INCORRECT ADMIN CODE")
                print("ONE ATTTEMPT REMAINING")
            else:
                updating = True

                while updating:
                    upd_choice = input("Would you like to update the: [Name] [Email] [Password] [Role] [Done] \n:").strip().lower()
                
                    if upd_choice == "name":
                        new_val = REGEX_Check.name_format()
                        for row in a_rows:
                            if row["email"] == user_em:
                                row["name"] = new_val
                        print("Name updated!")
                    elif upd_choice == "email":
                        new_val = REGEX_Check.email_format()
                        for row in a_rows:
                            if row["email"] == user_em:
                                row["email"] = new_val
                        user_em = new_val
                        print("Email updated!")
                    elif upd_choice == "password":
                        new_val = REGEX_Check.password_format()
                        for row in a_rows:
                            if row["email"] == user_em:
                                row["password"] = new_val
                        print("Password updated!")
                    elif upd_choice == "role":
                        new_val = input("Enter the new role: ").strip().lower()
                        for row in a_rows:
                            if row["email"] == user_em:
                                row["role"] = new_val
                        print("Role updated!")
                    elif upd_choice == "done":
                        updating = False
                    else:
                        print("Invalid entry, try again")

                with open(users_f, "w", newline="") as file:        #once all changes are made and done is selected loop ends and the new a_rows is writen to the csv file
                    user_a = csv.DictWriter(file, fieldnames=["name","email","password","role"])
                    user_a.writeheader()
                    user_a.writerows(a_rows)

                print("Changes Saved")
                updated = True
                break

        if updated:
            print("New user database: ")
            time.sleep(0.3)
            print("...")
            time.sleep(0.3)

            with open(users_f, newline="") as file:
                file_read = csv.DictReader(file)

                print(f"{'Name':<15} {'Email':<45} {'Password':<30} {'Role':<10}")
                print("-" * 100 + "|")

                for row in file_read:
                    print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30} {(row['role'].title()):<10}")
                print("-" * 100 + "|")


    def view_data(self):
        users_f = "User_Data.csv" 

        print("Printing Current Database: ")
        for i in range(1,3):
            time.sleep(0.5)
            print("." * i)

        with open(users_f, newline="") as file:
            file_read = csv.DictReader(file)

            print(f"{'Name':<15} {'Email':<45} {'Password':<30} {'Role':<10}")
            print("-" * 100 + "|")

            for row in file_read:
                print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30} {(row['role'].title()):<10}")

            print("-" * 100 + "|")


class Reader(User):     ##reader can view users data as an extra for their role

    ROLE = "reader"
    PERMS = {"view_self", "view_users"}

    def __init__(self, name, email, password):
        super().__init__(name, email, password)


    def menu_options(self):
        return("--Menu--"
        "\n1. Show animals"
        "\n2. Jokester"
        "\n3. Log Out"
        "\n-- DATABASE --"
        "\n4. View User Information")


    def view_data_r(self):
        users_f = "User_Data.csv" 

        print("Printing Current Database: ")
        for i in range(1,3):
            time.sleep(0.5)
            print("." * i)

        with open(users_f, newline="") as file:
            file_read = csv.DictReader(file)

            print(f"{'Name':<15} {'Email':<45} {'Password':<30}")
            print("-" * 90 + "|")

            for row in file_read:
                print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30}")



#Fully compelted on 11/04/26