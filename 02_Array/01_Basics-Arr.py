# USING ARRAY MODULE

# from array import *

# val = array('i', [1,2,3,4,5,6,7])

# copyVal = array(val.typecode, (x*3 for x in val))

# copyVal.remove(15)
# copyVal.pop(3)
# copyVal.pop()

# for i in range(0, len(copyVal)):
#     print(copyVal[i], end=" ")


#1
# for i in range(0, 6): 
    # print(val[i], end=" ")

#2
# for i in val:
#     print(i, end=" ")

# print(val)

# Slicing

# newArr = val[2:6]

# for i in range(0, len(newArr)):
#     print(newArr[i], end=" ")

# arr = array("i", [])

# n = int(input("Enter a num: "))

# for i in range(0, n):
#     arr.append(int(input("Enter next number: ")))

# for i in range(0, len(arr)):
#     print(arr[i], end=" ")


# USING NUMPY 

from numpy import *

# val = array([1,2,3,4,5])

# for x in val:
#     print(x, end=" ")

# Zero Dimentional

zero = array(10)
# print(zero)

one = array([1,2,3,4,5])
# print(one)

two = array([[1,2,3], [4,5,6], [7,8,9]])
# print(two)

three = array([ [ [1,2], [3,4]], [ [5,6], [7,8] ] ])
print(three)