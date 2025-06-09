colors = ["red", "green", "blue", "yellow", "purple", "orange"]

print(colors) # Output the list of colors
print(colors[0]) # Output the first color
print(colors[1:4]) # Output a slice of the list from index 1 to 3

print(colors[-1]) # Output the last color
print(colors[-3:]) # Output the last three colors

# --------Adding a new color to the list-------------
colors.append("pink")
print(colors) # Output the updated list of colors 

# --------Removing a color from the list-------------
colors.remove("yellow")