import unittest

import fibonacci

class test_function(unittest.TestCase):

    def test_fibonacci(self):

        self.assertEqual(fibonacci.fib(5), 8)
        self.assertEqual(fibonacci.fib(6), 13)
        self.assertEqual(fibonacci.fib(7), 21)

def test_fib(self):
    assert fibonacci.fib(5) == 8

if __name__ == '__main__':
    unittest.main()



