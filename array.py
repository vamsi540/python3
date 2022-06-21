#import array as arr

from array import *

#vals = array('i',[5,9,8,4,2])

#newArr = array(vals.typecode, (a for a in vals))

#for e in newArr:
#    print(e)

#vals = array('i',[5,9,8,4,2])

#newArr = array(vals.typecode, (a for a in vals))
#i = 0
#while i < len(newArr):
#    print(newArr[i])
#    i += 1

arr = array('i', [])
n = int(input("enter the length of array"))

for i in range(n):
    x = int(input("enter the next value"))
    arr.append(x)

print(arr)

val = int(input("enter the value for search"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1
print(arr.index(val))