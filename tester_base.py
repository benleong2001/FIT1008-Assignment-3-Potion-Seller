import unittest


class TesterBase(unittest.TestCase):
    def setUp(self):
        """ The 'setUp' method is a frequently used method in unittest, and is called BEFORE every test case is run.
        This is useful when you want to create certain conditions before running a series of tests, without having to
        repeat code within those tests. Used in conjunction with tearDown to help ensure the test is isolated from
        the performance of other tests.

        Here it's just creating storage for any potential raised errors in the tests."""
        self.documentationErrors = []
        self.verificationErrors = []
        self.syntaxErrors = []
        print(self.id().split(".")[-1])

    def tearDown(self):
        """ The 'tearDown' is another frequently used method in unittest, and is called AFTER every test case is run.
        This is useful when you want to delete created instances or do other required tasks,
        without having to repeat code within those tests. Used in conjunction with setUp to help
        ensure the test is isolated from the performance of other tests.

        Here it's just printing off the errors that may have been stored in our list of errors, as well as the total
        number of errors.
        """
        print(self.__error_str(self.verificationErrors, "Verification"))

    def __error_str(self, error_list, error_type):
        s = ""
        for item in error_list:
            s += str(item) + "\n"
        s += f"Number of {error_type} Errors = " + str(len(error_list))
        return s
