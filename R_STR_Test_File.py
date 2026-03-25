import REGEX_Check
import User_Levels
import csv
import re
import unittest  #tried another testing library apart from pytest as it wasnt working for me


class TestRegexFormatting(unittest.TestCase):

    def test_name(self):
        self.assertTrue(re.match(r'^[a-zA-Z]+$', "Timothy")) #checks that my format is correct for names
        self.assertTrue(re.match(r'^[a-zA-Z]+$', "Bradley"))
    

    def test_name_digits(self):
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "B0bby5")) #checks that formatting doesnt allow digits in names
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "Wr0ng5"))

    
    def test_name_specials(self):
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "B0bby/5")) #checks that formatting doesnt allow special characters in names
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "b4d/name"))


    def test_email(self):
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "edis@kent.ac.uk")) #checks that emails work under the domains allowed
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "awesomegamer23@gmail.com"))
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "correct@email.co.uk"))
    

    def test_email_inva(self):
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "bob#'@bobbyiscool.co.cz"))#checks that if a foreign domain is used it is flagged as invalid
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "in/correct@email.co.uk"))
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "wr.ong@email.uk.brz"))


class TestUserLevels(unittest.TestCase):        #overall checking that classes system works and roles are assigned correctly

    def test_admin_role(self):
        admin = User_Levels.Admin("edis", "edis@yahoo.com", "apple123")
        self.assertEqual(admin.role, "admin")


    def test_user_cant_manage(self):
        user = User_Levels.User("bob", "bobo@gmail.com", "banana5")
        self.assertFalse(user.has_permission("manage_users"))


    def test_user_can_view_self(self):
        user = User_Levels.User("bob", "bobo@gmail.com", "banana5")
        self.assertTrue(user.has_permission("view_self"))


    def test_reader_subclass_user(self):
        self.assertIsSubclass(User_Levels.Reader, User_Levels.User)     #checking if the classes are correctly subbed from User


    def test_reader_not_subclass_admin(self):
        self.assertFalse(issubclass(User_Levels.Admin, User_Levels.Reader))


class TestMenuOptions(unittest.TestCase):

    def test_reader_menu(self):
        reader = User_Levels.Reader("edi", "edicool@bingo.co.uk", "pass258")
        self.assertIn("4. View User Information", reader.menu_options())        #checks that options are in menu options


    def test_reader_cant_remove(self):
        reader = User_Levels.Reader("edi", "edicool@bingo.co.uk", "pass258")        #checks that reader doesnt have admin options
        self.assertNotIn("6. Remove User", reader.menu_options())


    def test_admin_mangement(self):
        admin = User_Levels.Admin("edis", "myemail@gmail.com", "monkey29")
        self.assertIn("7. Update User Role", admin.menu_options())


    def test_admin_no_extras(self):
        admin = User_Levels.Admin("edis", "myemail@gmail.com", "monkey29")      #checks that the option is not in menu options
        self.assertNotIn("9. Be silly", admin.menu_options())