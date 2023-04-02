**prime factorization**
```python
def prime_factors(n):
    """Print the prime factors of n in non-decreasing order
    >>>prime_factors(858)
    2
    3
    11
    13
    """
    while n>1:
        k=smallest_prime_factor(n)
        n=n//k
        print(k)
        
    return 0
def smallest_prime_factor(n):
    """Return the smallest prime factor i>1 of n
    >>>smallest_prime_factor(858)
    2
    """
    i=2
#    while n>1:
#        if n//i==0:
#            return i
#        else i=i+1
    while n%k !=0:
        k=k+1
    return k
```

**the fibonacci sequence**
```python
def fib(n):
    """Compute the nth Fibonacci number""
```

## Designing Functions
1. Give one function exactly one job
2. Don't repeat yourself
3. Define generally

## Higher-Order Functions
Generalize patterns by defining functions that take arguments that give us back the specific instances of those patterns.
```python
from math import pi
from operator import sq
def area_square(r):
    return area(r,1)
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

def area(r,shapeconst):
    assert r>0, "length must be greater than 0"
    return r*r*shapeconst
#the only different part of those computation processes is the number, shapeconst
```

```python
def sum_naturals(n):
    """Sum the first n natural numbers
    """
    return summation(n,identity)
def sum_cubes(n):
    """Sum the first n cubes of natural numbers
    """
    return summation(n,cube)

def identity(k):
    return k
def cube(k):
    return pow(k,3)
def summation(n,term):
    """Sum the first n terms of a sequence.

    >>>summation(5,cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k+1
    return total
``` 
A higher-order function: a function that takes annother function as an argument.

## Functions as Return Values
Functions defined within other function bodies are bound to names in a local frame