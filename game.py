""" Game
Group Number: T05G04
Members:      Lee Sing Yuan
              Benjamin Leong Tjen Ho
              Lim Jing Kai
              Loh Zhun Guan

Description:
    This file contains the Game class which contains the logic of the game,
        as well as a method to solve the game with the most optimal answer.
"""

from __future__ import annotations

# for inventory for the day
from avl import AVLTree
from hash_table import LinearProbePotionTable
from node import AVLTreeNode
from potion import Potion
from random_gen import RandomGen

Numeric = (int, float)


class Game:
    """ This is the Game class! It simulates the relationships between PotionCorp, Vendors, Adventurers and the user.
    Attributes:
        rand (RandomGen):                       A random number generator (used in choose_potions_for vendors)
        inventory (AVLTree):                    An AVLTree to store (potion_name, quantity) tuples
                                                    with the potion's buy_price as the key.
                                                Used for the utilization of kth largest.
        read_table (LinearProbePotionTable):    A hash table to contain the data of the Potions to be sold.
                                                Used for the utilization of quick __setitem__() and __getitem__() speed.

    Class Variables:
        None
    """

    def __init__(self, seed: int = 0) -> None:
        """ Basic Game object initialiser.
        :param seed: The seed value used to create a random number generator.
        :return:     None
        :complexity: O(1)
        """
        self.inventory: AVLTree[float, tuple[str, float]] = AVLTree()
        self.rand: RandomGen = RandomGen(seed=seed)

    def set_read_table(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        """ Mutator for read_table attribute. Creates Hash Table

        :param max_potions:         An integer used as input to create a hash table.
        :param good_hash:           A boolean value used as input to create a hash table.
        :param tablesize_override:  An integer (-1 or greater) used as input to create a hash table.
            (See details of parameters in LinearProbePotionTable.__init__() in hash_table.py)
        :return:                    None
        :complexity:                O(1). Because it is instantiation of class LinearProbePotionTable
        :pre:                       Input max_potions must be an integer.
        :pre:                       Input good_hash must be a boolean.
        :pre:                       Input tablesize_override must be an integer and tablesize_override >= -1.
        :raises TypeError:          When max_potions or tablesize_override is not an integer or good_hash is not a boolean.
        :raises ValueError:         When tablesize_override < -1.
        """
        # Checking pre condition(s)
        if not isinstance(good_hash, bool):
            raise TypeError("".join(["Parameter good_hash must a boolean: good_hash = ", str(good_hash)]))
        elif isinstance(max_potions, bool) or not isinstance(max_potions, int):
            raise TypeError("".join(["Parameter max_potions must an integer: max_potions = ", str(max_potions)]))
        elif isinstance(tablesize_override, bool) or not isinstance(tablesize_override, int):
            raise TypeError("".join(
                ["Parameter tablesize_override must an integer: tablesize_override = ", str(tablesize_override)]))
        elif tablesize_override < -1:
            raise ValueError("".join(
                ["Parameter tablesize_override must be -1 or greater: tablesize_override = ", str(tablesize_override)]))

        self.read_table: LinearProbePotionTable = LinearProbePotionTable(max_potions, good_hash, tablesize_override)

    def set_total_potion_data(self, potion_data: list[str, str, float]) -> None:
        """ Sets the inventory of the vendors.
            Uses Hash Table ADT due to ability to set and get data quickly using hash functions.

        :param potion_data: A list containing potion data to create empty potions to be stored in a hash table.
                                The list will contain tuples in this format (str, str, float)
        :complexity:        O(N) where n = len(potion_data).
                                Because we call the mutator method N times
                                which means it is O(N) * O(1) = O(N)

        ----------------------------------------------------------------------------------------------------------------
        METHODS CALLED                  |   COMPLEXITY  |   REMARKS
        --------------------------------|---------------|---------------------------------------------------------------
        isinstance()                    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        Game.set_read_table()           |   O(1)        |
        LinearProbePotionTable.insert() |   O(1)        |
        Potion.create_empty()           |   O(1)        |
        --------------------------------|---------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------
        """
        __author__ = 'Loh Zhun Guan'

        buy_price: float
        name: str
        potion: Potion
        potion_type: str

        # Checking pre condition(s)
        if not isinstance(potion_data, list):
            raise TypeError("".join(["Parameter potion_data must be a list: potion_data = ", str(potion_data)]))

        # This method inserts all of the data of the potions into the table using Potion.create_empty()
        self.set_read_table(len(potion_data))
        for potion_type, name, buy_price in potion_data:
            # Checking pre condition of values in potion_data
            if not isinstance(potion_type, str):
                raise TypeError("".join(
                    ["Tuple in parameter potion_data must contain string at index 0: potion_type = ",
                     str(potion_type)]))
            elif not isinstance(name, str):
                raise TypeError(
                    "".join(["Tuple in parameter potion_data must contain string at index 1: name = ", str(name)]))
            elif isinstance(buy_price, bool) or not isinstance(buy_price, Numeric):
                raise TypeError("".join(
                    ["Tuple in parameter potion_data must contain string at index 2: buy_price = ", str(buy_price)]))

            # Creating empty potion to insert into data hash table
            potion = Potion.create_empty(potion_type, name, buy_price)
            self.read_table.insert(name, potion)

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """ Updates the quantity of the potion object in the hash table and creates
            an AVL for the utilization of the kth largest.

        :param potion_name_amount_pairs: A list containing potion names and their quantities as tuples.
        :return:                        None
        :complexity:                    O(C x log(N))
                                            where C = len(potion_name_amount_pairs)
                                                  N = number of potions provided in set_total_potions_data()
        :pre:                           Input potion_name_amount_pairs needs to contain tuples which needs to be in the
                                            order of (str, float).
        :raises TypeError:              When the potion_name_amount_pairs is not a list or the tuples in the list is not
                                            in the order of (str, float)

        --------------------------------------------------------------------------------------------------
        ----------------------------------------|---------------|-----------------------------------------
        METHODS CALLED                          |   COMPLEXITY  |   REMARKS
        ----------------------------------------|---------------|-----------------------------------------
        isinstance()                            |   O(IsIns)    |   Unknown complexity of built-in method.
                                                |               |       Assumed to be O(1)
        LinearProbePotionTable.__getitem__()    |   O(1)        |
        Potion.get_buy_price()                  |   O(1)        |
        Potion.set_quantity()                   |   O(1)        |
        max()                                   |   O(1)        |   Here, max() only compares two items.
        min()                                   |   O(1)        |   Here, min() only compares two items.
        ----------------------------------------|---------------|-----------------------------------------
        --------------------------------------------------------------------------------------------------
        """
        __author__ = 'Lee Sing Yuan'

        # Type Hinting
        buy_price: float
        potion: Potion
        name: str
        quantity: float

        # Checking pre condition(s)
        if not isinstance(potion_name_amount_pairs, list):
            raise TypeError("".join(["Parameter potion_name_amount_pairs must be a list: potion_name_amount_pairs = ",
                                     str(potion_name_amount_pairs)]))

        # Go through the potion_name_amount_pairs --> O(C)
        for name, quantity in potion_name_amount_pairs:
            # Checking pre conditions for values in potion_name_amount_pairs
            if not isinstance(name, str):
                raise TypeError("".join(
                    ["Tuple in parameter potion_name_amount_pairs must contain string at index 0: name = ",
                     str(name)]))
            elif isinstance(quantity, bool) or not isinstance(quantity, Numeric):
                raise TypeError("".join(
                    ["Tuple in parameter potion_name_amount_pairs must contain float at index 1: quantity = ",
                     str(quantity)]))

            # Retrieve the potion stored in potion data hash table via the potion name (its key)
            potion = self.read_table[name]

            # Getting the potion's buy_price to use as a key
            buy_price = potion.get_buy_price()

            # Updating the quantity of the potion
            potion.set_quantity(quantity)

            # Add the (name, quantity) to the AVL with the buy_price as the key
            # This is so that in choose_potions_for_vendors(), the vendors will choose the
            #   kth currently most expensive potion based on the random number generated for them
            self.inventory[buy_price] = (name, quantity)

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """ Return a list specifying what the vendors will sell. Creates
            an AVL for the utilization of the kth largest.

        :param num_vendors: How many vendors will sell potions
        :return:            A list containing list of potion that vendors will sell
        :complexity:        Best O(C) when kth largest is the root node, where C is num_vendors
                            Worst O(C x log(N)) when kth largest is the leaf node,
                            where N is the number of potion in inventory.
                            Because we are iterating O(C) times and performing AVL opertation Kth largest
                            which is O(log(N)) where N is the number of nodes.
        :pre:               Input num_vendors must be an integer.
        :raises TypeError:  When input num_vendors is not an integer
        :raises ValueError: When input num_vendors is not between 0 and number of potions provided
                                in set_total_potions_data() (inclusive)

        ----------------------------------------------------------------------------------------------------------------
        --------------------------------|---------------|---------------------------------------------------------------
        METHODS CALLED                  |   COMPLEXITY  |   REMARKS
        --------------------------------|---------------|---------------------------------------------------------------
        isinstance()                    |   O(IsIns)    |   Unknown complexity of built-in function. Assumed to be O(1).
        RandomGen.randint()             |   O(1)        |
        AVLTree.kth_largest()           |   O(log N)    |   where N = len(self.inventory)
        BinarySearchTree.__delitem__()  |   O(log N)    |   where N = len(self.inventory)
        BinarySearchTree.__setitem__()  |   O(log N)    |   where N = len(self.inventory)
        List.append()                   |   O(1)        |
        --------------------------------|---------------|---------------------------------------------------------------
        ----------------------------------------------------------------------------------------------------------------

        Note:
            C = num_vendors
            N = number of potions provided in set_total_potion_data()
        """
        __author__ = 'Lim Jing Kai'

        # Type hinting
        i: int
        k: int
        node: AVLTreeNode
        result: list
        temp_tree: AVLTree

        # Checking pre condition(s)
        if isinstance(num_vendors, bool) or not isinstance(num_vendors, int):
            raise TypeError("".join(["Parameter num_vendors must be an integer: num_vendors = ", str(num_vendors)]))
        elif num_vendors < 0 or num_vendors > len(self.read_table):
            raise ValueError("".join([
                "Parameter num_vendors must be between 0 and the number of potions provided in "
                "set_total_potions_data(): num_vendors = ", str(num_vendors)]))

        temp_tree = AVLTree()
        result = []

        # O(C) for the for loop, where C is num_vendors
        for i in range(num_vendors):
            # Getting a random integer between 1 in len(self.inventory) (inclusive)
            k = self.rand.randint(len(self.inventory))

            # O(log(N)), where N = len(self.inventory)
            node = self.inventory.kth_largest(k)

            # Storing the potions into a temporary tree
            temp_tree[node.key] = node.item
            result.append(node.item)

            # Removing the potion chosen from inventory
            del self.inventory[node.key]

        # Returning the stored potions into the inventory
        # This loop will also be O(C) since the range uses num_vendors
        for j in range(1, num_vendors + 1):
            node = temp_tree.kth_largest(j)
            self.inventory[node.key] = node.item

        return result

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[float]) -> list[float]:
        """ Method to find the most optimal ending amount for each day
            corresponding to the amounts in the starting money input. Creates
            an AVL for the utilization of the kth largest.
        :param potion_valuations:   A list of tuples containing the potions being sold
                                        and how much adventurers are willing to pay for them
        :param starting_money:      A list of starting amounts for each day
        :return:                    A list of ending amount for each day corresponding to starting_money
        :complexity:                O(N log N + MN), M and N are defined in the note below.
        :pre:                       Input potion_valuations must be a list.
        :pre:                       Tuples in input potion_valuations must be in the format (str, float).
        :pre:                       Input starting_money must be a list.
        :pre:                       Input starting_money must only contain floats.
        :raises TypeError:          When any of the pre conditions fail.


        -----------------------------------------------------------------------------------------------------
        METHODS CALLED                          |   COMPLEXITY  |   REMARKS
        ----------------------------------------|---------------|--------------------------------------------
        AVLTree.kth_largest()                   |   O(log N)    |   Where N = number of nodes in profit_tree.
        BinarySearchTree.__setitem__()          |   O(log N)    |   Where N = number of nodes in profit_tree.
        LinearProbePotionTable.__getitem__()    |   O(1)        |
        List.append()                           |   O(1)        |
        Potion.get_buy_price()                  |   O(1)        |
        Potion.get_quantity()                   |   O(1)        |
        min()                                   |   O(1)        |   Here, min() only compares 2 items.
        ----------------------------------------|---------------|--------------------------------------------
        -----------------------------------------------------------------------------------------------------

        Explanation:
            - In order to get the most optimised ending amount for each day, we need to find out which potion would give
                us not only the greatest profit buy also at the cheapest cost.
            - Let's call this expression profit / buy_price as 'yield'.
            - We calculate the yield of all the potions in potion_valuations.
            - We then create an AVLTree to contain the potion's buy_price, selling price and quantity, using the yield
                as their key.
                - Uh-oh, yields are not unique! But their buy_prices are! So, we use a tuple as the key where the tuple
                    is (yield, -buy_price). The buy_price is negative as we want to prioritise the cheapest potion with
                    the greatest yield.
            - Then, we loop through starting_money and start spending as much as we can, going from the potion with the
                kth largest key to that of the smallest key. This is why we created an AVLTree, to use kth largest.
            - For each iteration, we compile the money earned and add the final amount per day into a returning list.

        Note:
            N = len(potion_valuations)
            M = len(starting_money)
        """
        __author__ = 'Benjamin Leong Tjen Ho'

        # Type hinting
        buy_price: float
        i: int
        num_of_litres: float
        profit: float
        profit_index: int
        profit_per_day: float
        profit_tree: AVLTree
        quantity: float
        returning_list: list[float]
        start: float

        profit_tree = AVLTree()
        returning_list = []

        # Checking pre condition(s)
        if not isinstance(potion_valuations, list):
            raise TypeError(
                "".join(["Parameter potion_valuations must be a list: potion_valuations = ", str(potion_valuations)]))
        elif not isinstance(starting_money, list):
            raise TypeError(
                "".join(["Parameter starting_money must be a list: starting_money = ", str(starting_money)]))
        elif any([isinstance(money, bool) or not isinstance(money, Numeric) for money in starting_money]):
            raise TypeError(
                ["Parameter starting money must only contain floats: starting_money = ", str(starting_money)])

        # Goes through potion_valuations --> O(N)
        for name, sell_price in potion_valuations:
            # Checking pre conditions for values in potion_valuations
            if not isinstance(name, str):
                raise TypeError("".join(
                    ["Tuples in parameter potion_valuations must contain strings at index 0: name = ", str(name)]))
            elif isinstance(sell_price, bool) or not isinstance(sell_price, Numeric):
                raise TypeError("".join(
                    ["Tuples in parameter potion_valuations must contain float at index 1: sell_price = ",
                     str(sell_price)]))

            potion = self.read_table[name]
            buy_price, quantity = potion.get_buy_price(), potion.get_quantity()
            profit = sell_price - buy_price

            # O(log N) to add items into the tree
            if profit > 0:
                profit_tree[(profit / buy_price, -buy_price)] = (buy_price, sell_price, quantity)
        # O(N log N) here^

        # O(M) since it goes through starting_money
        for i, start in enumerate(starting_money):
            profit_per_day, profit_index = 0, 0

            # This loop will through the profit_tree
            # But it may stop once there is no more money for the day
            while profit_index < len(profit_tree) and start > 0:
                buy, sell, quantity = profit_tree.kth_largest(profit_index + 1).item
                profit_index += 1

                # start / buy is how many litres that can be bought
                num_of_litres = min(start / buy, quantity)

                # The profit we make is how many litres * selling price
                profit_per_day += num_of_litres * sell

                # Our amount is reduced by loss amount
                start -= num_of_litres * buy

            # The final amount is then added to start
            returning_list.append(profit_per_day + start)
        # O(MN) here^

        # Total is O(N log N + MN)
        return returning_list
