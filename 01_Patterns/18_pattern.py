n = int(input("Enter n: "))

for i in range(n):
    for j in range(i+1):
        print(chr(65+n-i-1+j), end="")
    print()