n = int(input("Enter n: "))
iniS = 0 

for i in range(n):
    for j in range(n-i):
        print("*", end="")

    for j in range(iniS):
        print(" ", end="")
        
    for j in range(n-i):
        print("*", end="")

    iniS += 2
    print()

iniS = 2 * (n-1)
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")

    for j in range(iniS):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    iniS -= 2
    print()