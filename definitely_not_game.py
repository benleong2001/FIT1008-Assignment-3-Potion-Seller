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

from math import log10, floor

from avl import AVLTree
from hash_table import LinearProbePotionTable
from potion import Potion
from random_gen import RandomGen


class Game:
    """ This is the Game class! It simulates the relationships between PotionCorp, Vendors, Adventurers and the user.
    Attributes:
        rand (RandomGen):                    A random number generator (used in choose_potions_for vendors)
        inventory (AVLTree):                 An AVLTree to store (potion_name, quantity) tuples
                                                with the potion's buy_price as the key.
        read_table (LinearProbePotionTable): A hash table to contain the data of the Potions to be sold

    Class Variables:
        None
    """
    MAX_VALUE: int = 100000

    def __init__(self, seed=0) -> None:
        """
        :param seed:
        """
        self.inventory: AVLTree[float, tuple[str, float]] = AVLTree()
        self.rand: RandomGen = RandomGen(seed=seed)
        self.min_buy_price: float = Game.MAX_VALUE
        self.max_buy_price: float = 0

    def set_read_table(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        """ Mutator for read_table attribute.
        :param max_potions: An integer used as input to create a hash table.
        :param good_hash: A boolean value used as input to create a hash table.
        :param tablesize_override: An integer (-1 or greater) used as input to create a hash table.
            (See details of parameters in LinearProbePotionTable.__init__() in hash_table.py)
        :return: None
        :complexity: O(1)
        :pre: Input max_potions must be an integer.
        :pre: Input good_hash must be a boolean.
        :pre: Input tablesize_override must be an integer and tablesize_override >= -1.
        :raises TypeError: When max_potions or tablesize_override is not an integer or good_hash is not a boolean.
        :raises ValueError: When tablesize_override < -1.
        """
        self.read_table: LinearProbePotionTable = LinearProbePotionTable(max_potions, good_hash, tablesize_override)

    def set_total_potion_data(self, potion_data: list[tuple[str, str, float]]) -> None:
        """
        :param potion_data: A list containing tuples of 3 values; potion_name, type and buy_price used to create a
                            Potion
        :return: None
        """
        # This method inserts all of the data of the potions into the table using Potion.create_empty()
        max_potions = len(potion_data)
        self.set_read_table(max_potions)
        for potion_name, potion_type, potion_price in potion_data:
            potion = Potion.create_empty(potion_name, potion_type, potion_price)
            self.read_table[potion_name] = potion

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        # I think this just updates the hash table with the relevant quantity amounts.
        # We still can include a AVL tree but idk if need to lol
        """
        WHAT WE KNOW: set_total_potion_data is all available potions in the game for all days
        IDEA: so looping through the elements in the potion_name_amount_pairs is O(C)

        ASSUMPTION: hash table uses "name" as key
                    hash table stores potion object
                    AVL uses "buy_price" as key
        """
        potion: Potion
        buy_price: float

        # goes through input list
        for name, quantity in potion_name_amount_pairs:
            potion = self.read_table[name]

            # since it is hash tables, get is of O(1)
            buy_price = potion.get_buy_price()
            self.min_buy_price = min(self.min_buy_price, buy_price)
            self.max_buy_price = max(self.max_buy_price, buy_price)

            # accessing and changing the quantity in the hash table
            potion.set_quantity(quantity)

            # this is to add to the AVL
            # time complexity O(C) * O(logN)
            # avl uses the price as keys
            # print(buy_price)
            self.inventory[buy_price] = (name, quantity)

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """
        :param num_vendors:
        :return: A list containing the potion being sold by the vendors.
        :pre: num_vendors is an integer.
        :pre: 0 < num_vendors <= len(self.read_table)
        :raises TypeError:
        :raises ValueError:
        """
        temp_tree = AVLTree()
        returning_list = [None] * num_vendors
        for i in range(num_vendors):
            k = self.rand.randint(len(self.inventory))
            node = self.inventory.kth_largest(k)
            key = node.key
            potion_tup = node.item
            temp_tree[key] = potion_tup
            del self.inventory[key]
            returning_list[i] = potion_tup
        self.inventory = temp_tree
        return returning_list

        # Use rng to get random indices to assign vendors to Potions for them to sell.
        # result = []
        # # O(C) for the for loop, where C is num_vendors
        # for i in range(num_vendors):
        #     k = self.rand.randint(len(self.inventory))
        #     potion = self.inventory.kth_largest(k)  # O(log(N)), where N is the numbers of potion in self.inventory
        #     del self.inventory[potion.key]
        #     result.append(potion.item)
        # return result

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        """
        :param potion_valuations:   A list of tuples containing the potions being sold
                                        and how much adventurers are willing to pay for them
        :param starting_money:      A list of starting amounts for each day
        :return:                    A list of ending amount for each day corresponding to starting_money
        :target complexity:         O(N log N + MN) where N = len(potion_valuations)
                                                    where M = len(starting_money)

        """
        profit_tree: AVLTree = AVLTree()
        returning_list: list[float] = []
        # O(N) since it goes through potion_val
        for name, sell_price in potion_valuations:
            potion = self.read_table[name]
            buy_price, quantity = potion.get_buy_price(), potion.get_quantity()
            profit = sell_price - buy_price

            # O(log N) to add items into the tree
            if profit > 0:
                profit_tree[profit / buy_price + (
                        (self.max_buy_price - buy_price) / pow(10, floor(log10(self.max_buy_price)) + 1))] = (
                    buy_price, sell_price, quantity)
        # O(N log N) here

        # O(M) since it goes through starting_money
        for i, start in enumerate(starting_money):
            ending_amount = 0
            profit_index = 0

            while profit_index < len(profit_tree) and start >= self.min_buy_price:
                buy, sell, quantity = profit_tree.kth_largest(profit_index + 1).item
                profit_index += 1
                # if start < buy:
                #     continue
                print("start buy", start, buy)
                # start // buy is how many litres can be bought
                loss = min(start / buy, quantity)

                # The profit we make is how many litres * selling price
                ending_amount += loss * sell

                # Our amount is reduced by loss amount
                start -= loss * buy
            returning_list.append(ending_amount)
        # O(MN) for here
        # Total is O(N log N + MN)

        return returning_list


s = "aback abase abate abbey abyss acute adobe agate agree ahead allow aloft alone altar ample argue aroma aside " \
    "askew audit awake badge badly banal basic baton batty belch belly bench biome black bleed bloke blurt blush " \
    "booby boost boozy brake break briar bribe brine bring canny cargo cater caulk champ chant cheat cheek chest " \
    "chill choke chunk cigar civic click clock cloth cluck coast colon comet comma conic corny could crank crass " \
    "crate craze crazy crimp croak crust cynic death delta depot digit dodge dowry dozen drain drink duchy dutch " \
    "dwarf elder enema epoch epoxy erode error essay evade exult farce favor feign ferry fewer finer first fixer " \
    "fjord flair flesh flick fling floss flume focal focus foray forge forgo forth found foyer frame fresh front " \
    "gamma gaudy gecko golem goner gorge gouge grade great greet grime gripe groin group growl guild hairy hatch " \
    "heath heist helix heron hoard homer humor humph hyper inert islet ivory jaunt karma kebab knoll labor lapel " \
    "lapse larva light linen loopy lowly lowly lusty lying major marry masse maxim metal midst mimic mince model " \
    "moist month motor moult mount mourn movie nasty natal naval nymph offal olive other ought outdo oxide panel " \
    "panic paper parry pause peach perch perky picky pilot pithy plant pleat pluck point pound prick pride print " \
    "prove proxy pulpy purge query quiet radio react rebus rebut renew repay retch rhino robin robot rogue rouge " \
    "round royal rupee salad saute scare seedy serve shake shall shame shard shine shire shown shrub siege sissy " \
    "skill slosh slump slung smart smelt snout solar solve sonic sower spend spicy spike spill spray squad staff " \
    "stair stand start steed stink stool store story stout stove sugar surer sweet swill swirl tacit tangy tapir " \
    "tease their thorn those thumb tiger tilde tipsy today totem trace train trash trawl triad troll trope trove " \
    "truss tweed ulcer ultra unfed unify unmet usher using viral vital vivid vodka watch weary whack whelp wince " \
    "wooer world wrote wrung yearn zesty"
