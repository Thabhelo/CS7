"""Lab 1: Expressions and Control Structures"""

#Replace with your email here
email = "thabheloduve@gmail.com"
assignment = "lab1"

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    result = 0 # this is like a container variabe where we keep on adding up subsequent rightmost digits until we reach a point when n is no longer > 0
    while n > 0:
        rightmost_digit = n % 10 # % mod dividing will divide n by 10, and keep only the remainder e.g 4224/10 = 422.4 and 4229//10 = 422 and 4224 % 10 = 4
        result = result + rightmost_digit # new_val_of_result = current_val_of_result + rightmost_digit
        n = n // 10 
    return result


    total = 0
    while n > 0:
        rightmost_digit = n % 10 # reserve (cupha) the right-most digit ulibeke laphana e.g removing 8 from 236478
        total += rightmost_digit
        n //= 10 # your new n is the remaining number after removing the right most e.g 23647
    return total



# The questions below are completely optional.

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    if k == 0:
        return 1
    elif k == 1:
        return n

    factorial = 1        
    while k > 0:
        factorial = factorial * n
        n -= 1
        k -= 1
    return factorial

    


'''

The loop checks whether `k` is greater than `0`, and if so, multiplies `n` by itself, decrements `n` by 1, and decrements `k` by 1.
The loop continues until `k` reaches `0`, at which point the function returns the accumulated result.
The `falling` function should work correctly for all non-negative integer inputs, including cases where `k` is greater than `n`
(in which case the result should be `0` since the falling factorial is undefined in that case).
The test cases provided in the docstring demonstrate some examples of expected behavior.

'''


def double_eights(n):
    """
    Return True if n has two eights in a row.

    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    previous_digit = None
    while n > 0:
        digit = n % 10
        if digit == 8 and previous_digit == 8:
            return True
        previous_digit = digit
        n //= 10
    return False



'''
total = 0
while n > 0:
    total = total + n % 10 # 24 % 10 = 4
    n = n // 10 # our new n is 2
return total
'''



'''def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """

n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return while

def f (f, x):
    return f(x + n)

f = f(f, n)
g = (lambda y: y())(f)
'''
