#def greet():
#    print("Hello")
#    print("Welcome to python practice")
#greet()

#----------------Arguments
#def greet(f_name, l_name):
#    print(f"Hello {f_name} {l_name}")
#    print("Welcome to python practice")
#greet("golla","ranganadh")

#--------------------types of functions(perform a task & return a value)
#def greet(name):
#    print(f"Hello {name}")
#print(greet("ranganadh"))

#------------------keyword arguments
#def increment(number, by):
#    return number + by
#print(increment(4,1))

#-----------------default arguments
#def increment(number, by = 1):
#    return number + by
#print(increment(5))

#-------------------*args
#def multiply(*numbers):
#    total = 1
#    for n in numbers:
#        total *= n
#    return total
#print(multiply(2,3,4,5))

#---------------------**args
#def save_user(**user):
#    print(user)
#save_user(id = 1, name = "ranganadh", age = 22)

#----------------------scope
#message = "a"
#def greet(name):
#    global message
#    message = "b"
#greet("ranganadh")
#print(message)