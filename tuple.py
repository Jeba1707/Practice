#properties of tuple
# Tuples are ordered collections of elements that are immutable.
# They can contain duplicate values and are defined using parentheses.  
# Tuples are useful for storing a fixed collection of items that should not change.


t = (23,21,44,32,21,66,43,23,22)

print(21 in t)  # Checking if 21 is in the tuple, Output: True
print(100 in t)  # Checking if 100 is in the tuple, Output: False

print(len(t))  # Getting the length of the tuple, Output: 9

#add elements to a tuple
# Tuples are immutable, so we cannot add elements directly.
# However, we can create a new tuple that includes the old one and the new elements.
t = t + (100,)  # Adding 100 to the tuple, Output: (23, 21, 44, 32, 21, 66, 43, 23, 22, 100)

t8 = () # Creating an empty tuple, Output: ()
t8 = t8 + (1, 2, 3)  # Adding elements 1, 2, 3 to the empty tuple, Output: (1, 2, 3)

# Accessing elements in a tuple
print(t)  # Output: (23, 21, 44, 32, 21, 66, 43, 23, 22)

print(t[0])  # Accessing first element, Output: 23

print(t.count(21))  # Counting occurrences of 21, Output: 2

print(t.index(44))  # Finding index of first occurrence of 44, Output: 2
print(t[1:5])  # Slicing from index 1 to 4, Output: (21, 44, 32, 21)
print(t[-1])  # Accessing last element, Output: 22

t2 = (1,) # Creating a single-element tuple, Output: (1,)
t3 = ()  # Creating an empty tuple, Output: ()
 
# Attempting to modify an element will raise an error
# t[0] = 100  # Uncommenting this line will raise a TypeError

# Tuples are immutable, so we cannot add or remove elements
# Attempting to add an element will raise an error


#------------practice----------------
