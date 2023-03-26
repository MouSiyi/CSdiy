## Print and None
The special value *None* represents nothin in Python      
A func that does not explicitly return a value will return None
```python
None
#return nothing

def does_not_square(x):
    x*x
does_not_square(4)
#return nothing
```
**Pure Functions& Non-Pure Functions**
Pure function just return values;    
Non-Pure function have side effects(anything happens as a consequence of function calling)
```python
print(print(1),print(2))
1 #the side effct of print(1); 
#the interpreter does not auto display None when it is the value of an expression
2
None None #the return value of print() is None 
```

## Miscellaneous Python Features

**operators**
mathematical operators provide a method of *combination*    
each have their own evaluation procedures;can be thought of as short-hand for call expressions    
```python
from operator import floordiv, mod
5//4 == floordiv(5,4)
2013%10 == mod(2013,10)
```

**doctest**
```python
def divide_exact(n,d):
    """Return the quotient and remainder of div of n,d

    >>> q, r =divide_exact(2013,10)
    >>> q
    201
    >>> r 
    3
    """
    return n//d,n%d
quotient, remainder = divide_exact(2022,10)
#using python3 -m doctest -v [filename].py to implement a doctest
```

**default argument**    
The parameter having a default parameter has to be placed after other parameters.

## Conditional Statements
A *statement* is executed by the interpreter to perform an action
*Compound statement*(spend more than one line):
```python
#the whole thing is a statement
<header>#determines a statement's type; "controls" the suite that follows
    <statement>
    <statement>
    ...
    #suite of the clause; to execute its sequence of statements in order
#a clause
<separating header>
    <statement>
    <statement>
    ...

```
Execution rule for conditional statements:    
Each clause is considered in order.    
1. Evaluate the header's expression.
2. If it is a true value, execute the suite and skip the remaining clauses.    
Syntax: if; elif; else    

False values: False, 0, '', None...
True values: anything else

## Iteration
**while statement**     
Execution rule:    
1. Evaluate the header's expression.
2. If it is a true value, execute the whole suite, then return to step 1.

