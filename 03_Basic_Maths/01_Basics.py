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
    print(last_digit)
    num = num // 10


