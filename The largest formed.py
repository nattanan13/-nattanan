a = input('Enter the first number: ')
b = input('Enter the second number: ')
c = input('Enter the third number: ')
d = input('Enter the last number: ')

L = [a,b,c,d]

import itertools
y = list(itertools.permutations([L]))

print(y)



