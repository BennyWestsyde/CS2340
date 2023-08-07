import unittest

from Int2Bin import dec_int2bin_int, bin_int2dec_int
from BIntArth import bin_int_add, bin_int_sub, bin_int_mul, bin_int_div

class TestBinaryArithmetic(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def bin_int_add_test(self):
        bin1 = dec_int2bin_int(5)
        bin2 = dec_int2bin_int(6)
        expected = dec_int2bin_int(11)
        actual = bin_int_add(bin1, bin2)
        self.assertEqual(actual, expected)
    
    def bin_int_add_neg_test(self):
        bin1 = dec_int2bin_int(5)
        bin2 = dec_int2bin_int(-6)
        expected = dec_int2bin_int(-1)
        actual = bin_int_add(bin1, bin2)
        self.assertEqual(actual, expected)

    def bin_int_sub_test(self):
        bin1 = dec_int2bin_int(6)
        bin2 = dec_int2bin_int(5)
        expected = dec_int2bin_int(1)
        actual = bin_int_sub(bin1, bin2)
        self.assertEqual(actual, expected)

    def bin_int_sub_neg_test(self):
        bin1 = dec_int2bin_int(5)
        bin2 = dec_int2bin_int(-6)
        expected = dec_int2bin_int(11)
        actual = bin_int_sub(bin1, bin2)
        self.assertEqual(actual, expected)

    def bin_int_mul_test(self):
        bin1 = dec_int2bin_int(5)
        bin2 = dec_int2bin_int(6)
        expected = dec_int2bin_int(30)
        actual = bin_int_mul(bin1, bin2)
        self.assertEqual(actual, expected)

    def bin_int_mul_neg_test(self):
        bin1 = dec_int2bin_int(5)
        bin2 = dec_int2bin_int(-6)
        expected = dec_int2bin_int(-30)
        actual = bin_int_mul(bin1, bin2)
        self.assertEqual(actual, expected)
    
    def bin_int_div_test(self):
        bin1 = dec_int2bin_int(50)
        bin2 = dec_int2bin_int(5)
        expected = dec_int2bin_int(10)
        actual = bin_int_div(bin1, bin2)
        self.assertEqual(actual, expected)

    def bin_int_div_neg_test(self):
        bin1 = dec_int2bin_int(50)
        bin2 = dec_int2bin_int(-5)
        expected = dec_int2bin_int(-10)
        actual = bin_int_div(bin1, bin2)
        self.assertEqual(actual, expected)
