
import unittest
from num2w import Num2w


class MyTestCase(unittest.TestCase):
    """
    The black box testing technique is mainly used to examine
    the overall functionality of the application.
    """

    def testBoundary1(self):
        # Test for the value on the lower boundary.
        nn = Num2w()
        try:
            nn.low_high(0)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def testBoundary2(self):
        # Test for the value on the higher boundary.
        nn = Num2w()
        try:
            nn.low_high(100)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def testOver100(self):
        # Test for the values higher than 100.
        nn = Num2w()
        try:
            nn.low_high(120)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def testLower0(self):
        # Test for the values lower than 0.
        nn = Num2w()
        try:
            nn.low_high(-2)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def testOtherValue1(self):
        # Test for the float values entered by user.
        nn = Num2w()
        try:
            nn.low_high(1.5)
            self.assertTrue(True)
        except:
            self.assertFalse(False)

    def testOtherValue2(self):
        # Test for the string values entered by user.
        nn = Num2w()
        try:
            nn.low_high('test')
            self.assertTrue(True)
        except:
            self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
