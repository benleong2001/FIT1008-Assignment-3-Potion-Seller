import unittest

from potion import Potion
from tester_base import TesterBase


class TestPotion(TesterBase):
    tester_potion = Potion("type", "name", 1, 0)

    def test_creation(self):
        """ Testing __init__() and create_empty() methods.
        The tests are done in 2 stages:
            Testing instantiation
            Testing if attributes were initialised properly
        """
        test_potion_type = "Buff"
        test_potion_name = "Potion of Extreme Speed"
        test_potion_buy_price = 40
        test_potion_quantity = 4

        # Instantiating Potion via Potion.__init__() aka constructor
        try:
            p_init = Potion(test_potion_type, test_potion_name, test_potion_buy_price, test_potion_quantity)
        except Exception as e:
            self.verificationErrors.append("".join(["Potion could not be instantiated via constructor: ", str(e)]))
            return

        # Checking Potion potion_type value
        try:
            self.assertEqual(p_init.potion_type, test_potion_type,
                             "".join(["Potion type was not properly initialised via constructor. Expected",
                                      str(test_potion_type), ", got"]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion name value
        try:
            self.assertEqual(p_init.name, test_potion_name, "".join(
                ["Potion name was not properly initialised via constructor. Expected", str(test_potion_name), ", got ",
                 str(p_init.name)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion buy_price value
        try:
            self.assertEqual(p_init.buy_price, test_potion_buy_price, "".join(
                ["Potion buy_price was not properly initialised via constructor. Expected ", str(test_potion_buy_price),
                 ", got ", str(p_init.buy_price)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion quantity value
        try:
            self.assertEqual(p_init.quantity, test_potion_quantity, "".join(
                ["Potion quantity was not properly initialised via constructor. Expected ", str(test_potion_quantity),
                 ", got ", str(p_init.quantity)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        test_potion_name_empty = "Potion of Regeneration"
        test_potion_type_empty = "Health"
        test_potion_buy_price_empty = 20

        # Instantiating Potion via create_empty()
        try:
            p_empty = Potion.create_empty(test_potion_type_empty, test_potion_name_empty, test_potion_buy_price_empty)
        except Exception as e:
            self.verificationErrors.append("".join(["Potion could not be instantiated via create_empty(): ", str(e)]))
            return

        # Checking Potion potion_type
        try:
            self.assertEqual(p_empty.potion_type, test_potion_type_empty, "".join(
                ["Potion type was not properly initialised via create_empty(). Expected ", str(test_potion_type_empty),
                 ", got ", str(p_empty.potion_type)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion name
        try:
            self.assertEqual(p_empty.name, test_potion_name_empty, "".join(
                ["Potion name was not properly initialised via create_empty(). Expected ", str(test_potion_name_empty),
                 ", got ", str(p_empty.name)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion buy_price
        try:
            self.assertEqual(p_empty.buy_price, test_potion_buy_price_empty, "".join(
                ["Potion buy_price was not properly initialised via create _empty(). Expected ",
                 str(test_potion_buy_price_empty), ", got ", str(p_empty.buy_price)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking Potion quantity
        try:
            self.assertEqual(p_empty.quantity, 0, "".join(
                ["Potion quantity was not set to 0 via create_empty(). Expected 0, got ", str(p_empty.quantity)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Testing Mutator Methods
    def test_set_potion_type(self):
        """ Testing set_potion_type() method.
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        # Test 1: Valid Values
        valid_values = ["Buff", "Resistance", "Healing"]
        for value in valid_values:
            # Setting value using Mutator Method
            try:
                TestPotion.tester_potion.set_potion_type(value)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Potion type could not be set using set_potion_type(): ", str(e)]))
                return

            # Checking if value has been properly set
            try:
                self.assertEqual(TestPotion.tester_potion.potion_type, value, "".join(
                    ["Potion type was not properly set by set_potion_type(): potion_type = ",
                     str(TestPotion.tester_potion.potion_type)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Values
        invalid_values = [100, True, ["Buff"]]
        for value in invalid_values:
            try:
                self.assertRaises(TypeError, TestPotion.tester_potion.set_potion_type, value)
            except AssertionError:
                self.verificationErrors.append("set_potion_type() method does not handle invalid values properly.")

    def test_set_name(self):
        """ Testing set_name() method.
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        # Test 1: Valid Values
        valid_values = ["Potion of Healing", "Potion of Fire Resistance", "Potion of Strength"]
        for value in valid_values:
            # Setting value using Mutator Method
            try:
                TestPotion.tester_potion.set_name(value)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Potion name could not be set using set_name(): ", str(e)]))
                return

            # Checking if value has been properly set
            try:
                self.assertEqual(TestPotion.tester_potion.name, value, "".join(
                    ["Potion name was not properly set by set_name(): name = ",
                     str(TestPotion.tester_potion.name)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Values
        invalid_values = [100, True, ["Potion of Invalid"]]
        for value in invalid_values:
            # Testing if the method handles invalid values properly
            try:
                self.assertRaises(TypeError, TestPotion.tester_potion.set_name, value)
            except AssertionError:
                self.verificationErrors.append("set_name() method does not handle invalid values properly.")

    def test_set_buy_price(self):
        """ Testing set_buy_price() method.
         Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        # Test 1: Valid Values
        valid_values = [1, 3.1415, pow(2, 16)]
        for value in valid_values:
            # Setting value using Mutator Method
            try:
                TestPotion.tester_potion.set_buy_price(value)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Potion buy_price could not be set using set_buy_price(): ", str(e)]))
                return

            # Checking if value has been properly set
            try:
                self.assertEqual(TestPotion.tester_potion.buy_price, value, "".join(
                    ["Potion buy_price was not properly set by set_buy_price(): expected ", str(value),
                     ", got buy_price = ", str(TestPotion.tester_potion.buy_price)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Values
        invalid_values = ['100', True, [40]]
        for value in invalid_values:
            # Testing if the method handles invalid values properly
            try:
                self.assertRaises(TypeError, TestPotion.tester_potion.set_buy_price, value)
            except AssertionError:
                self.verificationErrors.append("set_buy_price() method does not handle invalid values properly.")

    def test_set_quantity(self):
        """ Testing set_quantity method.
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
                Using invalid type
                Using invalid numerical value
        """
        # Test 1: Valid Values
        valid_values = [1, 3.1415, pow(2, 16)]
        for value in valid_values:
            # Setting value using Mutator Method
            try:
                TestPotion.tester_potion.set_quantity(value)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Potion name could not be set using set_quantity(): ", str(e)]))
                return

            # Checking if value has been properly set
            try:
                self.assertEqual(TestPotion.tester_potion.quantity, value, "".join(
                    ["Potion quantity was not properly set by set_quantity(): expected ", str(value),
                     ", got quantity = ", str(TestPotion.tester_potion.quantity)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Inputs
        # Invalid Types
        invalid_values_type = ['100', True, ["Potion of Invalid"]]
        for value in invalid_values_type:
            # Testing if the method handles invalid values properly
            try:
                self.assertRaises(TypeError, TestPotion.tester_potion.set_quantity, value)
            except AssertionError:
                self.verificationErrors.append("set_quantity() method does not handle invalid types properly.")

        # Invalid Numerical Values
        invalid_values_numerically = [-1, -0.5, -pow(2, 16)]
        for value in invalid_values_numerically:
            # Testing if the method handles invalid values properly
            try:
                self.assertRaises(ValueError, TestPotion.tester_potion.set_quantity, value)
            except AssertionError:
                self.verificationErrors.append(
                    "set_quantity() method does not handle invalid numerical values properly.")

    def test_get_potion_type(self):
        """ Testing get_potion_type() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct potion_type value is returned.
        """
        values = ["Buff", "Resistance", "Healing"]
        for value in values:
            TestPotion.tester_potion.potion_type = value
            # Test 1
            try:
                potion_type = TestPotion.tester_potion.get_potion_type()
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["get_potion_type() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(potion_type, value, "".join(
                    ["Incorrect potion_type value returned via get_potion_type() method: expected ", str(value),
                     ", got ", str(potion_type)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_name(self):
        """ Testing get_name() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct name value is returned.
        """
        values = ["Potion of Healing", "Potion of Fire Resistance", "Potion of Strength"]
        for value in values:
            TestPotion.tester_potion.name = value
            # Test 1
            try:
                name = TestPotion.tester_potion.get_name()
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["get_name() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(name, value, "".join(
                    ["Incorrect name value returned via get_name() method: expected ", str(value), ", got ",
                     str(name)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_buy_price(self):
        """ Testing get_buy_price()
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct buy_price value is returned.
        """
        values = [1, 3.1415, pow(2, 16)]
        for value in values:
            TestPotion.tester_potion.buy_price = value
            # Test 1
            try:
                buy_price = TestPotion.tester_potion.get_buy_price()
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["get_buy_price() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(buy_price, value, "".join(
                    ["Incorrect buy_price value returned via get_buy_price() method: expected ", str(value), ", got ",
                     str(buy_price)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_quantity(self):
        """ Testing get_quantity() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct quantity value is returned.
        """
        values = [1, 3.1415, pow(2, 16)]
        for value in values:
            TestPotion.tester_potion.quantity = value
            # Test 1
            try:
                quantity = TestPotion.tester_potion.get_quantity()
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["get_quantity() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(quantity, value, "".join(
                    ["Incorrect quantity value returned via get_quantity() method: expected ", str(value), ", got ",
                     str(quantity)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_good_hash(self):
        """ Testing good_hash() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct hash value is produced from the method.

        Prove that the expected values are correct:
        a = 31415       b = 27183
        let tablesize = 47
        a = a * b % (tablesize - 1)
        a1 = 31415
        a2 = 31415 * 27183 % (47 - 1) = 9
        a3 = 9 * 27183 % (47 - 1) = 19
        a4 = 19 * 27183 % (47 - 1) = 35
        a5 = 35 * 27183 % (47 - 1) = 33

        let potion_name be "hello"                      let potion_name be "aloha"
        h - 104                                         a - 97
        e - 101                                         l - 108
        l - 108                                         o - 111
        o - 111                                         h - 104

        value = (ord(char) + a * value) % tablesize
        value = 104 % 47 = 10                           value = 97 % 47 = 3
        = (101 + 9 * 10) % 47 = 3                       = (108 + 9 * 3) % 47 = 41
        = (108 + 19 * 3)  % 47 = 24                     = (111 + 19 * 41) % 47 = 44
        = (108 + 35 * 24) % 47 = 8                      = (104 + 35 * 44) % 47 = 46
        = (111 + 33 * 8) % 47 = 46                      = (97 + 33 * 46) % 47 = 17
        """
        potion_names = ["hello", "aloha"]
        hash_values = [46, 17]
        tablesize = 47
        for potion_name, hash_value in zip(potion_names, hash_values):
            # Hashing the potion name
            try:
                index = TestPotion.tester_potion.good_hash(potion_name, tablesize)
            except Exception as e:
                self.verificationErrors.append("".join(["Hash value could not be produced: ", str(e)]))
                return

            # Checking if the correct hash value is returned
            try:
                self.assertEqual(hash_value, index, "".join(
                    ["good_hash() did not produce the correct hash value: expected ", str(hash_value), ", got ",
                     str(index)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_bad_hash(self):
        """ Testing bad_hash() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct hash value is produced from the method.

        Prove that the expected values are correct:
        a = 2
        Let tablesize = 47

        let potion_name be "hello"                      let potion_name be "aloha"
        h - 104                                         a - 97
        value = 104 * 2 % 47 = 20                       value = 97 * 2 % 47 = 6
        """
        potion_names = ["hello", "aloha"]
        hash_values = [20, 6]
        tablesize = 47
        for potion_name, hash_value in zip(potion_names, hash_values):
            # Hashing the potion name
            try:
                index = TestPotion.tester_potion.bad_hash(potion_name, tablesize)
            except Exception as e:
                self.verificationErrors.append("".join(["Hash value could not be produced: ", str(e)]))
                return

            # Checking if the correct hash value is returned
            try:
                self.assertEqual(hash_value, index, "".join(
                    ["bad_hash() did not produce the correct hash value: expected ", str(hash_value), ", got ",
                     str(index)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_comparison_hash_spread(self):
        """ This is not a tester method!!!
        This method is used in order to test the spread of the good_hash() and the bad_hash().
        Refer to the analysis file, analysis.pdf, to see the details of the output
           H    A    S    H         V    A    L    U    E    S"
        |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |
        --------------------------------------------------------
        """
        # A list of 5 letter strings, used as key values to be hashed by the hash functions
        lst = ['aback', 'abase', 'abate', 'abbey', 'abyss', 'acute', 'adobe', 'agate', 'agree', 'ahead', 'allow',
               'aloft', 'alone', 'altar', 'ample', 'argue', 'aroma', 'aside', 'askew', 'audit', 'awake', 'badge',
               'badly', 'banal', 'basic', 'baton', 'batty', 'belch', 'belly', 'bench', 'biome', 'black', 'bleed',
               'bloke', 'blurt', 'blush', 'booby', 'boost', 'boozy', 'brake', 'break', 'briar', 'bribe', 'brine',
               'bring', 'canny', 'cargo', 'cater', 'caulk', 'champ', 'chant', 'cheat', 'cheek', 'chest', 'chill',
               'choke', 'chunk', 'cigar', 'civic', 'click', 'clock', 'cloth', 'cluck', 'coast', 'colon', 'comet',
               'comma', 'conic', 'corny', 'could', 'crank', 'crass', 'crate', 'craze', 'crazy', 'crimp', 'croak',
               'crust', 'cynic', 'death', 'delta', 'depot', 'digit', 'dodge', 'dowry', 'dozen', 'drain', 'drink',
               'duchy', 'dutch', 'dwarf', 'elder', 'enema', 'epoch', 'epoxy', 'erode', 'error', 'essay', 'evade',
               'exult', 'farce', 'favor', 'feign', 'ferry', 'fewer', 'finer', 'first', 'fixer', 'fjord', 'flair',
               'flesh', 'flick', 'fling', 'floss', 'flume', 'focal', 'focus', 'foray', 'forge', 'forgo', 'forth',
               'found', 'foyer', 'frame', 'fresh', 'front', 'gamma', 'gaudy', 'gecko', 'golem', 'goner', 'gorge',
               'gouge', 'grade', 'great', 'greet', 'grime', 'gripe', 'groin', 'group', 'growl', 'guild', 'hairy',
               'hatch', 'heath', 'heist', 'helix', 'heron', 'hoard', 'homer', 'humor', 'humph', 'hyper', 'inert',
               'islet', 'ivory', 'jaunt', 'karma', 'kebab', 'knoll', 'labor', 'lapel', 'lapse', 'larva', 'light',
               'linen', 'loopy', 'lowly', 'lowly', 'lusty', 'lying', 'major', 'marry', 'masse', 'maxim', 'metal',
               'midst', 'mimic', 'mince', 'model', 'moist', 'month', 'motor', 'moult', 'mount', 'mourn', 'movie',
               'nasty', 'natal', 'naval', 'nymph', 'offal', 'olive', 'other', 'ought', 'outdo', 'oxide', 'panel',
               'panic', 'paper', 'parry', 'pause', 'peach', 'perch', 'perky', 'picky', 'pilot', 'pithy', 'plant',
               'pleat', 'pluck', 'point', 'pound', 'prick', 'pride', 'print', 'prove', 'proxy', 'pulpy', 'purge',
               'query', 'quiet', 'radio', 'react', 'rebus', 'rebut', 'renew', 'repay', 'retch', 'rhino', 'robin',
               'robot', 'rogue', 'rouge', 'round', 'royal', 'rupee', 'salad', 'saute', 'scare', 'seedy', 'serve',
               'shake', 'shall', 'shame', 'shard', 'shine', 'shire', 'shown', 'shrub', 'siege', 'sissy', 'skill',
               'slosh', 'slump', 'slung', 'smart', 'smelt', 'snout', 'solar', 'solve', 'sonic', 'sower', 'spend',
               'spicy', 'spike', 'spill', 'spray', 'squad', 'staff', 'stair', 'stand', 'start', 'steed', 'stink',
               'stool', 'store', 'story', 'stout', 'stove', 'sugar', 'surer', 'sweet', 'swill', 'swirl', 'tacit',
               'tangy', 'tapir', 'tease', 'their', 'thorn', 'those', 'thumb', 'tiger', 'tilde', 'tipsy', 'today',
               'totem', 'trace', 'train', 'trash', 'trawl', 'triad', 'troll', 'trope', 'trove', 'truss', 'tweed',
               'ulcer', 'ultra', 'unfed', 'unify', 'unmet', 'usher', 'using', 'viral', 'vital', 'vivid', 'vodka',
               'watch', 'weary', 'whack', 'whelp', 'wince', 'wooer', 'world', 'wrote', 'wrung', 'yearn', 'zesty']
        tablesize = 11
        good_count_list = [0] * tablesize
        bad_count_list = [0] * tablesize
        for name in lst:
            i = TestPotion.tester_potion.good_hash(name, tablesize)
            j = TestPotion.tester_potion.bad_hash(name, tablesize)
            good_count_list[i] += 1
            bad_count_list[j] += 1

        title = "\n              H    A    S    H         V    A    L    U    E    S\n"
        line = "            --------------------------------------------------------\n"
        final_string = "hash values |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |\n"
        good_string = "good_hash()" + "".join(
            [" |  " + str(num) if len(str(num)) == 1 else " | " + str(num) for num in good_count_list]) + " |\n"
        bad_string = "bad_hash() " + "".join(
            [" |  " + str(num) if len(str(num)) == 1 else " | " + str(num) for num in bad_count_list]) + " |\n"
        print("".join([title, line, final_string, line, good_string, line, bad_string, line]))
        print("* the table above is used for the hash table analysis")
        return good_count_list, bad_count_list


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPotion)
    unittest.TextTestRunner(verbosity=0).run(suite)
