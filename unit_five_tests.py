import unittest
import for_loops
import multiplication
import multiples
import fibonacci
import hailstone


class MyTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual("0 1 2 3 4 5 6 ", for_loops.count(0, 6))
        self.assertEqual("10 9 8 7 6 ", for_loops.count(10, 6))
        self.assertEqual("3 ", for_loops.count(3, 3))

    def test_multiplication_tables(self):
        self.assertEqual("6 12 18 24 30 36 42 48 54 60 66 72 ", multiplication.multiplication_table(6))
        # Create two additional tests underneath this line

    def test_multiples(self):
        self.assertEqual(233168, multiples.get_sum(1000))

    def test_fibonacci(self):
        self.assertEqual("1 1 2 3 5 ", fibonacci.fibonacci(5))
        self.assertEqual("1 ", fibonacci.fibonacci(1))
        self.assertEqual("1 1 ", fibonacci.fibonacci(2))
        # Create two additional tests underneath this line

    def test_hailstone(self):
        self.assertEqual(10, hailstone.sequence(13))
        # Create two additional tests underneath this line





if __name__ == '__main__':
    unittest.main()
