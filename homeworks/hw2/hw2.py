#Fill in your name and surname
name = "Thabhelo"
surname = "Duve"
assignment = "hw2"

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else: 
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n
    else:
        prev1, prev2, prev3 = 3, 2, 1
        i = 4
        while i <= n:
            curr = 1*prev1 + 2*prev2 + 3*prev3
            prev1, prev2, prev3 = curr, prev1, prev2
            i =+ 1
        return curr 

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    
    def pingpong_helper(k, p, direction):
        if k == n:
            return p
        elif k % 7 == 0 or has_seven(k):
            return pingpong_helper(k+1, p-direction, -direction)
        else:
            return pingpong_helper(k+1, p+direction, direction)

    def has_seven(k):
        if k % 10 == 7:
            return True
        elif k < 10:
            return False
        else:
            return has_seven(k // 10)

    return pingpong_helper(1, 1, 1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partition(amount, cent_coints):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif cent_coints > amount:
            return 0
        with_cent_coints = count_partition(amount - cent_coints, cent_coints)
        without_cent_coints = count_partition(amount, 2* cent_coints)
        return without_cent_coints + with_cent_coints
    return count_partition(amount, 1)

    '''if amount == 1:
        return 1
    elif amount == 0:
        return 1
    elif amount < 0:
        return 0
    else:
    '''

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    
    intermediate = 6 - end - start
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, intermediate)
        print_move(start, end)
        move_stack(n-1, start, end)


#The question below is optional

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 0 else n * f(f, n-1))

