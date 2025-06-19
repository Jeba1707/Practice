# Functions in Python
# Functions are reusable blocks of code that perform a specific task. They can take inputs (arguments) and return outputs (results).
# Functions help in organizing code, making it more readable and maintainable.
#basic syntax:
# def function_name(parameters):
#     # code block
#     return value



#--------------------------------
def square(num): 
  return num ** 2 
print(square(5))

#--------------------------------
# def sum(num1, num2): 
#   return num1 + num2
# print(sum(3, 4))

#--------------------------------
def multiply(p1,p2):
  return p1 * p2
print(multiply(2, 3))
print(multiply("Hi ", 5))

#--------------------------------
def greet(name = "user"):
  return "Hello, " + name

print(greet())
print(greet("Alice"))

#--------------------------------
#-----------Lambda Functions-----------

cube = lambda x: x ** 3
print(cube(3)) #prints 27

multiply = lambda x, y: x * y
print(multiply(2, 5)) #prints 10

#--------------------------------
#-----------*args---------------- #args allows for variable number of arguments
def add(*args):
    return sum(args)

print(add(1, 2, 3)) #prints 6
print(add(1, 2, 3, 4, 5)) #prints 15

#--------------------------------
def names(*args):
    return " ".join(args)
print(names("Alice", "Bob", "Charlie")) #prints "Alice Bob Charlie" 
 
#-------------------------------- 
def print_args(*args):
    for arg in args:
        print(arg)
print_args("Hello", "World", 123) #prints each argument on a new line

#--------------------------------
#-------------args is a tuple-------------

def show(*args):
    print(args) # Prints the tuple of arguments
    print(*args)  # Unpacking the tuple

print(show(1, 2, 3)) #prints (1, 2, 3) and then 1 2 3 

#--------------------------------
def square_numbers(*args):
    for num in args:
       print(num ** 2, end=' ')
    print()  # New line after printing all squares
square_numbers(1, 2, 3, 4)  # prints 1 4 9 16

#--------------------------------
#-------------**kwargs---------------- #kwargs allows for variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print_info(name="Bob", age=25, country="USA", hobby="Reading")
print_info(name = "Charlie")  # Only name provided
print_info()  # No arguments, nothing will be printed        

#--------------------------------
#-------------yeild----------------

def even_numbers(n):
    for i in range(2, n + 1, 2):
            yield i 

print(even_numbers(10))  # Prints a generator object
for num in even_numbers(10):
    print(num, end=' ')  # Prints even numbers from 2 to 10: 2 4 6 8 10

#--------------------------------
# -------------Generators----------------
# Generators are a special type of iterator that allow you to iterate through a sequence of values without storing them all in memory at once.
# They are defined using the `yield` keyword, which allows the function to return a value and pause its execution, resuming later from where it left off.
# Generators are useful for working with large datasets or streams of data, as they can produce values on-the-fly without requiring the entire dataset to be loaded into memory.


#---------------------------------
#-------------return vs yield----------------
def count_up_to(n):
    for i in range(1, n + 1):
        yield i  # Yielding values one by one
def count_up_to_return(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)  # Collecting all values in a list
    return result  # Returning the entire list at once


#---------------------------------
#-------------recursion----------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # prints 120