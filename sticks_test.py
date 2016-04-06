import unittest
from pickup_pvp import *

###This works with functions when not in a class. Didn't have time to figure out how to test in a class :(

class TestSticks(unittest.TestCase):


    def test_check_initial_stick_count(self):
        self.assertTrue(self.check_initial_stick_count('30'))

    def test_check_initial_stick_count_with_letter(self):
        self.assertFalse(check_initial_stick_count('D'))

    def test_check_initial_stick_count_out_of_range(self):
        self.assertFalse(check_initial_stick_count('104'))

    def test_check_initial_stick_count_symbol(self):
        self.assertFalse(check_initial_stick_count('!'))

    def test_acceptable_pickup_amount(self):
        self.assertTrue(acceptable_pickup_amount('2'))

    def test_acceptable_pickup_amount_letter(self):
        self.assertFalse(acceptable_pickup_amount('D'))

    def test_acceptable_pickup_amount_out_of_range(self):
        self.assertFalse(acceptable_pickup_amount('4'))

    def test_acceptable_pickup_symbol(self):
        self.assertFalse(acceptable_pickup_amount('!'))

    def test_check_loss_conditions(self):
        self.assertTrue(check_loss(0))




if __name__ == '__main__':
    unittest.main()
