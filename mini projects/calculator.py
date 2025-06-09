a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

if op =='+':
   result = a + b
elif op =='-':    
    result = a - b
elif (op =='*'):           #also can witten in this way
    result = a * b
elif op =='/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."

print("Result:", result)