import unittest

from main import number_hash

class number_hash_test(unittest.TestCase):
    def test_3_digits(self):
        self.assertEqual(number_hash(231),321-123)

    def test_5_digits(self):
        self.assertEqual(number_hash(32154),54321-12345)

    def test_7_digits(self):
        self.assertEqual(number_hash(6574132),7654321-1234567)