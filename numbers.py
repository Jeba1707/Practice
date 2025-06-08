a = 2
b = a + 2.2 
print(a, b)  # Output: 2 4.2
print(type(a), type(b))  # Output: <class 'int'> <class 'float'>

x , y , z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3
print(x +2 , y + 2, z + 2)  # Output: 3 4 5
print(x + y + z)  # Output: 6

repr("hello")  # Output: "'hello'"
print(repr("hello"))  # Output: 'hello'

print(repr(5))  # Output: '5'
print(repr(5))  # Output: '5'

str("hello")  # Output: 'hello'
print(str("hello"))  # Output: 'hello'
print(str(5))  # Output: '5'
print(str(5.5))  # Output: '5.5'

print(str(5 + 2j))  # Output: '(5+2j)'

#repr defines how an object is represented in a way that can be evaluated by Python
#str defines how an object is represented in a way that is more user-friendly 
#repr is used for debugging and development, while str is used for end-user display
#repr is more precise and unambiguous, while str is more readable and informal


import math 
print(math.floor(5.5))  # Output: 5 returns the largest integer less than or equal to 5.5
print(math.ceil(5.5))   # Output: 6 # returns the smallest integer greater than or equal to 5.5

print(math.floor(-5.5))  # Output: -6 # returns the largest integer less than or equal to -5.5
print(math.ceil(-5.5))   # Output: -5 # returns the smallest integer greater than or equal to -5.5

print(math.trunc(5.5))  # Output: 5 # returns the integer part of 5.5
print(math.trunc(-5.5))  # Output: -5 # returns the integer part of -5.5


print(0o20)  # Output: 16 # octal representation of 16
print(0x10)  # Output: 16 # hexadecimal representation of 16
print(0b10000)  # Output: 16 # binary representation of 16
print(0o20 + 0x10 + 0b10000)  # Output: 48 # sum of octal, hexadecimal, and binary representations of 16
print(0o20 + 0x10 + 0b10000 == 16)  # Output: False # sum is not equal to 16, it's 48

import random
print(random.random())  # Output: a random float between 0.0 and 1.0
print(random.randint(1, 10))  # Output: a random integer between 1 and 10 (inclusive)
print(random.choice([1, 2, 3, 4, 5]))  # Output: a random element from the list [1, 2, 3, 4, 5]

l1 = ['jeba', 'jebin','tasnim', 'tasin']
print(random.choice(l1))  # Output: a random element from the list l1
print(random.sample(l1, 2))  # Output: a random sample of 2 elements from the list l1
l2 = random.shuffle(l1) # Output: None, shuffles the list l1 in place
 

print(0.1+0.1+0.1)  # Output: 0.30000000000000004, due to floating-point precision issues
print((0.1 + 0.1 + 0.1 )- 0.3)  # Output: 5.551115123125783e-17, a very small number close to zero, due to floating-point precision issues
print(0.1 + 0.1 + 0.1 == 0.3)  # Output: False, due to floating-point precision issues
print(round(0.1 + 0.1 + 0.1, 2) == 0.3)  # Output: True, rounding to 2 decimal places resolves the precision issue
print(round(0.1 + 0.1 + 0.1, 2)) # Output: 0.3, rounding to 2 decimal places gives the expected result
print(round(0.1 + 0.1 + 0.1, 2)- 0.3) # Output: 0.0, no precision issues after rounding

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Output: 0.3, using Decimal for precise decimal arithmetic
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))- Decimal('0.3'))  # Output: 0.0, no precision issues with Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))  # Output: True, no precision issues with Decimal


print(True==1)  # Output: True, True is equivalent to 1
print(False==0)  # Output: True, False is equivalent to 0 
print(True is 1)  # Output: False, True is not the same object as 1
print(False is 0)  # Output: False, False is not the same object as 0
print(True + 4)  # Output: 5, True is treated as 1 in arithmetic operations
