""" Primes
Description:
    This file contains the method largest_prime().
    This method is used to determine the best tablesize in LinearProbePotionTable class, in hash_table.py file.
"""
__author__ = 'Benjamin Leong Tjen Ho'

MAX_SIZE = 100000


def largest_prime(k: int) -> int:
    """ Method to produce the largest prime number smaller than k
    :param k:           The upper limit where the returning prime number must be lesser than (exclusive).
    :return:            The largest prime number, strictly lesser than k.
    :complexity:        O(k)
    :pre:               Input k must be a positive integer larger than 2 and smaller or equal to 100000.
    :raises TypeError:  When input k is not an integer.
    :raises ValueError: When input k is less than 3 or larger than 100000.

    -------------------------------------------------------------------------------------------------
    METHODS CALLED    | COMPLEXITY  |   REMARKS
    ------------------|-------------|----------------------------------------------------------------
    isinstance()      | O(IsIns)    |   Unknown complexity for built-in function. Assumed to be O(1).
    list.__getitem__()| O(1)        |
    list.__setitem__()| O(1)        |
    ------------------|-------------|----------------------------------------------------------------
    -------------------------------------------------------------------------------------------------
    """
    # Checking pre condition(s)
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("".join(["Input k must be an integer: k = ", str(k)]))
    elif k < 3 or k > MAX_SIZE:
        raise ValueError("".join(["Input k must be between 3 and 100000 (inclusive): k = ", str(k)]))

    # Creating a list of k elements representing numbers 0 to k-1
    # True if the index is prime, False otherwise
    prime_list = [True] * k  # 0 to k exclusive

    # We know 0 and 1 are not prime
    prime_list[0] = prime_list[1] = False

    # Looping through the elements of the list until the square root of k
    for i in range(2, int(k ** 0.5 // 1)):
        num = i ** 2
        # Going through all multiples of i
        # starting from it's square until it reaches k
        if prime_list[i]:
            while num < k:
                prime_list[num] = False
                num += i

    # Finding the largest prime smaller than k
    # This is done by traversing the list from the end to the start
    #   and then returning the first index found where the element is True.
    for j in range(k - 1, -1, -1):
        if prime_list[j]:
            return j

    raise ValueError("Largest prime smaller than k not found")


if __name__ == "__main__":
    N = MAX_SIZE  # Must be less than MAX_SIZE
