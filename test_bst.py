import unittest

from bst import BinarySearchTree
from tester_base import TesterBase


class TestBST(TesterBase):

    def setUp(self) -> None:
        self.b = BinarySearchTree()
        self.b[15] = "A"
        self.b[10] = "B"
        self.b[20] = "C"
        self.b[17] = "D"
        self.b[5] = "E"
        self.b[3] = "F"
        self.b[4] = "G"
        self.b[22] = "H"
        self.b.draw()
        """
        15
        ╟─10
        ║ ╟─5
        ║ ║ ╟─3
        ║ ║ ║ ╟─
        ║ ║ ║ ╙─4
        ║ ║ ╙─
        ║ ╙─
        ╙─20
          ╟─17
          ╙─22
          
                               ----15----
                               |         |
                             --10--    --20--
                             |     |   |     |
                           --5--       17    22
                           |    |    
                         --3--  
                         |    |
                              4
        """

        return super().setUp()

    def test_minimal(self):
        self.assertEqual(self.b.get_minimal(self.b.get_tree_node_by_key(15)).item, "F")
        self.assertEqual(self.b.get_minimal(self.b.get_tree_node_by_key(20)).item, "D")
        print(self.b.get_minimal(self.b.get_tree_node_by_key(3)))
        self.assertEqual(self.b.get_minimal(self.b.get_tree_node_by_key(3)).item, "F")

    def test_successor(self):
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(15)).item, "D")
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(5)), None)
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(10)), None)

        # testing boundaries
        # if i test 22 i should get NONE
        # print(self.b.get_successor(self.b.get_tree_node_by_key(22)))
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(22)), None)

        # if i test 3 i should get 4
        # print(self.b.get_successor(self.b.get_tree_node_by_key(3)))
        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(3)).item, "G")

        self.assertEqual(self.b.get_successor(self.b.get_tree_node_by_key(5)), None)

    def test_successor_2(self):
        tree = BinarySearchTree()
        """
                                  --10--
                                 |      |
                                5    --20--
                                     |     |
                                    19     21
        """

        tree[10] = "A"
        tree[5] = "B"
        tree[20] = "C"
        tree[19] = "D"
        tree[21] = "E"

        tree.draw()
        self.assertEqual(tree.get_successor(tree.get_tree_node_by_key(10)).item, "D")

    def test_get_successor_invalid_input(self):
        tree = BinarySearchTree()
        tree[10] = "A"

        invalid_inputs = [10, "A", True]
        for value in invalid_inputs:
            try:
                self.assertRaises(TypeError, tree.get_successor, value)
            except AssertionError:
                self.verificationErrors.append("get_successor() method does not handle invalid inputs properly.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBST)
    unittest.TextTestRunner(verbosity=0).run(suite)

