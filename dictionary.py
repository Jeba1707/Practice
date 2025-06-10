marks = {"bangla": 22, "english": 23, "maths": 34, "science": 32 }

print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32}
print(marks["bangla"])  # Accessing value by key, Output: 22
print(marks.get("english"))  # Accessing value using get method, Output: 23

# Adding a new key-value pair
marks["history"] = 30
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 34, 'science': 32, 'history': 30}

# Updating an existing key-value pair
marks["maths"] = 35
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 35, 'science': 32, 'history': 30}

# Deleting a key-value pair
del marks["science"]
print(marks)  # Output: {'bangla': 22, 'english': 23, 'maths': 35, 'history': 30}

# Checking if a key exists
print("maths" in marks)  # Output: True
print("geography" in marks)  # Output: False

