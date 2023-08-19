# Numeric expressions
2022
2000 + 22
0 + (1 + 2) + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Call expressions
max(2.0, 1.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(min(1, -2), min(pow(3, 5), -4))
abs(-4)
pow(2, 3) == 2 ** 3

# Importing and arithmetic with call expressions
from operator import add, mul
add(1, 2)
mul(3, 3)
mul(add(2, mul(4, 6)), add(3, 5))
mul(10, add(mul(add(2, mul(4, 6)), add(3, 5)), -6.5))

from operator import sub, mul, truediv, floordiv, mod
truediv(9, 4)
floordiv(9, 4)
mod(9, 4)


# Objects
# Note: Download from the course website
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)
max(words)
max(words, key=len)

# Reversals
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
