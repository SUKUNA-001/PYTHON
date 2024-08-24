n = int(input("enter n:"))

for i in range(1, n+1):
    #print space
    print(" " * (n-i), end="")
    #printing details
    for j in range(1, 2 * i):
        print(j , end="")
    print()