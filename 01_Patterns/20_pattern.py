n = int(input("Enter n: "))
spaces = 2*n - 2

for i in range(1, 2*n):
    stars = i
    if i > n:
        stars = 2*n - i

    for j in range(stars):
        print("*", end="")

    for j in range(spaces):
        print(" ", end="")

    for j in range(stars):
        print("*", end="")

    print()

    if i < n: 
        spaces -= 2
    else:
        spaces += 2
