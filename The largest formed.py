a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")
d = input("Enter the last number: ")

L =[]
# itertools.permutations use str
import itertools
y = list(itertools.permutations([a,b,c,d]))

for i in y:
  x = ""
  for j in i:
    x = x + j
  L.append(x)

print('The largest formed number is',max(L))
