#----------while loop-------------------

i = 1 
while(i <= 10):
    print('*')
    i += 1

j = 1
while(j <= 5):
    print(j * ' jeba')
    j = j +1

print(j)  # Output: 6
print(i)  # Output: 11

#----------while loop with list-------------------
l = [2, "jeba", True, 3.14 ,"hello"]
k = 0
while(k<len(l)):
    print(l[k])  # Output: jeba, True, 3.14, hello
    k += 1

#----------range function-------------------
print(range(5)) # Output: range(0, 5)
numbers = list(range(5))  # Convert range to a list
print(numbers)  # Output: [0, 1, 2, 3, 4] 

#----------for loop-------------------
for i in range(1, 6):
    print(i)  # Output: 1 2 3 4 5

#----------for loop with list-------------------
list = [1, 2, 3, 4, 5]
for i in list:
    print(i) 

string = "Tasnim"    
for char in string:
    print(char)  # Output: T a s n i m

#-----------using end parameter in print-------------------
todolist = ["study", "exercise", "read"]
for task in todolist:
    print(task , end=" ")  # Output: study exercise read
  
print()  # Print a newline after the loop
print("All tasks completed!")  # Output: All tasks completed!

name = "Tasnim"
for char in name:
    print(char, end=" ")  # Output: T a s n i m

#----------for loop with else-------------------

mylist = [100,200,300,400,500]
for i in mylist:
    print(i)  # Output: 100 200 300 400 500
else:
    print("Loop completed successfully!")  # Output: Loop completed successfully!



