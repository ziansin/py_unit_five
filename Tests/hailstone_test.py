import unittest
from hailstone import sequence


class MyTestCase(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    """

    def test_hailstone(self):
        self.assertEqual(9, sequence(13))
        self.assertEqual(1, sequence(2))
        self.assertEqual(0, sequence(1))


if __name__ == '__main__':
    unittest.main()
