from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return min((x**2 + y**2), (y**2 + z**2), (x**2 + z**2))


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    #list_of_factors = [ i for i in range(1, n+1) if n % i == 0]
    #return max(list_of_factors)

    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1    


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    True

def true_func():
    print (42)

def false_func():
    print (47)

'''In this solution, the `cond()` function always returns `True`, which means that the `true_func()` will be called when `with_if_statement()` is called, 
and both `true_func()` and `false_func()`will be called when `with_if_function()` is called. 

The `true_func()` and `false_func()` functions print the values `42` and `47`, respectively, and do not return any value. 
The `with_if_statement()` function uses an `if` statement to call the appropriate function based on the result of the `cond()` function, 
while the `with_if_function()` function uses the `if_function()` function to achieve the same result.

Note that in both `with_if_statement()` and `with_if_function()` functions, the `print()` function is used to print the output of the 
`true_func()` and `false_func()` functions. However, since these functions do not return any value,
 the overall result of the functions is `None`, which is what is printed when the `print(result)` statement is executed.
'''

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1
    while n > 1:
        print (n)
        if n % 2 == 0:
            n //= 2
        else:
            n = ((n * 3) + 1)
        count += 1
    print (count)
    return count
   

