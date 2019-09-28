import unittest
from lab1 import *

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    """ Function max_list_iter Tests """
    def test_max_list_iter(self):
        # Checks if max_list_iter raises a ValueError if a list with None is entered
        nums = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(nums)

    def test_max_list_iter_empty_list(self):
        # Checks to make sure max_list_iter returns 'None' when passed an empty list
        nums = []
        self.assertEqual(max_list_iter(nums), None)

    def test_max_list_iter_beginning_largest(self):
        # Checks if the function returns the largest value if it is the first in the list
        nums = [10, 8, 6, 4, 2]
        self.assertEqual(max_list_iter(nums), 10)

    def test_max_list_iter_middle_largest(self):
        # Checks if the function returns the largest value if it is in the middle of the list
        nums = [6, 8, 10, 4, 2]
        self.assertEqual(max_list_iter(nums), 10)

    def test_max_list_iter_ending_largest(self):
        # Checks if the function returns the largest value if it is last in the list
        nums = [2, 8, 6, 4, 10]
        self.assertEqual(max_list_iter(nums), 10)

    def test_max_list_iter_negative(self):
        # Checks if the function returns the largest negative value in a list of negatives
        nums = [-22, -2, -10, -7, -16]
        self.assertEqual(max_list_iter(nums), -2)

    def test_max_list_iter_mixed(self):
        # Checks if the function returns the largest value in a mixed list of positives and negatives
        nums = [77537, -19423, 270465024, 64358, -824365]
        self.assertEqual(max_list_iter(nums), 270465024)

    def test_max_list_iter_two_largest(self):
        # Checks if the function returns the largest value when there are 2 largest values
        nums = [2, 20, 13, 20, 5]
        self.assertEqual(max_list_iter(nums), 20)

    """ Function reverse_rec Tests """
    def test_reverse_rec_odd_size(self):
        # Checks to make sure this function works on odd and even sized lists
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # Checks odd number sized list

    def test_reverse_rec_even_size(self):
        self.assertEqual(reverse_rec([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])  # Checks even number sized list

    def test_reverse_rec_negatives(self):
        # Checks list with all negative values
        self.assertEqual(reverse_rec([-5, -4, -3, -2, -1]), [-1, -2, -3, -4, -5])

    def test_reverse_rec_single_value(self):
        # Checks the base case when a list with a length of 1 is passed as a parameter
        self.assertEqual(reverse_rec([0]), [0])

    def test_reverse_rec_empty_list(self):
        # Checks the base case for when an empty list is passed as a parameter
        self.assertEqual(reverse_rec([]), None)

    def test_reverse_rec_none(self):
        # Checks the base case for when 'None' is passed as a parameter
        nums = None
        with self.assertRaises(ValueError):
            reverse_rec(nums)

    """ Function bin_search Tests """
    def test_bin_search_left(self):
        # Checks if the function can find a value in the left part of the array
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), 2)

    def test_bin_search_right(self):
        # Checks if the function can find a value in the right part of the array
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, low, high, list_val), 7)

    def test_bin_search_middle(self):
        # Checks if the function can find the value in the middle of the array
        list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search_even_sized_list(self):
        # Checks to make sure bin_search works with an even sized list
        list_val = [0, 1, 2, 3, 4, 5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search_negatives(self):
        # Checks to make sure bin_search works with negative numbers
        list_val = [-10, -9, -8, -7, -4, -3, -2, -1, -0]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-7, low, high, list_val), 3)

    def test_bin_search_value_not_present(self):
        # Checks to make sure bin_search returns 'None' when a value is not present in the list
        list_val = [0, 1, 2, 5, 6, 7]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, low, high, list_val), None)

    def test_bin_search_empty_list(self):
        # Checks to make sure bin_search returns 'None' when it is passed an empty list
        list_val = []
        low = 0
        high = len(list_val)
        self.assertEqual(bin_search(0, low, high, list_val), None)

    def test_bin_search_none_list(self):
        # Checks to make sure bin_search raises a ValueError when it is passed a 'None' list
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, list_val)

    def test_bin_search_one_value(self):
        list_val = [1]
        low = 0
        high = len(list_val)
        self.assertEqual(bin_search(1, low, high, list_val), 0)

    def test_bin_search_one_value_no_target(self):
        list_val = [1]
        low = 0
        high = len(list_val)
        self.assertEqual(bin_search(2, low, high, list_val), None)


if __name__ == "__main__":
    unittest.main()

