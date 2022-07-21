import unittest

from avl import AVLTree
from node import AVLTreeNode
from tester_base import TesterBase


class TestAVL(TesterBase):

    def test_run_through(self):
        self.b = AVLTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        # self.b.draw()
        """
        15
        ╟─5
        ║ ╟─3
        ║ ║ ╟─
        ║ ║ ╙─4
        ║ ╙─10
        ╙─20
          ╟─17
          ╙─22
        """
        self.assertEqual(self.b.root.item, "A")
        self.assertEqual(self.b.root.left.left.item, "F")
        self.assertEqual(self.b.root.right.left.item, "D")
        self.assertEqual(self.b.root.left.right.item, "B")

        del self.b[20]
        del self.b[17]

        # self.b.draw()
        """
        5
        ╟─3
        ║ ╟─
        ║ ╙─4
        ╙─15
          ╟─10
          ╙─22
        """
        self.assertEqual(self.b.root.item, "E")
        self.assertEqual(self.b.root.right.left.item, "B")
        self.assertEqual(self.b.root.left.item, "F")

    def test_kth(self):
        self.b = AVLTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        self.assertEqual([self.b.kth_largest(x).key for x in range(1, 9)], [22, 20, 17, 15, 10, 5, 4, 3])

    def test_get_height(self):
        """ Testing get_height() method.
        Setup: Adding nodes to an empty AVL Tree
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct height is returned by the method.
        """
        # Setup
        self.test_height_tree = AVLTree()
        self.test_height_tree[25] = "Node 1"
        self.test_height_tree[20] = "Node 2"
        self.test_height_tree[15] = "Node 3"
        self.test_height_tree[17] = "Node 4"
        self.test_height_tree[5] = "Node 5"

        # Testing get_height() method
        try:
            h = self.test_height_tree.get_height(self.test_height_tree.root)
        except Exception as e:
            self.verificationErrors.append("".join(["Height of tree could not be accessed via get_height(): ", str(e)]))
            return

        # Checking if value returned is correct
        try:
            self.assertEqual(h, 2, "".join(
                ["Incorrect height value returned via get_height() method: expected 2, got ", str(h)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_balance(self):
        """ Testing get_balance() method.
        Setup: Adding nodes to an empty AVL Tree.
        Test 1: Testing if the method can be invoked.
        Test 2: Testing if the correct balance value is returned.
        """
        # Setup
        self.test_balance_tree = AVLTree()
        self.test_balance_tree[20] = "Node 1"
        self.test_balance_tree[25] = "Node 2"
        self.test_balance_tree[15] = "Node 3"
        self.test_balance_tree[17] = "Node 4"
        # self.test_balance_tree.draw()
        """
        20
        ╟─15
        ║ ╟─
        ║ ╙─17
        ╙─25
        """
        keys = [15, 20, 25]
        balances = [1, -1, 0]

        for key, balance in zip(keys, balances):
            # Getting balance value of the tree
            try:
                returned_balance = self.test_balance_tree.get_balance(self.test_balance_tree.get_tree_node_by_key(key))
            except Exception as e:
                self.verificationErrors.append(
                    "".join(["Balance value could not be retrieved via get_balance() method: ", str(e)]))
                return

            # Checking if value returned is correct
            try:
                self.assertEqual(returned_balance, balance, "".join(
                    ["Incorrect balance value returned via get_balance() method: expected ", str(balance),
                     " for key = ", str(key), ", got ", str(returned_balance)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_left_rotate(self):
        """ Testing left_rotate() method.
        Setup: Adding nodes to an empty tree to simulate this:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

        Test 1: To perform a left rotation
        Test 2: Test if the nodes end up in the correct place
        """
        # Setup
        self.test_left_tree = AVLTree()
        self.test_left_tree.root = AVLTreeNode(2, "current")
        self.test_left_tree.root.right_count = 3
        self.test_left_tree.root.left = AVLTreeNode(1, "l-tree")
        self.test_left_tree.root.right = AVLTreeNode(4, "child")
        self.test_left_tree.root.right.right_count = 1
        self.test_left_tree.root.right.left = AVLTreeNode(3, "center")
        self.test_left_tree.root.right.right = AVLTreeNode(5, "r-tree")

        # Performing left rotation
        try:
            self.test_left_tree.root = self.test_left_tree.left_rotate(self.test_left_tree.root)
        except Exception as e:
            self.verificationErrors.append(
                "".join(["Left rotation could not be performed onto the tester AVL tree: ", str(e)]))
            return

        # Checking if the nodes are in the correct positions
        try:  # root = child
            self.assertEqual(self.test_left_tree.root.item, "child",
                             "".join(["Incorrect root node item: expected child, got ",
                                      str(self.test_left_tree.root.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:  # root left = current
            self.assertEqual(self.test_left_tree.root.left.item, "current",
                             "".join(["Incorrect left node item: expected current, got ",
                                      str(self.test_left_tree.root.left.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:  # root right = r-tree
            self.assertEqual(self.test_left_tree.root.right.item, "r-tree",
                             "".join(["Incorrect right node item: expected r-tree, got ",
                                      str(self.test_left_tree.root.right.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:  # root left left = l-tree
            self.assertEqual(self.test_left_tree.root.left.left.item, "l-tree", "".join(
                ["Incorrect left, left node item: expected l-tree, got ",
                 str(self.test_left_tree.root.left.left.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:  # root left right = center
            self.assertEqual(self.test_left_tree.root.left.right.item, "center", "".join(
                ["Incorrect left, right node item: expected center, got ",
                 str(self.test_left_tree.root.left.right.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_right_rotate(self):
        """ Testing right_rotate() method.
        Setup: Adding nodes to an empty tree to simulate this:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

        Test 1: To perform a right rotation
        Test 2: Test if the nodes end up in the correct place
        """
        # Setup
        self.test_right_tree = AVLTree()
        self.test_right_tree.root = AVLTreeNode(4, "current")
        self.test_right_tree.root.right_count = 1
        self.test_right_tree.root.left = AVLTreeNode(2, "child")
        self.test_right_tree.root.left.right_count = 1
        self.test_right_tree.root.right = AVLTreeNode(5, "r-tree")
        self.test_right_tree.root.left.left = AVLTreeNode(1, "l-tree")
        self.test_right_tree.root.left.right = AVLTreeNode(3, "center")

        # Performing left rotation
        try:
            self.test_right_tree.root = self.test_right_tree.right_rotate(self.test_right_tree.root)
        except Exception as e:
            self.verificationErrors.append(
                "".join(["Left rotation could not be performed onto the tester AVL tree: ", str(e)]))
            return

        # Checking if the nodes are in the correct positions
        try:
            self.assertEqual(self.test_right_tree.root.item, "child",
                             "".join(["Incorrect root node item: expected child, got ",
                                      str(self.test_right_tree.root.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(self.test_right_tree.root.left.item, "l-tree",
                             "".join(["Incorrect left node item: expected current, got ",
                                      str(self.test_right_tree.root.left.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(self.test_right_tree.root.right.item, "current",
                             "".join(["Incorrect right node item: expected r-tree, got ",
                                      str(self.test_right_tree.root.right.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(self.test_right_tree.root.right.left.item, "center", "".join(
                ["Incorrect left, left node item: expected l-tree, got ",
                 str(self.test_right_tree.root.right.left.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        try:
            self.assertEqual(self.test_right_tree.root.right.right.item, "r-tree", "".join(
                ["Incorrect left, right node item: expected center, got ",
                 str(self.test_right_tree.root.right.right.item)]))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_rebalance(self):
        """ Testing rebalance() method.
        Setup: Adding nodes to an empty tree.
        Test 1: Testing re-balancing an unbalanced tree.
        Test 2: Checking if the tree is balanced after re-balancing.
        There will be two versions of this:
            - Using left rotation only
            - Using right, left rotation
        """
        # Setup
        self.test_l_bal_tree = AVLTree()
        self.test_l_bal_tree.root = AVLTreeNode(10, "Node 10")
        self.test_l_bal_tree.root.right_count = 2
        self.test_l_bal_tree.root.height = 2
        self.test_l_bal_tree.root.right = AVLTreeNode(15, "Node 15")
        self.test_l_bal_tree.root.right.right_count = 1
        self.test_l_bal_tree.root.right.right = AVLTreeNode(20, "Node 20")
        self.test_l_bal_tree.root.right.right.height = 0
        """
        10
        ╟─15
        ║ ╟─20
        ║ ╙─
        ╙─
        """

        self.test_rl_bal_tree = AVLTree()
        self.test_rl_bal_tree.root = AVLTreeNode(10, "Node 10")
        self.test_rl_bal_tree.root.right_count = 2
        self.test_rl_bal_tree.root.height = 2
        self.test_rl_bal_tree.root.right = AVLTreeNode(20, "Node 20")
        self.test_rl_bal_tree.root.right.left = AVLTreeNode(15, "Node 15")
        self.test_rl_bal_tree.root.right.left.height = 0
        """
        10
        ╟─20
        ║ ╟─
        ║ ╙─15
        ╙─
        """

        for tree in [self.test_l_bal_tree, self.test_rl_bal_tree]:
            # Re-balancing the tree
            try:
                tree.root = tree.rebalance(tree.root)
            except Exception as e:
                self.verificationErrors.append(str(e))

            # Checking if tree is balanced after re-balancing
            try:
                self.assertEqual(tree.get_balance(tree.root), 0, "".join(
                    ["Tree not balanced properly: expected 0, got ",
                     str(tree.get_balance(tree.root)), " for balance value"]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            # Checking if the position of the nodes are correct as well
            try:  # root = Node 15
                self.assertEqual(tree.root.item, "Node 15", "".join(
                    ["Node 15 is not in its correct position: expected Node 15, got ", str(tree.root.item)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            try:  # root left = Node 10
                self.assertEqual(tree.root.left.item, "Node 10", "".join(
                    ["Node 10 is not in its correct position: expected Node 10, got ", str(tree.root.left.item)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            try:  # root right = Node 20
                self.assertEqual(tree.root.right.item, "Node 20", "".join(
                    ["Node 20 is not in its correct position: expected Node 20, got ", str(tree.root.right.item)]))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    # Not included in submission
    # def test_delete(self):
    #     t = AVLTree()
    #     t[15] = 15
    #     t[10] = 10
    #     t[20] = 20
    #     t[5] = 5
    #     t[25] = 25
    #     t[18] = 18
    #     t[27] = 27
    #     t[0] = 7
    #     t[-3] = -3
    #     t[19] = 19
    #     t[22] = 22
    #     t[21] = 21
    #     t[24] = 24
    #     t.draw()
    #     assert t.root.right.right_count == 5
    #     del t[20]
    #     assert t.root.right.right_count == 4


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAVL)
    unittest.TextTestRunner(verbosity=0).run(suite)
