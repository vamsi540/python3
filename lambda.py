# Lambda

#f = lambda a : a * a
#result = f(5)
#print(result)

#f = lambda a,b : a + b
#result = f(5,6)
#print(result)

#def is_even(n):
#    return n%2 == 0
#nums = [3,2,6,8,4,6,2,9]
#evens = list(filter(is_even,nums))
#evens = list(filter(lambda n : n%2 == 0, nums))
#print(evens)

#nums = [3,2,6,8,4,6,2,9]
#even = list(filter(lambda  n : n%2 == 0,nums))
#double = list(map(lambda n : n*2,even))
#print(double)

from functools import reduce

nums = [3,2,6,8,4,6,2,9]
even = list(filter(lambda n : n%2 == 0,nums))
double = list(map(lambda n : n*2,even))
print(double)
sum = reduce(lambda a,b : a + b,double)
print(sum)
