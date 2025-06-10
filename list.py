colors = ["red", "green", "blue", "yellow", "purple", "orange"]

print(colors) # Output the list of colors
print(colors[0]) # Output the first color
print(colors[1:4]) # Output a slice of the list from index 1 to 3

print(colors[-1]) # Output the last color
print(colors[-3:]) # Output the last three colors

# --------Adding a new color to the list-------------
colors.append("pink") # Append "pink" to the end of the list

# --------Updating an existing color in the list-------------
colors.insert(2, "cyan") # Insert "cyan" at index 2

# --------Removing a color from the list-------------
colors.remove("yellow")

#--------------checking if a color exists in the list-------------
print("yellow" in colors) # Check if "yellow" is in the list, Output: False

print(colors) # Output the updated list of colors 
print(len(colors)) # Output the number of colors in the list

list = ["red", "green", "blue", "yellow", "purple", "orange"]
print(list) # Output the initial list

#-----------Sorting the list-------------
list.sort() # Sort the list in alphabetical order
print(list) # Output the sorted list

# --------Reversing the order of the list-------------
list.reverse() # Reverse the order of the list
print(list) # Output the reversed list

# --------Copying the list-------------
list2 = list.copy() # Create a copy of the list
print(list2) # Output the copied list, Output: []

# --------Clearing the list-------------
list.clear() # Clear all elements from the list
print(list) # Output the cleared list, Output: []

# --------Iterating through the list-------------
for color in list2:
    print(color)  # Output each color in the list