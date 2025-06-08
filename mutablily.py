#print("jeba jehejeba  heje63653553")
# jeba print("52v syvw wjeba  w")

# name = "jeba"
# print(dir(name))
a =5
b =a 
print(a is b)  # True, both refer to the same integer object
print(a == b)  # True, both have the same value

b= 5
print(a is b)  # True, still the same integer object
print(a == b)  # True, both still have the same value

l1 = [1, 2, 3, 4, 5]
l2 = l1
print(l1 is l2)  # True, both refer to the same list object
print(l1 == l2)  # True, both lists have the same content

l2 = [1, 2, 3, 4, 5]
print(l1 is l2)  # False, l2 now refers to a new list object
print(l1 == l2)  # True, both lists still have the same content

s = "hello"
s2 = s
print(s is s2)  # True, both refer to the same string object
print(s == s2)  # True, both strings have the same content
s2 = "hello"
print(s is s2)  # True, still the same string object  
print(s == s2)  # True, both strings still have the same content

p = "jeba"
q = p
#p[0]= 'J'  # This will raise an error because strings are immutable
p = "Jeba"  # This is valid, now p refers to a new string object
print(p is q)  # False, p now refers to a new string object
print(p == q)  # false, p and q have different content
print(p, q)  # Output: Jeba jeba 
