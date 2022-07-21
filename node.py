""" Implementation of a node in linked lists and binary search trees. """

from typing import TypeVar, Generic

I = TypeVar('I')
K = TypeVar('K')
T = TypeVar('T')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'


class ListNode(Generic[T]):
    """ Simple linked node. It contains an item and has a reference to next node. """

    def __init__(self, item: T = None) -> None:
        """ Node initialiser. """
        self.item = item
        self.next = None


class TreeNode(Generic[K, I]):
    """ Node class represent BST nodes.
        Attributes:
            key (int):          The key value used to determine the position of the node in the Tree.
            item (T):           The item stored in the node.
            left (TreeNode):    The left child node of the TreeNode instance.
            right (TreeNode):   The right child node of the TreeNode instance.
    """

    def __init__(self, key: K, item: I = None) -> None:
        """
            Initialises the node with a key and optional item
            and sets the left and right pointers to None
            :complexity: O(1)
        """
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        """
            Returns the string representation of a node
            :complexity: O(N) where N is the size of the item
        """
        key = str(self.key) if type(self.key) != str else "'{0}'".format(self.key)
        item = str(self.item) if type(self.item) != str else "'{0}'".format(self.item)
        return '({0}, {1})'.format(key, item)

    def is_leaf(self) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return self.left is None and self.right is None


class AVLTreeNode(TreeNode, Generic[K, I]):
    """ Node class for AVL trees.
        Objects of this class have an additional variable - height.

        Attributes:
            key (int):          The key value used to determine the position of the node in the Tree.
            item (T):           The item stored in the node.
            left (TreeNode):    The left child node of the AVLTreeNode instance.
            right (TreeNode):   The right child node of the AVLTreeNode instance.
            height (int):       The height of the tree rooted at the AVLTreeNode instance.
            right_count (int):  The number of nodes attached to the right of the AVLTreeNode instance.

        Class Variables:
            None
    """

    def __init__(self, key: K, item: I = None) -> None:
        """
            Initialises the node with a key and optional item
            and sets the left and right pointers to None

        :param key:  The key for this node.
        :param item: The item stored in this node.
        :returns:    None
        :complexity: O(1)

        ---------------------------------------------------------------
        METHODS CALLED                  |   COMPLEXITY  |   REMARKS
        --------------------------------|---------------|--------------
        TreeNode.__init__()             |   O(1)        |
        AVLTreeNode.set_height()        |   O(1)        |
        AVLTreeNode.set_right_count()   |   O(1)        |
        --------------------------------|---------------|--------------
        ---------------------------------------------------------------
        """

        super(AVLTreeNode, self).__init__(key, item)
        self.set_height(1)

        # Additional AVL Tree Node attributes: right_count
        # This attribute keeps track of how many nodes are on the right side of the AVL Tree Node
        # right_count is used to find the k-th largest node in the entire AVL Tree
        self.set_right_count(0)

    # Mutator Methods
    def set_height(self, height: int) -> None:
        """ Mutator method for height attribute of an AVLTreeNode.
        :param height:      Node's height attribute value.
        :return:            None
        :complexity:        O(1)
        :pre:               Input height must be a non-negative integer.
        :raises TypeError:  When input height is not an integer.
        :raises ValueError: When input height is negative.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in functions. Assumed to be O(1)
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        if isinstance(height, bool) or not isinstance(height, int):
            raise TypeError("".join(["Parameter height must be an integer: height = ", str(height)]))
        elif height < 0:
            raise ValueError("".join(["Parameter height must be non-negative: height = ", str(height)]))

        # Initialising AVLTreeNode's height attribute
        self.height = height
        
    def set_right_count(self, right_count: int) -> None:
        """ Mutator method for right_count attribute of an AVLTreeNode.
        :param right_count: Number of nodes on the right side of an AVLTreeNode
        :return:            None
        :complexity:        O(1)
        :pre:               Input right_count must be a non-negative integer.
        :raises TypeError:  When input right_count is not an integer.
        :raises ValueError: When input right_count is negative.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in functions. Assumed to be O(1)
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(right_count, bool) or not isinstance(right_count, int):
            raise TypeError("".join(["Parameter right_count must be an integer: right_count = ", str(right_count)]))
        elif right_count < 0:
            raise ValueError("".join(["Parameter right_count must be non-negative: right_count = ", str(right_count)]))

        # Initialising AVLTreeNode's right_count attribute
        self.right_count = right_count

    # Accessor Methods
    def get_height(self) -> int:
        """ Accessor method for height attribute of an AVLTreeNode.
        :return:     The height of the Node
        :complexity: O(1)
        """
        return self.height

    def get_right_count(self) -> int:
        """ Accessor method for right_count attribute of an AVLTreeNode.
        :return:     The right_count of the Node
        :complexity: O(1)
        """
        return self.right_count