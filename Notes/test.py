"""
from math import sqrt
def improve(update, close, guess=1):
    while not (close(guess)):
        guess = update(guess)
    return guess
def golden_update(guess):
    guess = 1 + 1/guess
    return guess
def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)
def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance
improve(golden_update, square_close_to_successor)

phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), "bad approximimprove_test()"
    """
"""
import numpy as np
h = np.array([1, 1/2, 1/3, 1/2, 1/3, 1/4, 1/3, 1/4, 1/5])
H = np.reshape(h, (3, 3))
y = np.array([23/6, 9/4, 97/60])
print(np.linalg.solve(H, y))
"""
def ka(f, e):
    return (f - e)*(f - e)/e
sum = ka(58, 41.48) + ka(51, 44.88) + ka(47, 46.27) + ka(44, 54.14) + ka(22 , 33.78) + ka(14 , 15.73) + ka(31, 47.82)\
    + ka(46, 52.12) + ka(53, 53.73) + ka(73, 62.86) + ka(51, 39.22) + ka(20, 18.27)
print(sum)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    