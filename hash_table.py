""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.

Updated by: Lim Jing Kai
"""
__author__ = 'Brendon Taylor, modified by Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from typing import TypeVar, Generic

from potion import Potion
from primes import largest_prime, MAX_SIZE
from referential_array import ArrayR

T = TypeVar('T')


class LinearProbePotionTable(Generic[T]):
    """
    Linear Probe Potion Table

    This potion table does not support deletion.

    attributes:
        conflict_count (int):
        count (int): number of elements in the hash table
        table (ArrayR): used to represent our internal array
        table_size: current size of the hash table
    """

    def __init__(self, max_potions: int, good_hash: bool = True, tablesize_override: int = -1) -> None:
        # Statistic setting
        self.conflict_count = 0
        self.probe_max = 0
        self.probe_total = 0

        self.set_good_hash(good_hash)
        self.set_table_size(max_potions, tablesize_override)
        self.initalise_with_tablesize(self.get_table_size())

    # Mutator Methods
    def set_good_hash(self, good_hash: bool) -> None:
        """ Mutator for good_hash attribute of a LinearProbePotionTable.
        :param good_hash:   A boolean value stating if good_hash() or bad_hash() should be used.
        :return:            None
        :complexity:        O(1)
        :pre:               Input good_hash must be a boolean.
        :raises TypeError:  When input good_hash is not a boolean.
        """
        # Checking pre condition(s)
        if not isinstance(good_hash, bool):
            raise TypeError("".join(["Parameter good_hash must be a boolean: good_hash = ", str(good_hash)]))

        # Initialising LinearProbePotionTable's is_good_hash attribute
        self.good_hash = good_hash

    def set_table_size(self, max_potions: int, tablesize_override: int) -> None:
        """ Mutator for tablesize attribute of a LinearProbePotionTable.
        :param max_potions:         The maximum number of potions that the hash table can hold.
        :param tablesize_override:  The overriding tablesize value or -1.
        :return:                    None
        :complexity:                O(1)
        :pre:                       Input max_potions must be a non-negative integer.
        :pre:                       Input tablesize_override must be an integer greater or equal to max_potions or -1
        :raises TypeError:          When input tablesize_override or max_potions are not integers.
        :raises ValueError:         When input tablesize is not -1 and less than max_potions or max_potions < 0.
        """
        # Checking pre condition(s)
        if isinstance(max_potions, bool) or not isinstance(max_potions, int):
            raise TypeError("".join(["Parameter max_potions must be an integer: max_potions = ", str(max_potions)]))
        elif max_potions < 0:
            raise ValueError(
                "".join(["Parameter max_potions must be a non-negative integer: max_potions = ", str(max_potions)]))
        elif isinstance(tablesize_override, bool) or not isinstance(tablesize_override, int):
            raise TypeError("".join(
                ["Parameter tablesize_override must be an integer: tablesize_override = ", str(tablesize_override)]))
        elif tablesize_override != -1 and tablesize_override < max_potions:
            raise ValueError("".join(
                ["Parameter tablesize_override must be greater or equal to max_potions or -1: tablesize_override = ",
                 str(tablesize_override)]))

        # Initialising LinearProbePotionTable's tablesize attribute
        self.table_size = largest_prime(min(max_potions * 2, MAX_SIZE)) if tablesize_override == -1 \
            else tablesize_override

    def get_good_hash(self) -> bool:
        """ Accessor for good_hash attribute of a LinearProbePotionTable.
        :return:        The good_hash attribute of a LinearProbePotionTable.
        :complexity:    O(1)
        """
        return self.good_hash

    def get_table_size(self) -> int:
        """ Accessor for tablesize attribute of a LinearProbePotionTable.
        :return:        The tablesize attribute of a LinearProbePotionTable.
        :complexity:    O(1)
        """
        return self.table_size

    def hash(self, potion_name: str) -> int:
        """ Method to produce the hash value of an item.
        :param potion_name: The name of the Potion used as an input for the hash function.
        :return:            Returns the hash value of the Potion.
        :complexity:        O(1)
        """
        hash_function = Potion.good_hash if self.good_hash else Potion.bad_hash
        return hash_function(potion_name, self.get_table_size())

    def statistics(self) -> tuple:
        """ "Accessor" of statistics of the table.
        :return:     Returns a tuple of 3 values:
                        ○ the total number of conflicts (conflict_count)
                        ○ the total distance probed throughout the execution of the code (probe_total)
                        ○ the length of the longest probe chain throughout the execution of the code (probe_max)
        :complexity: O(1)
        """
        return self.conflict_count, self.probe_total, self.probe_max

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    # Private Method
    def __linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        :complexity best: O(K) first position is empty
                          where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash
        probe_local = 0
        probe_start = False
        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing

            if self.table[position] is None:  # found empty slot
                if is_insert:
                    self.probe_max = max(probe_local, self.probe_max)
                    self.conflict_count += probe_start
                    return position
                else:
                    raise KeyError(key)  # so the key is not in

            elif self.table[position][0] == key:  # found key
                return position

            else:  # there is something but not the key, try next
                position = (position + 1) % len(self.table)
                self.probe_total += 1
                probe_local += 1
                probe_start = True

        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :raises KeyError: when the item doesn't exist
        """
        position = self.__linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        if len(self) == len(self.table) and key not in self:
            raise ValueError("Cannot insert into a full table.")
        position = self.__linear_probe(key, True)

        if self.table[position] is None:
            self.count += 1
        self.table[position] = (key, data)

    def initalise_with_tablesize(self, tablesize: int) -> None:
        """
        Initialise a new array, with table size given by tablesize.
        Complexity: O(n), where n is len(tablesize)
        """
        self.count = 0
        self.table = ArrayR(tablesize)

    def is_empty(self):
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
        Returns whether the hash table is full
        :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + ", " + str(value) + ")\n"
        return result
