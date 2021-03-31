import unittest
from pythonds_functions.infix_to_postfix import infix_to_postfix as i2p

class BasicTest(unittest.TestCase):
    def setUp(self):
        print("===========================================================")
        print(self._testMethodName)

    # basic run thru most of the StackLL functions
    def test_i2p(self):
        # Do some basic test cases
        test1 = i2p("( A + B ) * ( C + D )")
        print(f"test1: {test1}")
        self.assertEqual(test1, "A B + C D + *", f'Value not matching: received {test1} expected A B + C D + *')
        test2 = i2p("( A + B ) * C")
        print(f"test2: {test2}")
        self.assertEqual(test2, "A B + C *", f'Value not matching: received {test2} expected A B + C *')
        test3 = i2p("A + B * C")
        print(f"test3: {test3}")
        self.assertEqual(test3, "A B C * +", f'Value not matching: received {test3} expected A B C * +')
