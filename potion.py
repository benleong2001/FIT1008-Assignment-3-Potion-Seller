""" Potion Class!
This file is the class which acts as a blueprint for all potions
which the player (us!) buys from the Vendors of PotionCorp
and sells to the adventurers.
"""
from __future__ import annotations

__author__ = 'Benjamin Leong Tjen Ho, Lim Jing Kai'

Numeric = (int, float)


class Potion:
    """ A Potion which is sold by Vendors and purchased by Adventurers.
    Attribute(s):
        potion_type (str):  The type of the Potion.
        name (str):         The name of the Potion.
        buy_price (float):  The buying price of the Potion.
        quantity (float):   The quantity of the Potion, in litres.

    Class Variable(s):
        None
    """

    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        """ Basic Potion object initialiser.
        :param potion_type: The type of the Potion.
        :param name:        The name of the Potion.
        :param buy_price:   The buying price of the Potion.
        :param quantity:    The quantity of the Potion, in litres.
        :returns:           None
        :complexity:        Worst Case - O(IsIns)

        -------------------------------------------------------------------------------------------------
        METHODS CALLED   |  COMPLEXITY  |   REMARKS
        -----------------|--------------|----------------------------------------------------------------
        set_buy_price()  |  O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        set_name()       |  O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        set_potion_type()|  O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        set_quantity()   |  O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        -----------------|--------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        self.set_potion_type(potion_type)
        self.set_name(name)
        self.set_buy_price(buy_price)
        self.set_quantity(quantity)

    # Mutator Methods
    def set_potion_type(self, potion_type: str) -> None:
        """ Mutator for potion_type attribute of a Potion.
        :param potion_type: New Potion potion_type value.
        :returns:           None
        :complexity:        Worst Case - O(IsIns)
        :pre:               Input potion_type must be a string.
        :raises TypeError:  When potion_type is not a string.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(potion_type, str):
            raise TypeError("".join(["Parameter potion_type must be a string: potion_type = ", str(potion_type)]))

        # Initialising Potion's potion_type attribute
        self.potion_type = potion_type

    def set_name(self, name: str) -> None:
        """ Mutator for name attribute of a Potion.
        :param name:        New Potion name value.
        :returns:           None
        :complexity:        Worst Case - O(IsIns)
        :pre:               Input name must be a string.
        :raises TypeError:  When name is not a string.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(name, str):
            raise TypeError("".join(["Parameter name must be a string: name = ", str(name)]))

        # Initialising Potion's name attribute
        self.name = name

    def set_buy_price(self, buy_price: float) -> None:
        """ Mutator for buy_price attribute of a Potion.
        :param buy_price:   New Potion buy_price value.
        :returns:           None
        :complexity:        Worst Case - O(IsIns)
        :pre:               Input buy_price must be positive and Numeric.
        :raises TypeError:  When input buy_price is not Numeric.
        :raises ValueError: When input quantity is non-positive.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(buy_price, bool) or not isinstance(buy_price, Numeric):
            raise TypeError("".join(["Parameter buy_price must be Numeric: buy_price = ", str(buy_price)]))
        elif buy_price <= 0:
            raise ValueError("".join(["Parameter buy_price must be positive: buy_price = ", str(buy_price)]))

        # Initialising Potion's buy_price attribute
        self.buy_price = buy_price

    def set_quantity(self, quantity: float) -> None:
        """ Mutator for quantity attribute of a Potion.
        :param quantity:    New Potion quantity value.
        :returns:           None
        :complexity:        Worst Case - O(IsIns)
        :pre:               Input quantity must be non-negative and Numeric.
        :raises TypeError:  When input buy_price is not Numeric.
        :raises ValueError: When input quantity is negative.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(quantity, bool) or not isinstance(quantity, Numeric):
            raise TypeError("".join(["Parameter quantity must be Numeric: quantity = ", str(quantity)]))
        elif quantity < 0:
            raise ValueError("".join(["Parameter quantity must be non-negative: quantity = ", str(quantity)]))

        # Initialising Potion's quantity attribute
        self.quantity = quantity

    # Accessor Methods
    def get_potion_type(self) -> str:
        """ Accessor method for Potion's potion_type attribute.
        :returns:       Returns the Potion's potion_type attribute.
        :complexity:    Worst Case - O(1)
        """
        return self.potion_type

    def get_name(self) -> str:
        """ Accessor method for Potion's name attribute.
        :returns:       Returns the Potion's name attribute.
        :complexity:    Worst Case - O(1)
        """
        return self.name

    def get_buy_price(self) -> float:
        """ Accessor method for Potion's buy_price attribute.
        :returns:       Returns the Potion's buy_price attribute.
        :complexity:    Worst Case - O(1)
        """
        return self.buy_price

    def get_quantity(self) -> float:
        """ Accessor method for Potion's quantity attribute.
        :returns:       Returns the Potion's quantity attribute.
        :complexity:    Worst Case - O(1)
        """
        return self.quantity

    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> Potion:
        """ Alternative constructor that always sets the quantity as 0
        :param potion_type: The potion type of the Potion created.
        :param name:        The name of the Potion created.
        :param buy_price:   The buying price of the Potion created.
        :returns:           Returns a potion with the input attributes but with 0 quantity
        :complexity:        O(IsIns)

        -------------------------------------------------------------------------------------------------
        METHODS CALLED    | COMPLEXITY  |   REMARKS
        ------------------|-------------|----------------------------------------------------------------
        Potion.__init__() | O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ------------------|-------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------
        """
        return Potion(potion_type, name, buy_price, 0)

    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int) -> int:
        """ Good hashing function
        :param potion_name: The Potion name being hashed.
        :param tablesize:   The size of the hash table which the Potion is added to.
        :return:            The hash value of the Potion.
        :complexity:        O(IsIns + len(potion_name))
        :pre:               Input potion_name must be a string.
        :pre:               Input tablesize must be a positive integer.
        :raises TypeError:  When potion_name is not a string or tablesize is not an integer.
        :raises ValueError: When tablesize is non-positive.

        -------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|----------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ord()           |   O(1)        |   Assumed to be O(1) as it just requires to convert a
                        |               |       character to its ASCII equivalent value
        ----------------|---------------|----------------------------------------------------------------
        -------------------------------------------------------------------------------------------------

        Note:
            The method includes a loop which goes through the characters of potion_name.
            Hence, the loop has a total complexity of O(len(potion_name)).
        """
        # Checking pre condition(s)
        if not isinstance(potion_name, str):
            raise TypeError("".join(["potion_name must be a string: potion_name = ", str(potion_name)]))
        elif isinstance(tablesize, bool) or not isinstance(tablesize, int):
            raise TypeError("".join(["tablesize must be an integer: tablesize = ", str(tablesize)]))
        elif tablesize < 1:
            raise ValueError("".join(["tablesize must be a positive integer: tablesize = ", str(tablesize)]))

        # Hashing potion_name
        value = 0
        a = 31415
        b = 27183

        # For each iteration, value gets multiplied with some pseudo random integer.
        # Each time the hash function is called, it will produce the same i-th integer every time.
        # However, the pseudo randomness encourages uniformity as well as
        #   extreme changes in the hash value for small changes in the key value.
        for char in potion_name:
            value = (ord(char) + a * value) % tablesize
            a = a * b % (tablesize - 1)
        return value

    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int) -> int:
        """ Bad hashing function
        :param potion_name: The Potion name being hashed.
        :param tablesize:   The size of the hash table which the Potion is added to.
        :return:            The hash value of the Potion.
        :complexity:        O(IsIns)
        :pre:               Input potion_name must be a string.
        :pre:               Input tablesize must be a positive integer.
        :raises TypeError:  When potion_name is not a string or tablesize is not an integer.
        :raises ValueError: When tablesize is non-positive.


        -----------------------------------------------------------------------------------------------------
        METHODS CALLED      |   COMPLEXITY  |   REMARKS
        --------------------|---------------|----------------------------------------------------------------
        isinstance()        |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        ord()               |   O(1)        |   Assumed to be O(1) as it just requires to convert a
                            |               |       character to its ASCII equivalent value
        str.__getitem__()   |   O(1)        |
        --------------------|---------------|----------------------------------------------------------------
        -----------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(potion_name, str):
            raise TypeError("".join(["Parameter potion_name must be a string: potion_name = ", str(potion_name)]))
        elif isinstance(tablesize, bool) or not isinstance(tablesize, int):
            raise TypeError("".join(["Parameter tablesize must be an integer: tablesize = ", str(tablesize)]))
        elif tablesize < 1:
            raise ValueError("".join(["Parameter tablesize must be a positive integer: tablesize = ", str(tablesize)]))

        # Hashing potion_name (terribly)
        a = 2
        return ord(potion_name[0]) * a % tablesize
