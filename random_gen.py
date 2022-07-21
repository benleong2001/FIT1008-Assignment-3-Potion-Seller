from typing import Generator


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:
    """ Random Number Generator class.
        Attributes:
            seed (int): The seed used in the random number generator to create a generator (via lcg()).

        Class Variables:
            None
    """

    def __init__(self, seed: int = 0) -> None:
        """ Constructor for RandomGen class.
        :param seed: The seed value for the generator (via the lcg()).
        """
        self.set_seed(seed)
        self.generator = lcg(pow(2, 32), 134775813, 1, self.get_seed())

    # Mutator Method
    def set_seed(self, seed: int) -> None:
        """ Mutator for RandomGen attribute, seed.
        :param seed:        The seed value for the generator.
        :returns:           None
        :pre:               Input seed must be an integer.
        :raises TypeError:  When input seed is not an integer.

        ------------------------------------------------------------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|---------------------------------------------------------------
        isinstance()    |   O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1)
        ----------------|---------------|---------------------------------------------------------------
        ------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if isinstance(seed, bool) or not isinstance(seed, int):
            raise TypeError("".join(["Parameter seed must be an integer: seed = ", str(seed)]))

        # Initialising RandomGen's seed attribute
        self.seed = seed

    # Accessor Method
    def get_seed(self) -> int:
        """ Accessor for RandomGen attribute, seed.
        :returns:    The seed value for the generator.
        """
        return self.seed

    def randint(self, k: int) -> int:
        """ Produces a random integer between 1 and k.
        :param k:           The upper bound of what number can be produced.
        :returns:           A random integer between 1 and k.
        :complexity:        O(1)
        :pre:               Input k must be an integer.
        :raises TypeError:  When input k is not an integer.
        :raises ValueError: When input k is non-positive.

        --------------------------------------------------------------------------------------------------
        METHODS CALLED     | COMPLEXITY  |   REMARKS
        -------------------|-------------|----------------------------------------------------------------
        isinstance()       | O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
        enumerate()        | O(1)        |   Here, it should be O(len(list)) but len(list) = 16 --> O(1).
        list.__setitem__() | O(1)        |
        list.append()      | O(1)        |
        pow()              | O(1)        |
        -------------------|-------------|----------------------------------------------------------------
        --------------------------------------------------------------------------------------------------
        """
        digits: list[int]
        final_num: int
        rand_num_list: list[int]

        # Checking pre condition(s)
        if isinstance(k, bool) or not isinstance(k, int):
            raise TypeError("".join(["Input k must be an integer: k = ", str(k)]))
        if k < 1:
            raise ValueError("".join(["k must be a positive integer: k = ", str(k)]))

        rand_num_list = []
        digits = [0] * 16
        final_num = 0

        # O(5) --> O(1)
        for _ in range(5):
            rand_num_list.append(next(self.generator) // pow(2, 16))

        # O(5) --> O(1)
        for rand in rand_num_list:
            # O(16) --> O(1)
            for i in range(-1, -17, -1):
                digits[i] += rand % 2
                rand //= 2

        # O(16) --> O(1)
        for ind, dig in enumerate(digits):
            final_num += (dig > 2) * pow(2, 15 - ind)
        return final_num % k + 1


if __name__ == "__main__":
    Random_gen = lcg(pow(2, 32), 134775813, 1, 0)
