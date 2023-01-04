#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_regular(self):
        """Unittest for max_integer([..])"""
        test_m = [1, 34, 5, 8, 56]
        self.assertEqual(max_integer(test_m), 56)

    def test_only_floats(self):
        """Test for list with only float"""
        test_m = [1.78, 34.56, 5.00001, 8.77777, 5.63]
        self.assertEqual(max_integer(test_m), 34.56)

    def test_floats_and_ints(self):
        """Test for list with float and int"""
        test_m = [1000, 101.98, 5.00001, 888, 5.63]
        self.assertEqual(max_integer(test_m), 1000)

    def test_all_equal(self):
        """Test for list with equal values"""
        test_m = [124, 124, 124, 124, 124]
        self.assertEqual(max_integer(test_m), 124)

    def test_positive_negative(self):
        """Test for list with positive and negative values"""
        test_m = [124, -678, -1000, 24, 999]
        self.assertEqual(max_integer(test_m), 999)

    def test_only_negatives(self):
        """Unittest for list with only negatives"""
        test_m = [-1, -34, -5, -8, -56]
        self.assertEqual(max_integer(test_m), -1)

    def test_infinite_value(self):
        """Test for list with infinite value"""
        test_m = [124, -678, float('inf'), 24, 999]
        self.assertEqual(max_integer(test_m), float('inf'))

    def test_value_none(self):
        """Test for list with None value"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """Test for empty list"""
        test_m = []
        self.assertEqual(max_integer(test_m), None)

    def test_one_argument(self):
        """Test for list with one element"""
        test_m = [6]
        self.assertEqual(max_integer(test_m), 6)

    def test_string(self):
        """Test for list with string"""
        test_m = [56, "string", 65, 7899]
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_num(self):
        """Test for numeric string"""
        test_m = "126976878"
        self.assertEqual(max_integer(test_m), "9")

    def test_list_mix(self):
        """Test for numeric string"""
        test_m = [[1, 2], 23333, {2, 67}, (89, 3)]
        with self.assertRaises(TypeError):
           max_integer(test_m)

    def test_nan(self):
        """Test for list with nan"""
        test_m = [56, float('nan'), 65, 7899]
        self.assertEqual(max_integer(test_m), 7899)

    def test_list_string(self):
        """Test for list of string lists"""
        test_m = [["gregge"], ["fvuuu"], ["dsdv"]]
        self.assertEqual(max_integer(test_m), ["gregge"])

    def test_long_int(self):
        """Test for list of long integers"""
        test_m = [
                234334343434343, 45555555555545, 45555555555554,
                4444444444444445555555, 2323222222222222232]
        self.assertEqual(max_integer(test_m), 4444444444444445555555)

    def test_long_floats(self):
        """Test for list of long floats"""
        test_m = [
                2.34334343434343, .45555555555545, 45.555555553530593535,
                4.44444444444444555555523325, 2.323222222222222232]
        self.assertEqual(max_integer(test_m), 45.555555553530593535)

if __name__ == "__main__":
    unittest.main()
