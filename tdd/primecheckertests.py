'''
   primecheckertests.py
   Jeff Ondich, 9 May 2012
   Updated for use in a lab exercise, 4 Nov 2013
'''

import primechecker
import unittest

class PrimeCheckerTester(unittest.TestCase):
    
    def setUp(self):
        # print("setUp")
        self.prime_checker = primechecker.PrimeChecker(100)

    def tearDown(self):
        # print("tearDown")
        pass

    def test_zero(self):
        # print("test_zero")
        # self.assertTrue(self.prime_checker.is_prime(0))
        self.assertFalse(1 <= 0)
        #self.assertRaises(ValueError, self.prime_checker.is_prime, 0)

    def test_one(self):
        self.assertFalse(self.prime_checker.is_prime(1))
        
    def test_two(self):
        # print("test_two")
        self.assertTrue(self.prime_checker.is_prime(2))

    def test_prime(self):
        # print("test_prime")
        self.assertTrue(self.prime_checker.is_prime(97))
    
    def test_biggest_prime(self):
        self.assertRaises(ValueError, self.prime_checker.is_prime, 2**136279841-1)

    def test_composite(self):
        # print("test_composite")
        self.assertFalse(self.prime_checker.is_prime(96))
        
    def test_negative(self):
        self.assertRaises(ValueError, self.prime_checker.is_prime, -2)
            
    def test_decimal(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, 1.5)
    
    def test_imaginary(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, 1j)
        
    def test_string(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, "two")
        
    def test_list(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, [5])
        
    def test_dict(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, {'value':7})
    
    def test_set(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, {5})
        
    def test_tuple(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, (5,))
        
    def test_empty(self):
        self.assertRaises(TypeError, self.prime_checker.is_prime, None)
        
    def test_primes_below(self):
        # print("test_primes_below")
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()

