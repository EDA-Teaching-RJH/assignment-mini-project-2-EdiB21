import csv
import time 

class User:

    ROLE = "user"
    PERMS = {"view_self"}


class Admin(User):

    ROLE = "admin"
    PERMS = {"view_self", "view_users", "manage_users"}


class Reader(User):

    ROLE = "reader"
    PERMS = {"view_self", "view_users"}