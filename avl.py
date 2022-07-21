""" AVL Tree implemented on top of the standard BST.
Updated by: Lee Sing Yuan, Loh Zhun Guan
"""

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic, Union

from bst import BinarySearchTree
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')
NoneType = type(None)
Numeric = (int, float)


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """
        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is 
            not None. Otherwise, return -1.

        :param current:     An AVLTreeNode.
        :return:            The height of the subtree rooted at current.
        :complexity:        O(1)
        :pre:               Input current must be an AVLTreeNode.
        :raises TypeError:  When current is not an AVLTreeNode.

        ----------------------------------------------------------------------------------------------------
        METHODS CALLED        | COMPLEXITY  |   REMARKS
        ----------------------|-------------|---------------------------------------------------------------
        isinstance()          | O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        AVLTree.get_height()  | O(1)        |
        ----------------------|-------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode) and not isinstance(current, NoneType):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode: current = ", str(current)]))

        return -1 if current is None else current.get_height()

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.

        :param current:     An AVLTreeNode.
        :return:            The balance factor of the subtree rooted at current.
        :complexity:        O(1)
        :pre:               Input current must be an AVLTreeNode.
        :raises TypeError:  When current is not an AVLTreeNode.

        ----------------------------------------------------------------------------------------------------
        METHODS CALLED        | COMPLEXITY  |   REMARKS
        ----------------------|-------------|---------------------------------------------------------------
        isinstance()          | O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        AVLTree.get_height()  | O(1)        |
        ----------------------|-------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode) and not isinstance(current, NoneType):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode or None: current = ", str(current)]))

        return 0 if current is None else self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: Union[AVLTreeNode, NoneType], key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.

        :param current:     The root of the current subtree.
        :param key:         The key value to determine the location of the new node.
        :param item:        The item that will be store in the new location.
        :return:            Returns the new root of the subtree.
        :complexity:        O(log n), where n is the number of nodes rooted by current.
        :pre:               Input current must be an AVLTreeNode or None
        :pre:               Input key must be Numeric.
        :raises TypeError:  When current is not an AVLTreeNode or key is not Numeric

        ----------------------------------------------------------------------------------------------------------------
        METHODS CALLED                    | COMPLEXITY  |   REMARKS
        ----------------------------------|-------------|---------------------------------------------------------------
        isinstance()                      | O(IsIns)    |   Unknown complexity for built-in function. Assume to be O(1).
        AVLTree.insert_aux()              | O(log n)    |   where n is the size of the tree
        AVLTree.get_height()              | O(1)        |
        AVLTree.rebalance()               | O(1)        |
        AVLTreeNode.__init__()            | O(1)        |
        AVLTreeNode.get_right_count()     | O(1)        |
        AVLTreeNode.set_height()          | O(1)        |
        AVLTreeNode.set_right_count()     | O(1)        |
        TreeNode.is_leaf()                | O(1)        |
        max()                             | O(1)        |   Here, max() only compares two items --> O(1)
        ----------------------------------|-------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode) and not isinstance(current, NoneType):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode or None: current = ", str(current)]))

        if current is None:  # base case: at the leaf
            new_node = AVLTreeNode(key, item)
            current = new_node
            self.length += 1

        elif key < current.key:  # If the key is smaller, it should go to the left.
            current.left = self.insert_aux(current.left, key, item)

        elif key > current.key:  # If the key is larger, it should go to the right.
            current.set_right_count(current.get_right_count() + 1)
            current.right = self.insert_aux(current.right, key, item)

        else:  # key == current.key
            raise ValueError('Inserting duplicate item')

        # Updating current's height and then re-balancing if need be
        current.set_height(max(self.get_height(current.left), self.get_height(current.right)) + 1)
        return self.rebalance(current)

    def delete_aux(self, current: Union[AVLTreeNode, NoneType], key: K) -> Union[AVLTreeNode, NoneType]:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.

        :param current:     The root of the current subtree.
        :param key:         The key value used to determine the location of the deleting node (if any)
        :return:            Returns the new root of the subtree.
        :complexity:        O(log n), where n = number of nodes in the subtree rooted by current.
        :pre:
        :raises TypeError:

        ----------------------------------------------------------------------------------------------------------------
        METHODS CALLED                    | COMPLEXITY  |   REMARKS
        ----------------------------------|-------------|---------------------------------------------------------------
        isinstance()                      | O(IsIns)    |   Unknown complexity for built-in function. Assume to be O(1).
        AVLTree.delete_aux()              | O(log n)    |   where n is the size of the tree
        BinarySearchTree.get_successor()  | O(log n)    |   where n = number of nodes of the subtree rooted by the input
        AVLTree.get_height()              | O(1)        |
        AVLTree.rebalance()               | O(1)        |
        AVLTreeNode.get_right_count()     | O(1)        |
        AVLTreeNode.set_height()          | O(1)        |
        AVLTreeNode.set_right_count()     | O(1)        |
        TreeNode.is_leaf()                | O(1)        |
        max()                             | O(1)        |   Here, max() only compares two items --> O(1)
        ----------------------------------|-------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode) and not isinstance(current, NoneType):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode or None: current = ", str(current)]))

        # Proceed with deletion
        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')

        elif key < current.key:
            current.left = self.delete_aux(current.left, key)

        elif key > current.key:
            current.set_right_count(current.get_right_count() - 1)
            current.right = self.delete_aux(current.right, key)

        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

            # Updating current's right count
            current.set_right_count(current.get_right_count() - 1)

        # Updating current's height and then re-balancing if need be
        current.set_height(max(self.get_height(current.left), self.get_height(current.right)) + 1)
        return self.rebalance(current)

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center


        :param current:     The root of the current subtree.
        :return:            The new root of the current subtree.
        :complexity:        O(1)
        :pre:               Input current must be an AVLTreeNode.
        :raises TypeError:  When input current is not an AVLTreeNode.

        ----------------------------------------------------------------------------------------------------------------
        METHODS CALLED                  |   COMPLEXITY  |   REMARKS
        --------------------------------|---------------|---------------------------------------------------------------
        isinstance()                    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        AVLTree.get_height()            |   O(1)        |
        AVLTreeNode.get_right_count()   |   O(1)        |
        AVLTreeNode.set_height()        |   O(1)        |
        AVLTreeNode.set_right_count()   |   O(1)        |
        TreeNode.is_leaf()              |   O(1)        |
        max()                           |   O(1)        |   Here, max() only compares two items.
        --------------------------------|---------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode: current = ", str(current)]))

        # The swapping child node
        child_node = current.right

        # The current's right child is then the child's left child
        current.right = child_node.left
        current.set_right_count(current.get_right_count() - child_node.get_right_count() - 1)

        # The child node's new left child will be current
        child_node.left = current

        # Giving them their new heights
        current.set_height(
            0 if current.is_leaf() else max(self.get_height(current.left), self.get_height(current.right)) + 1)
        child_node.set_height(
            0 if child_node.is_leaf() else max(self.get_height(child_node.left), self.get_height(child_node.right)) + 1)
        return child_node

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

        :param current:     The root of the current subtree.
        :return:            The new root of the current subtree.
        :complexity:        O(1)
        :pre:               Input current must be an AVLTreeNode.
        :raises TypeError:  When input current is not an AVLTreeNode.

        ----------------------------------------------------------------------------------------------------------------
        METHODS CALLED                  |   COMPLEXITY  |   REMARKS
        --------------------------------|---------------|---------------------------------------------------------------
        isinstance()                    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        AVLTree.get_height()            |   O(1)        |
        AVLTreeNode.get_right_count()   |   O(1)        |
        AVLTreeNode.set_height()        |   O(1)        |
        AVLTreeNode.set_right_count()   |   O(1)        |
        TreeNode.is_leaf()              |   O(1)        |
        max()                           |   O(1)        |   Here, max() only compares two items.
        --------------------------------|---------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode: current = ", str(current)]))

        # The swapping child node
        child_node = current.left

        # The current's left child is then the child node's right child
        current.left = child_node.right

        # The child node's new right child will be current
        child_node.right = current
        child_node.set_right_count(child_node.get_right_count() + current.get_right_count() + 1)

        # Giving them their new heights
        current.set_height(max(self.get_height(current.left), self.get_height(current.right)) + 1)
        child_node.set_height(max(self.get_height(child_node.left), self.get_height(child_node.right)) + 1)
        return child_node

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate

        :param current:     The current node.
        :return:            Returns the new root of the subtree.
        :complexity:        O(1)
        :pre:               Input current must be an AVLTreeNode.
        :raises TypeError:  When current is not an AVLTreeNode.

        -------------------------------------------------------------------------------------------------------
        METHODS CALLED          |   COMPLEXITY  |   REMARKS
        ------------------------|---------------|--------------------------------------------------------------
        isinstance()            |   O(IsIns)    |   Unknown complexity for built-in function. Assume to be O(1)
        AVLTree.get_balance()   |   O(1)        |
        AVLTree.get_height()    |   O(1)        |
        AVLTree.left_rotate()   |   O(1)        |
        AVLTree.right_rotate()  |   O(1)        |
        ------------------------|---------------|--------------------------------------------------------------
        -------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(current, AVLTreeNode):
            raise TypeError("".join(["Parameter current must be an AVLTreeNode: current = ", str(current)]))

        # Re-balancing
        # If it is right heavy
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        # If it is left heavy
        elif self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        # If it does not need balancing, it returns itself
        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """ Method to return the kth largest node in the entire AVL Tree.
        :param k:           An integer that determines which node to be returned.
                                (k=1 would return the largest.)
        :return:            Returns the kth largest element in the tree.
        :complexity:        O(log n) where n is the number of nodes in the AVL Tree.
        :pre:               Input k must be a positive integer.
        :raises TypeError:  When input k is not an integer.
        :raises ValueError: When input k is not positive.

        -------------------------------------------------------------------------------------------------------------
        METHODS CALLED              |   COMPLEXITY  |   REMARKS
        ----------------------------|---------------|----------------------------------------------------------------
        isinstance()                |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        AVLTree.kth_largest_aux()   |   O(1)        |   Get's called a maximum of log n times,
                                    |               |       where n is the number of nodes in the AVLTree.
        ----------------------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(k, bool) or not isinstance(k, int):
            raise TypeError("".join(["Parameter k must be an integer: k = ", str(k)]))
        elif k <= 0:
            raise ValueError("".join(["Parameter k must be a positive integer: k = ", str(k)]))

        # Calling auxiliary method
        return self.kth_largest_aux(self.root, k)

    def kth_largest_aux(self, current: AVLTreeNode, k: int) -> AVLTreeNode:
        """ Auxiliary function for kth_largest() method.
        :param current:     The current node in the AVL Tree being traversed.
        :param k:           Is the current value of k.
        :return:            The kth largest node in the AVL Tree.
        :pre:               Input k must be a positive integer.
        :raises TypeError:  When input k is not an integer.
        :raises ValueError: When input k is not positive.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(k, bool) or not isinstance(k, int):
            raise TypeError("".join(["Parameter k must be an integer: k = ", str(k)]))
        elif k <= 0:
            raise ValueError("".join(["Parameter k must be a positive integer: k = ", str(k)]))
        if not isinstance(current, AVLTreeNode):
            raise ValueError(
                "".join(["Parameter current must be an AVLTreeNode: current = ", str(current), ", k = ", str(k)]))

        # Traversing the AVL Tree
        if k == current.right_count + 1:
            return current
        elif k > current.right_count + 1:
            k -= current.right_count + 1
            return self.kth_largest_aux(current.left, k)
        elif k <= current.right_count:
            return self.kth_largest_aux(current.right, k)
        else:
            raise ValueError("kth largest node does not exist.")
