import unittest

from hash_table import LinearProbePotionTable
from tester_base import TesterBase


class TestTable(TesterBase):

    def test_hash(self):
        """ Testing hash() method.
        Test 1: Testing hashing with good_hash()
        Test 2: Testing hashing with bad_hash()
        For each test:
            - Testing if method can be invoked.
            - Testing if the value returned is correct.

        |------|------|
        |  69  | 420  |
        |------|------|
        """
        # This sets the tablesize as 47 (24 * 2 = 48, greatest prime below 48 = 47)
        table = LinearProbePotionTable(24)
        potion_names, good_expected, bad_expected = ["hello", "aloha"], [46, 17], [20, 6]

        # Test 1: Using good_hash() to hash
        table.good_hash = True
        for name, output in zip(potion_names, good_expected):
            # Hashing name using hash() method
            try:
                hash_val = table.hash(name)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["hash value could not be produced via hash() method: ", str(e)]))
                return

            # Checking if value returned is correct
            try:
                self.assertEqual(hash_val, output, "".join(
                    ["Incorrect hash value returned by hash() method: expected ", str(output), ", got ",
                     str(hash_val)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Using bad_hash() to hash
        table.good_hash = False
        for name, output in zip(potion_names, bad_expected):
            # Hashing name using hash() method
            try:
                hash_val = table.hash(name)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["hash value could not be produced via hash() method: ", str(e)]))
                return

            # Checking if value returned is correct
            try:
                self.assertEqual(hash_val, output, "".join(
                    ["Incorrect hash value returned by hash() method: expected ", str(output), ", got ",
                     str(hash_val)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test___len__(self):
        """ Testing __len__() method.
        Test 1: Testing method call.
        Test 2: Testing if length returned is correct
        """
        table = LinearProbePotionTable(50)
        for i in range(1, 51):
            table.insert(str(i), i)
            # Test 1
            try:
                length = len(table)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Hash Table's length value could not be retrieved using __len__() method: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(length, i,
                                 "".join(["Incorrect length value returned: expected ", str(i), ", got ", str(length)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test___contains__(self):
        """" Testing __contains__() method.
        Test 1: Testing method call.
        Test 2: Testing if value returned is correct.
        """
        table = LinearProbePotionTable(10)
        table.insert("0", 0)
        table.insert("1", 1)
        input_values, outputs = ['0', '1', '2'], [True, True, False]
        for value, output in zip(input_values, outputs):
            # Test 1
            try:
                boolean = value in table
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["__contains__() method could not be invoked properly: ", str(e)]))
                return

            # Test 2
            try:
                self.assertEqual(boolean, output, "".join(
                    ["Incorrect value returned by __contains__() method: expected ", str(output), ", got ",
                     str(boolean)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test___getitem__(self):
        """ Testing __getitem__() method.
        Test 1: Testing valid keys.
            - Testing method call.
            - Testing if value returned is correct.
        Test 2: Testing invalid keys.
            - Testing if method can handle invalid keys properly.
        """
        table = LinearProbePotionTable(10)
        for i in range(5):
            table.insert(str(i), i)

        # Test 1: Valid Keys
        for j in range(5):
            # Retrieving item
            try:
                item = table[str(j)]
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["__getitem__() method could not be invoked properly: ", str(e)]))
                return

            # Checking if item returned is correct
            try:
                self.assertEqual(item, j, "".join(
                    ["Incorrect item value returned by __getitem__() method: expected ", str(j), ", got ", str(item)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid keys
        for k in range(6, 11):
            # Using invalid keys
            try:
                self.assertRaises(KeyError, table.__getitem__, str(k))
            except AssertionError:
                self.verificationErrors.append("__getitem__() method does not handle invalid keys properly.")

    def test_initialise_with_tablesize(self):
        """ Testing initialise_with_tablesize() method.
        Test 1: Testing method call.
        Test 2: Testing if count attribute was set properly.
        Test 3: Testing if length of table attribute was set properly.
        """
        table = LinearProbePotionTable(10)

        #
        try:
            table.initalise_with_tablesize(19)
        except Exception as e:
            self.verificationErrors.append(
                "".join(["initialise_with_tablesize() method could not be invoked properly: ", str(e)]))

        # Checking if count attribute was set properly
        try:
            self.assertEqual(table.count, 0, "".join([
                "Incorrect count attribute value was not set properly via "
                "initialise_with_tablesize() method: expected 0, got ",
                str(table.count)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Checking if table size was set properly
        try:
            self.assertEqual(len(table.table), 19, "".join(
                ["Size of table not set properly via initialise_with_tablesize() method: expected 19, got ",
                 str(len(table.table))]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_is_empty(self):
        """ Testing is_empty() method.
        Test 1: Testing when table is empty.
        Test 2: Testing when table is not empty.
        For each test:
            - Testing method call.
            - Testing if value returned is correct.
        """
        table = LinearProbePotionTable(10)
        # Test 1: Empty Table
        # Method call
        try:
            boolean = table.is_empty()
        except Exception as e:
            self.verificationErrors.append("".join(["is_empty() method could not be invoked properly: ", str(e)]))
            return

        # Checking if value returned is correct
        try:
            self.assertEqual(boolean, True, "".join(
                ["Incorrect value returned by is_empty() method: expected True, got ", str(boolean)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test 2: Non-Empty Table
        table.insert("0", 0)

        # Method call
        try:
            boolean = table.is_empty()
        except Exception as e:
            self.verificationErrors.append("".join(["is_empty() method could not be invoked properly: ", str(e)]))
            return

        # Checking if value returned is correct
        try:
            self.assertEqual(boolean, False, "".join(
                ["Incorrect value returned by is_empty() method: expected False, got ", str(boolean)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_is_full(self):
        """ Testing is_full() method.
        Test 1: Testing when table is not full.
        Test 2: Testing when table is full.
        For each test:
            - Testing method call.
            - Testing if value returned is correct.
        """
        table = LinearProbePotionTable(1, True, 2)
        # Testing Non-Full Table
        # Method call
        try:
            boolean = table.is_full()
        except Exception as e:
            self.verificationErrors.append("".join(["is_full() method could not be invoked properly: ", str(e)]))
            return

        # Checking if value returned is correct
        try:
            self.assertEqual(boolean, False, "".join(
                ["Incorrect value returned by is_full() method: expected False, got ", str(boolean)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Testing Full Table
        table.insert("0", 0)
        table.insert("1", 1)

        # Method call
        try:
            boolean = table.is_full()
        except Exception as e:
            self.verificationErrors.append("".join(["is_full() method could not be invoked properly: ", str(e)]))
            return

        # Checking if value returned is correct
        try:
            self.assertEqual(boolean, True, "".join(
                ["Incorrect value returned by is_full() method: expected True, got ", str(boolean)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_insert(self):
        """ Testing insert() method.
        Test 1: Testing method call.
        Test 2: Testing if the key is in the table
        Test 3: Testing if the data is in the table, with the key.
        """
        table = LinearProbePotionTable(10)
        for i in range(5):
            # Method Call
            try:
                table.insert(str(i), i)
            except Exception as e:
                self.verificationErrors.append("".join(["insert() method could not be invoked properly: ", str(e)]))

            # Checking if key was inserted into the table
            try:
                self.assertTrue(str(i) in table, "key value not inserted into table properly via insert() method.")
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            # Checking if data/value was assigned with the key as key, data pair into the table
            try:
                self.assertEqual(i, table[str(i)], "".join(
                    ["Value not properly assigned with key value via insert() method: expected ", str(i), ", got ",
                     str(table[str(i)])]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test___str__(self):
        """ Testing __str__() method.
        Test 1: Testing Method Call.
        Test 2: Testing if string representation returned is correct.
        """
        table = LinearProbePotionTable(5, False, 5)

        new_hash = lambda key: int(key)
        temp = table.hash
        table.hash = new_hash

        keys, items = ['0', '1', '2', '3', '4'], ["first", "second", "third", "fourth", "fifth"]
        for key, item in zip(keys, items):
            table.insert(key, item)

        # Method Call
        try:
            string = str(table)
        except Exception as e:
            self.verificationErrors.append("".join(["__str__() method could not be invoked properly: ", str(e)]))
            return

        # Checking if value returned is Correct
        try:
            expected = "(0, first)\n" \
                       "(1, second)\n" \
                       "(2, third)\n" \
                       "(3, fourth)\n" \
                       "(4, fifth)\n"
            self.assertEqual(string, expected, "".join(
                ["Incorrect string representation returned by __str__() method: expected ", str(expected), ", got ",
                 str(string)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        table.hash = temp

    def test_tablesize(self):
        c1 = LinearProbePotionTable(100, True, 120)
        c2 = LinearProbePotionTable(100, True, -1)
        # Should be exactly 120.
        self.assertEqual(len(c1.table), 120)
        # Should at least accommodate all positions.
        self.assertGreaterEqual(len(c2.table), 100)

    def test_stats(self):
        # Using a dictionary in the tester file for hash table ;)
        lookup = {
            "s1": 5,
            "s2": 5,
            "s3": 5,
            "s4": 7
        }
        h = lambda self, k: lookup[k]
        saved = LinearProbePotionTable.hash
        LinearProbePotionTable.hash = h
        # What the above code does is essentially work around using good_hash or bad hash.
        # This is the example given in the section on conflict and probe counting
        l = LinearProbePotionTable(10, True, 10)
        l["s1"] = "s1"
        l["s2"] = "s2"
        l["s3"] = "s3"
        l["s4"] = "s4"
        LinearProbePotionTable.hash = saved

        self.assertEqual(l.statistics(), (3, 4, 2))

    # We are putting the testers for Mutator and Accessor Methods at the bottom
    # as they are relatively insignificant compared to the other methods in the class.
    # Testing Mutator Methods
    def test_set_good_hash(self):
        """ Testing set_good_hash() method.
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        table = LinearProbePotionTable(10)

        # Test 1: Valid Values
        valid_values = [True, False]
        for value in valid_values:
            # Setting value using Mutator Method
            try:
                table.set_good_hash(value)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Hash Table's good_hash could not be set using set_good_hash() method: ", str(e)]))
                return

            # Checking if value has been properly set
            try:
                self.assertEqual(table.good_hash, value, "".join(
                    ["Hash Table's good_hash value was not properly set by set_good_hash() method: expected ",
                     str(value), ", got good_hash = ", str(table.good_hash)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Values
        invalid_values = [0, "Invalid Value", {}]
        for value in invalid_values:
            try:
                self.assertRaises(TypeError, table.set_good_hash, value)
            except AssertionError:
                self.verificationErrors.append("set_good_hash() method does not handle invalid values properly.")

    def test_set_table_size(self):
        """ Testing set_tablesize_override
        Test 1: Using valid values.
            Testing method call.
            Testing if attribute was properly set.
        Test 2: Using invalid values.
            Testing if method handles invalid values properly.
        """
        table = LinearProbePotionTable(10)

        # Test 1: Valid Values
        valid_values, outputs = [(10, -1), (10, 10)], [19, 10]
        for (max_pot, tbl_over), output in zip(valid_values, outputs):
            try:
                table.set_table_size(max_pot, tbl_over)
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Hash Table's tablesize could not be set using set_table_size() method: ", str(e)]))

            try:
                self.assertEqual(table.table_size, output, "".join(
                    ["Hash Table's table_size value was not properly set by set_table_size() method: expected ",
                     str(output), ", got good_hash = ", str(table.table_size)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        # Test 2: Invalid Input
        # Invalid Types
        invalid_types = [(True, 10), (12, "23"), ([10], False)]
        for max_pot, tbl_over in invalid_types:
            try:
                self.assertRaises(TypeError, table.set_table_size, max_pot, tbl_over)
            except AssertionError:
                self.verificationErrors.append("set_table_size() does not handle invalid types properly.")

        # Invalid Values
        invalid_values = [(10, 9), (-1, 10)]
        for max_pot, tbl_over in invalid_values:
            try:
                self.assertRaises(ValueError, table.set_table_size, max_pot, tbl_over)
            except AssertionError:
                self.verificationErrors.append("set_table_size() does not handle invalid numerical values properly.")

    # Testing Accessor Methods
    def test_get_good_hash(self):
        """ Testing get_good_hash() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct good_hash value is returned.
        """
        table = LinearProbePotionTable(10)
        values = [True, False]
        for value in values:
            table.good_hash = value
            # Test 1
            try:
                good_hash = table.get_good_hash()
            except Exception as e:
                self.verificationErrors.append("get_good_hash() method could not be invoked properly: ", str(e))
                return

            # Test 2
            try:
                self.assertEqual(good_hash, value, "".join(
                    ["Incorrect good_hash value returned via get_good_hash() method: expected ", str(value), ", got ",
                     str(good_hash)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_table_size(self):
        """ Testing get_table_size() method.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct table_size value is returned.
        """
        table = LinearProbePotionTable(10)
        for value in range(1, 101):
            table.table_size = value
            # Test 1
            try:
                table_size = table.get_table_size()
            except Exception as e:
                self.verificationErrors.append("get_table_size() method could not be invoked properly: ", str(e))
                return

            # Test 2
            try:
                self.assertEqual(table_size, value, "".join(
                    ["Incorrect table_size value returned via get_table_size() method: expected ", str(value), ", got ",
                     str(table_size)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_comparison_hash_statistics(self):
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

        # Creating two tables, one for good_hash(), one for bad_hash()
        good_table = LinearProbePotionTable(330, True, -1)
        bad_table = LinearProbePotionTable(330, False, -1)

        # Selecting a table to insert values in
        for table in [good_table, bad_table]:
            # Going through the list of key values
            for key in lst:
                # Inserting the keys into the selected table
                table.insert(key, key)
        good_conflict_count, good_probe_total, good_probe_max = good_table.statistics()
        bad_conflict_count, bad_probe_total, bad_probe_max = bad_table.statistics()
        print("".join(["---------------------\n",
                       "GOOD TABLE",
                       "\n---------------------",
                       "\nconflict_count: ", str(good_conflict_count),
                       "\nprobe_total:    ", str(good_probe_total),
                       "\nprobe_max:      ", str(good_probe_max),
                       "\n---------------------",
                       "\n\n---------------------\n",
                       "BAD TABLE",
                       "\n---------------------",
                       "\nconflict_count: ", str(bad_conflict_count),
                       "\nprobe_total:    ", str(bad_probe_total),
                       "\nprobe_max:      ", str(bad_probe_max),
                       "\n---------------------\n"]))
        return "".join(["GOOD TABLE",
                        "\nconflict_count: ", str(good_conflict_count),
                        "\nprobe_total:    ", str(good_probe_total),
                        "\nprobe_max:      ", str(good_probe_max),
                        "\n\nBAD TABLE",
                        "\nconflict_count: ", str(bad_conflict_count),
                        "\nprobe_total:    ", str(bad_probe_total),
                        "\nprobe_max:      ", str(bad_probe_max)])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTable)
    unittest.TextTestRunner(verbosity=0).run(suite)
