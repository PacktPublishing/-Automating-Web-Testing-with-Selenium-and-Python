import unittest

class TestExample(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(True)

    def test_example_2(self):
        self.assertTrue(False, 'example of failed test')

    @unittest.skip('example of skipped test')
    def test_example_3(self):
        self.assertTrue(True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample('test_example_1'))
    suite.addTest(TestExample('test_example_2'))
    suite.addTest(TestExample('test_example_3'))
    return suite

if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(suite())
