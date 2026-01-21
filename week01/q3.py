#Question3: Order of operations

a = 1
b = 2
c = 3
d = 4

#Fully- bracketed Version of: e=a-b**c//d+a%c
e = (a -((b**c) // d)) + (a%c)
print(e)
