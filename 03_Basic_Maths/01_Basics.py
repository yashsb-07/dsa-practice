# Que: Count the number - Loop-Based Approach

n = 5438
count = 0

num = n
while num > 0:
    count += 1
    num = num // 10
    # print(count)

# Que: Print the number

n = 5438

num = n
while num > 0:
    last_digit = num % 10
    # print(last_digit)
    num = num // 10

# Logarithm-Based Approach

from math import *

num = 3456

def countDigit():
    return int(log10(num) + 1)

# Que1: Check number is palindrome or not

n = 121
num = n
result = 0 

while num > 0:
    last_digit = num % 10
    result = (result*10) + last_digit
    num = num // 10

if n == result:
    print("Palindrome")
else:
    print("Not Palindrome")

