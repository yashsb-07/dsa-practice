n = int(input("Enter n: "))

for i in range(1, n):
    for j in range(i, (n-1)+1):
        print("*", end="")
    print()
