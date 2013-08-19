__author__ = 'James Polera'
__email__ = 'james@uncryptic.com'
__since__ = '2013-08-18'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from srambler import scramble

class TestScrambler(unittest.TestCase):


    def test_string(self):
        self.assertNotEqual("James", scramble("James"))


    def test_int(self):
        self.assertNotEqual(42, scramble(42))


    def test_float(self):
        self.assertNotEqual(3.14, scramble(3.14))


    def test_currency(self):
        self.assertNotEqual("$3.50", scramble("$3.50"))


if __name__ == "__main__":
    unittest.main()