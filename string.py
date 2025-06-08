name = "Wajiha Tasnim"

print("Tasnim" in name)  # True
print("Wajiha" not in name)  # False

print(name.find("Tasnim"))  # 7


#-------------string slicing----------------
# # Slicing is used to extract a part of the string
# Syntax: string[start:end:step]


s = name[0:6]  # Extracting substring from index 0 to 6
print(s)  # Wajiha
print(name[7:])  # Extracting substring from index 7 to the end, Output: Tasnim
print(name[:6])  # Extracting substring from the start to index 6, Output: Wajiha

print(name[-6:-1])  # Extracting substring from index -6 to -1, , Output: Tasni
print(name[-6:])  # Extracting substring from index -6 to the end, Output: Tasnim

num = "0123456789"
print(num[0:10:2])  # Extracting every second character from index 0 to 10, Output: 02468
print(num[::2])  # Extracting every second character from the entire string, Output: 02468

# st = input("Enter a string: ")
# print(f"The string you entered is: {st}") 

#--------------replacing strings----------------
letter = '''Dear <name>,
you are selected 
<date>'''
print(letter.replace("<name>", "Wajiha").replace("<date>", "2023-10-01"))
# Output: Dear Wajiha, you are selected on 2023-10-01


#-------------strip methods----------------
st2 = "  Wajiha  Tasnim   "
print(st2)  # Output:   Wajiha  Tasnim
print(st2.strip())  # Removes leading and trailing whitespace, Output: Wajiha  Tasnim
print(st2.strip().replace("  "," "))  # Replaces multiple spaces with a single space, Output: Wajiha Tasnim


#-------------splitting strings----------------
todolist = "buy groceries, clean the house, pay bills"
print(todolist.split(", "))  # Splits the string into a list, Output: ['buy groceries', 'clean the house', 'pay bills']


#-------------joining strings----------------
tasks = ['buy groceries', 'clean the house', 'pay bills']
print(", ".join(tasks))  # Joins the list into a string, Output: buy groceries, clean the house, pay bills

#---------------place holders----------------
order = "You have ordered {} items worth ${}."
print(order.format(5, 99.99))  # Output: You have ordered 5 items worth $99.99

item = input("enter order item: ")
price = input("enter price: ")
print(order.format(item, price))  # Output: You have ordered <item> items worth $<price>.