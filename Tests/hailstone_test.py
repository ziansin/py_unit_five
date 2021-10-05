import unittest
from hailstone import sequence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_hailstone(self):
        self.assertEqual(10, sequence(13))
        # Create two additional tests underneath this line


if __name__ == '__main__':
    unittest.main()
