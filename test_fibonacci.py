import unittest

import fibonacci

##Unit testing with unittest
class test_function(unittest.TestCase):

    def test_fibonacci(self):

        #tests for fibonacci method
        self.assertEqual(fibonacci.fib(5), 8)
        self.assertEqual(fibonacci.fib(6), 13)
        self.assertEqual(fibonacci.fib(7), 21)

        #test for factorial method
        self.assertEqual(fibonacci.factorial(3), 6)

if __name__ == '__main__':
    unittest.main()









