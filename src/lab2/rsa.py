import random
import typing as tp

def is_prime(n: int) -> bool:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    # PUT YOUR CODE HERE
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    # PUT YOUR CODE HERE
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)

