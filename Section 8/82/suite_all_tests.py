import unittest
from testAll import TestLogin


def suite():
    suite = unittest.TestSuite()
    # Login page tests
    suite.addTest(TestLogin('test_TC_L_001'))
    suite.addTest(TestLogin('test_TC_L_002'))
    suite.addTest(TestLogin('test_TC_L_003'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)