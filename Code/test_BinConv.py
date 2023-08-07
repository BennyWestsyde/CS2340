import unittest

from Dbl2Bin import dec_float2double_bin_float, double_bin_float2dec_float
from Half2Bin import dec_float2half_bin_float, half_bin_float2dec_float
from Int2Bin import dec_int2bin_int, bin_int2dec_int
from Sngl2Bin import dec_float2single_bin_float, single_bin_float2dec_float


class TestBinaryConversions(unittest.TestCase):
    def setUp(self) -> None:
        self.tolerance = 1e-5

    def test_dec_int2bin_int(self):
        # Test cases for integer conversions
        self.assertEqual(dec_int2bin_int("42"), "101010")
        self.assertEqual(bin_int2dec_int("101010"), "42")
        self.assertEqual(dec_int2bin_int(bin_int2dec_int("101010")), "101010")
        self.assertEqual(bin_int2dec_int(dec_int2bin_int("42")), "42")

    def test_half_precision(self):
        # Half precision
        tolerance = 1e-4
        self.assertEqual(dec_float2half_bin_float("65505.0"), "Alert: Overflow. The input number is larger than the largest possible number in half precision.")
        self.assertEqual(dec_float2half_bin_float("6.103515625e-06"), "Alert: Underflow. The input number is closer to zero than the smallest possible number in half precision.")
        half_bin_float = dec_float2half_bin_float("0.33333")
        self.assertAlmostEqual(float(half_bin_float2dec_float(half_bin_float)), 0.33333, delta=tolerance)
        
    def test_single_precision(self):
        # Single precision
        self.assertEqual(dec_float2single_bin_float("3.4028236e38"), "Alert: Overflow. The input number is larger than the largest possible number in single precision.")
        self.assertEqual(dec_float2single_bin_float("1.17549435e-39"), "Alert: Underflow. The input number is closer to zero than the smallest possible number in single precision.")
        single_bin_float = dec_float2single_bin_float("0.33333")
        self.assertAlmostEqual(float(single_bin_float2dec_float(single_bin_float)), 0.33333, delta=self.tolerance)

    def test_double_precision(self):
        # Double precision
        self.assertEqual(dec_float2double_bin_float("1.7976931348623158e308"), "Alert: Overflow. The input number is larger than the largest possible number in double precision.")
        self.assertEqual(dec_float2double_bin_float("2.2250738585072015e-309"), "Alert: Underflow. The input number is closer to zero than the smallest possible number in double precision.")
        double_bin_float = dec_float2double_bin_float("0.33333")
        self.assertAlmostEqual(float(double_bin_float2dec_float(double_bin_float)), 0.33333, delta=self.tolerance)

if __name__ == '__main__':
    unittest.main()
