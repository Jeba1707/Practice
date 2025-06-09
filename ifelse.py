age = 16
 
if age >= 18:
    print("You are an adult.")

print("Hello, World!")    #outside the if block

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
else: 
    print("The number is not positive.")

print("This is outside the if-else block.")    


price = float(input("Enter the price of the item: "))
if price > 100:
    print("The item is expensive.")
elif price > 50:
    print("The item is moderately priced.")
else:
    print("The item is cheap.")



# Example of using if-else with a list
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
if "pink" in colors:
    print("pink is in the list of colors.")
elif "green" in colors:
    print("Green is in the list of colors.")
else:
    print("Neither blue nor green is in the list of colors.")    


marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("You got an A grade.")
elif marks >= 80 and marks < 90:
    print("You got a B grade.")
elif marks >= 70 and marks < 80:
    print("You got a C grade.")
elif marks >= 60 and marks < 70:
    print("You got a D grade.")
else:
    print("You got an F grade.")