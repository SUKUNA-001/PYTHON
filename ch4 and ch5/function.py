n = int(input("enter the number:"))
#sum = 0
#for i in range(1,n+1):
 #   sum += i
  #  print("sum of all num till n",sum) 

#writing a function for calculating sum from 1to n
def sumoneton(n):
    sum=0
    for i in range(1,n+1):
        sum += i
    return sum
#call function
output= sumoneton(n)
print("sum of all number till n",output )
