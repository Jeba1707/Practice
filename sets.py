#properties of sets in Python
# Sets are unordered collections of unique elements.
# They are mutable, meaning we can add or remove elements.
# Sets do not allow duplicate values, and they are defined using curly braces {} or the set() constructor.
# Sets are useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations


#creating an empty set

set2 = {} #its a dictionary, not a set
# To create an empty set, we should use set() instead of {}

set1 = set()  # Creating an empty set
set1.add(10)  # Adding an element to the set
set1.add(20)  # Adding another element to the set
set1.add(30)  # Adding yet another element to the set
print(set1)  # Output: {10, 20, 30}

set = {22 , 23, 34, 32, 22, 23}  # Creating a set with duplicate values
print(set)  # Output: {32, 34, 22, 23}
print(type(set))  # Output: <class 'set'>

# Sets are unordered collections of unique elements
# Duplicate values are automatically removed

# Adding elements to a set
set.add(100)  # Adding 100 to the set
print(set)  # Output: {32, 34, 100, 22, 23}
set.add(200)  # Adding 200 to the set
print(set)  # Output: {32, 34, 100, 200, 22, 23}

# Adding multiple elements using update method
set.update([300, 400])  # Adding 300 and 400 to the set
print(set)  # Output: {32, 34, 100, 200, 22, 23, 300, 400}

# Removing elements from a set
set.remove(100)  # Removing 100 from the set
print(set)  # Output: {32, 34, 200, 22, 23, 300, 400}
set.discard(200)  # Discarding 200 from the set
print(set)  # Output: {32, 34, 22, 23, 300, 400}

# Removing an element that does not exist using discard will not raise an error
set.discard(500)  # Attempting to discard 500, which does not exist
print(set)  # Output: {32, 34, 22, 23, 300, 400}

# Removing an element that does not exist using remove will raise an error
# set.remove(500)  # Uncommenting this line will raise a KeyError

# Checking if an element exists in the set
print(22 in set)  # Checking if 22 is in the set, Output: True
print(100 in set)  # Checking if 100 is in the set, Output: False

# Iterating through the set
for item in set:
    print(item)  # Output: 32, 34, 22, 23, 300, 400 (order may vary)

# Clearing the set
set.clear()  # Clearing all elements from the set
print(set)  # Output: set() (empty set)

# Creating a frozenset (immutable set)
#frozenset is a built-in type in Python that creates an immutable set.
frozen_set = frozenset([1, 2, 3, 4, 5])  # Creating a frozenset
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})
print(type(frozen_set))  # Output: <class 'frozenset'>

# Attempting to add an element to a frozenset will raise an error
# frozen_set.add(6)  # Uncommenting this line will raise an AttributeError
# Attempting to remove an element from a frozenset will raise an error
# frozen_set.remove(1)  # Uncommenting this line will raise an AttributeError
# Checking if an element exists in the frozenset
print(3 in frozen_set)  # Checking if 3 is in the frozenset # Output: True
print(6 in frozen_set)  # Checking if 6 is in the frozenset # Output: False

# Iterating through the frozenset
for item in frozen_set:
    print(item)  # Output: 1, 2, 3, 4, 5 (order may vary) 

# Clearing the frozenset
# frozen_set.clear()  # Uncommenting this line will raise an AttributeError since frozenset is immutable
