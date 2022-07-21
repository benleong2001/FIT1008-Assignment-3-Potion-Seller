import unittest

from random_gen import RandomGen
from tester_base import TesterBase


class TestRandom(TesterBase):

    def test_run(self):
        r = RandomGen(seed=0)
        try:
            self.assertEqual(r.randint(100), 77)
        except AssertionError as e:
            print(str(e), 1)
        try:
            self.assertEqual(r.randint(100), 30)
        except AssertionError as e:
            print(str(e), 2)
        r = RandomGen(seed=25)
        try:
            self.assertEqual(r.randint(100), 69)
        except AssertionError as e:
            print(str(e), 3)

    def test_set_seed(self):
        """ Testing set_seed() method.
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        r = RandomGen()

        # Test 1: Valid Values
        valid_seeds = [-1, 0, 1]
        for seed in valid_seeds:
            # Setting value using Mutator Method
            try:
                r.set_seed(seed)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["RandomGen seed could not be set via set_seed() method: ", str(e)]))

            # Checking if value has been properly set
            try:
                self.assertEqual(r.seed, seed, "".join(
                    ["RandomGen seed value was not properly set: expected " + str(seed) + ", got seed = " + str(
                        r.seed)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Values
        invalid_seeds = [True, "0", valid_seeds]
        for seed in invalid_seeds:
            try:
                self.assertRaises(TypeError, r.set_seed, seed)
            except AssertionError:
                self.verificationErrors.append("set_seed() method does not handle invalid values properly.")

    def test_get_seed(self):
        """ Testing get_seed() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct seed value is returned.
        """
        r = RandomGen()
        values = [-1, 0, 1]
        for value in values:
            r.seed = value
            # Test 1
            try:
                seed = r.get_seed()
            except Exception as e:
                self.verificationErrors.append("".join(["get_seed() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(seed, value, "".join(
                    ["Incorrect seed value returned via get_seed() method: expected ", str(value), ", got ",
                     str(seed)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRandom)
    unittest.TextTestRunner(verbosity=0).run(suite)
