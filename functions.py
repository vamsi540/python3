#def greet():
#    print("hello")
#    print("good morning")
#greet()

#def greet():
#    print("hello")
#    print("good morning")
#def add(x,y):
#    c = x + y
#    return c
#greet()
#result = add(5,4)
#print(result)

#def add_sub(x,y):
#    c = x + y
#    d = x - y
#    return c, d
#result1, result2 = add_sub(5,4)
#print(result1, result2)

# function arguments

#def update(x):
#    print(id(x))
#    x = 8
#    print(id(x))
#    print("x", x)
#a = 10
#print(id(a))
#update(a)
#print("a", a)

#def update(lst):
#    print(id(lst))
#    lst[1] = 25
#    print(id(lst))
#    print("lst", lst)
#lst = [10,20,30]
#print(id(lst))
#update(lst)
#print("lst", lst)

# passing list in function

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
lst = [20,25,14,19,16,24,28,47,26]
even, odd = count(lst)
print("even: {} and odd: {}".format(even,odd))