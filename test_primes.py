import unittest

from primes import largest_prime
from tester_base import TesterBase


class TestPrimes(TesterBase):

    def test_some_valid_values(self):
        """ Testing with Valid Input Values.
        Test 1: Testing method call.
        Test 2: Testing if the correct value was returned.
        """
        inputs = [3, 20, 47]
        outputs = [2, 19, 43]
        for i, o in zip(inputs, outputs):
            try:
                p = largest_prime(i)
            except Exception as e:
                self.verificationErrors.append("".join(["largest_prime() was not executed: ", str(e)]))
                return

            try:
                self.assertEqual(p, o, "".join(["Incorrect number returned: Expected ", str(o), ", got ", str(p)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_some_invalid_values(self):
        """ Testing with Invalid Numerical Input Values. """
        bad_input_values = [-1, 0, 2, 100001]
        for bad_input in bad_input_values:
            try:
                self.assertRaises(ValueError, largest_prime, bad_input)
            except AssertionError:
                self.verificationErrors.append("largest_prime() method does not handle incorrect values of k properly.")

    def test_some_invalid_types(self):
        """ Testing with Invalid Value Types. """
        bad_input_types = [True, "bad input", [99991]]
        for bad_input in bad_input_types:
            try:
                self.assertRaises(TypeError, largest_prime, bad_input)
            except AssertionError:
                self.verificationErrors.append("largest_prime() method does not handle incorrect types of k properly.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimes)
    unittest.TextTestRunner(verbosity=0).run(suite)
