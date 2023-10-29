# from django.test import TestCase
from unittest import TestCase, main
# from cards.run_app import *  # for run in python console
# from cards.get_cards import *# for run in python console
from run_app import *  # for test
from get_cards import * # for test



# Create your tests here.

class testInputCardType(TestCase):
    # Test if the type of variable 'existing_cards' is a list
    def test_input_existing_cards_type(self):
        self.assertIsInstance(existing_cards, list, "Cards list input is not a list.")


class testInputCardIsString(TestCase):
    # Test if type of elements of 'existing_cards' is string
    def test_input_existing_card_is_string(self):
        for card in existing_cards:
            self.assertIsInstance(card, str, "Cards input is not a string.")


class testInputURLIsNotEmpty(TestCase):
    # Test ir file_url is not empty
    def test_file_url_is_not_empty(self):
        self.assertNotEqual(file_url, "")


# Test get_cards() return
class testGetCardFunc(TestCase):
    # test if get_card() returns a dictionary
    def test_get_card_return_dict_type(self):
        self.assertIsInstance(get_cards(existing_cards, file_url), dict)

    # test if get_card() returns a dictionary not empty
    def test_get_card_return_not_empty(self):
        self.assertTrue(get_cards(existing_cards, file_url), "No cards is the uploaded file.")


# Detect all test classes and run all tests in the file
if __name__ == '__main__':
    unittest.main()
