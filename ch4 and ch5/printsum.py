def sum_1_to_n(n):

    #base case
    if n == 1:
        return 1
    
    #recursive case
    ans = n + sum_1_to_n(n-1)
    return ans
n = int(input("enter no:"))
print(sum_1_to_n(n))