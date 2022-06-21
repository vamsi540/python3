#def add(a,b):
#    c = a + b
#    print(c)
#add(5,6)

#def person(name, age):
#def person(name, age = 18):
#    print(name)
#    print(age)
#person(name = 'ranganadh', age = 23)
#person('ranganadh', 28)

#def sum(*b):
#    c = 0
#    for i in b:
#        c = c + 1
#    print(c)
#sum(5,6,34,78)

# kwargs (keyword variable length arguments)

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i,j)
person('ranganadh', age = 23, city = 'ap', mob = 12345)