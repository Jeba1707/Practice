#properties of dictionary
# Dictionaries are unordered collections of key-value pairs.
# They are mutable, meaning we can add, remove, or change elements.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Keys must be unique and immutable, while values can be of any type.


marks = {
  "bangla": 22,
  "english": 23,
  "maths": 34,
  "science": 32 }

print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32}
print(marks.keys())  # Output: dict_keys(['bangla', 'english', 'maths', 'science'])
print(marks.values())  # Output: dict_values([22, 23, 34, 32])

print(marks["bangla"])  # Accessing value by key, Output: 22
print(marks.get("english"))  # Accessing value using get method, Output: 23

print(marks.get("history1")) # Accessing a non-existing key using get method, Output: None
# print(marks["history1"]) # Accessing a non-existing key directly will raise KeyError

# Adding a new key-value pair
marks["history"] = 30
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32, 'history': 30}

marks.update({"geography": 28})  # Adding using update method
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32, 'history': 30, 'geography': 28}

# Updating an existing key-value pair
marks["maths"] = 35
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 35, 'science': 32, 'history': 30}

marks.update({"english": 24}) # Updating using update method 
print(marks)  # Output: {'bangla': 22, 'english': 24, 'maths': 35, 'science': 32, 'history': 30}


newMarks = marks.copy()  # Creating a copy of the dictionary
print(newMarks)  # Output: {'bangla': 22, 'english': 24, 'maths': 35, 'science': 32, 'history': 30, 'geography': 28}

# Deleting a key-value pair
del marks["science"]
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 35, 'history': 30}

# Checking if a key exists
print("maths" in marks)  # Output: True
print("geography" in marks)  # Output: False

marks.pop("history")  # Removing a key-value pair using pop method
print(marks)  # Output: {'bangla': 22, 'english': 24, 'maths': 35}

for mark in marks:  # Iterating through keys
    print(mark, marks[mark])  # Output: bangla 22, english 24, maths 35

for key, value in marks.items():  # Iterating through key-value pairs
    print(key, value)  # Output: bangla 22, english 24,    

marks.clear()  # Clearing the dictionary
print(marks)  # Output: {}  


students = {
    "Jeba": {"bangla": 22, "english": 23, "maths": 34, "science": 32},
    "Rima": {"bangla": 25, "english": 26, "maths": 30, "science": 28},
    "Sima": {"bangla": 20, "english": 22, "maths": 35, "science": 30}
} #creating a nested dictionary

print(students)  # Output: {'Jeba': {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32}, ...}
print(students["Jeba"])  # Accessing Jeba's marks, Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32}
print(students["Rima"]["maths"])  # Accessing Rima's maths marks, Output: 30  
print(students["Sima"]["science"])  # Accessing Sima's science marks, Output: 30
# Adding a new student
students["Tina"] = {"bangla": 24, "english": 25, "maths": 33, "science": 31}
print(students)  # Output: {'Jeba': {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32}, ..., 'Tina': {'bangla': 24, 'english': 25, 'maths': 33, 'science': 31}}
# Updating a student's marks
students["Jeba"]["maths"] = 36
print(students["Jeba"])  # Output: {'bangla': 22, 'english': 23, 'maths': 36, 'science': 32}
# Deleting a student
del students["Rima"]

square = {x: x**2 for x in range(1, 11)}  # Creating a dictionary using dictionary comprehension
print(square)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}