import REGEX_Check
import User_Levels
import csv
import re
import unittest  #tried another testing library apart from pytest as it wasnt working for me


class TestRegexFormatting(unittest.TestCase):
    
    def test_name(self):
        self.assertTrue(re.match(r'^[a-zA-Z]+$', "Timothy"))
        self.assertTrue(re.match(r'^[a-zA-Z]+$', "Bradley"))
    

    def test_name_digits(self):
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "B0bby5"))
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "Wr0ng5"))

    
    def test_name_specials(self):
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "B0bby/5"))
        self.assertFalse(re.match(r'^[a-zA-Z]+$', "b4d/name"))


    def test_email(self):
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "edis@kent.ac.uk"))
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "awesomegamer23@gmail.com"))
        self.assertTrue(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "correct@email.co.uk"))
    

    def test_email_inva(self):
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "bob#'@bobbyiscool.co.cz"))
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "in/correct@email.co.uk"))
        self.assertFalse(re.match(r'^\w+@\w+\.(ac\.uk|gov\.uk|com|co\.uk)$', "wr.ong@email.uk.brz"))


class TestUserLevels(unittest.TestCase):


class TestMenuOptions(unittest.TestCase):