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
    #remember to intent
    """Return the quotient and remainder of div of n,d

    >>> q, r =divide_exact(2013,10)
    >>> q
    201
    >>> r 
    3
    """
    return n//d,n%d
quotient, remainder = divide_exact(2022,10)
#use python3 -m doctest -v [filename].py to implement a doctest
#use help(funcname) to see its docstring
```

**default argument**    
The parameter having a default parameter has to be placed after other parameters.

# Control
Control statements are ones that control the flow of a program's execution based on the results of logical comparisons.
## Statements
Statements are executed.    
Statements govern the relationship among expressions in a program and what happens to their results.
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
1. Expressions, return statements, and assign statements are simple statements.
2. A def statement is a compound statement.The suite following the header defines the function body.      


Each kind of header correspond to specialized evaluation rules for executing its suite, and that's called *control*.      
To execute a sequence of statements, execute the first statement. If that statement does not *redirect control*, then proceed to execute the resr of the sequence of statements,if any remain.      
an example of redirecting control : the process of function application terminates whenever the first return statement is executed


**Execution rule for conditional statements:**
Each clause is considered in order.    
1. Evaluate the header's expression.
2. If it is a true value, execute the suite and skip the remaining clauses.     

Syntax: if; elif; else    

**Boolean context:**     
Their truth values matter to control flow.
False values: False, 0, '', None...
True values: anything else
Every built-in kind of data in Python has both true and false values.    
**Boolean values:**     
Boolean values represent truth values in logical expressions.    
The built-in comparison operations return Boolean values.
**Boolean operators:**      
not;and;or       
**Evaluation procedure for expression <left>and<right>**
1. Evaluate the subexpression <left>.
2. If the result is a false value v, then the expression evaluates to v.
3. Othervise, the expression evaluates to the value of <right>.     

The values, operators, rules provide a way of *combination*.      
Functions that perform comparisons and return boolean values typically begin with ```is```.
  




## Iteration
**while statement**     
Execution rule:    
1. Evaluate the header's expression.
2. If it is a true value, execute the whole suite, then return to step 1.

