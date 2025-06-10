#---------------break-----------------
for i in range(20):
  if(i ==10):
    break  # Exit the loop when i is 10
  print(i)  # Output: 0 1 2 3 4 5 6 7 8 9

  
#---------------continue-----------------
for i in range(20):
  if(i == 10):
    continue  # Skip the iteration when i is 10
  print(i)  # Output: 0 1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19


#---------------pass-----------------
for i in range(20):
  pass  # skip the iteration without doing anything

