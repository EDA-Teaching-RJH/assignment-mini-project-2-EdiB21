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

        with open(users_f, "a", newline="") as file:
            user_a = csv.writer(file)
            user_a.writerow([user_na, user_em, user_pa, user_ro])

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
                print(f"{(row['name'].title()):<15} {row['email']:<45} {row['password']:<30} {(row['role'].title()):<10}")

            print("-" * 100 + "|")


class Reader(User):

    ROLE = "reader"
    PERMS = {"view_self", "view_users"}