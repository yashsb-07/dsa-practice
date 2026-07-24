n = int(input("Enter n: "))

space = 2 *(n-1)
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    for j in range(1, space+1):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    space -= 2
    print()