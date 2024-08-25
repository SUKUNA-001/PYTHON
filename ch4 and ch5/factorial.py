#function for calculating factorial  oa a number
def factorial(n):
    ans = 1
    if n == 0:
       ans = 1

    else:
        for i in range(1,n+1):
            ans *= i

        return ans 

n = int(input("enter number:"))

output = factorial(n)
print("the factoral is:", output)