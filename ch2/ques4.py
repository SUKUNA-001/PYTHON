n1 = int(input("enter number1:"))
n2 = int(input("enter number2:"))
n3 = int(input("enter number3:"))
# if n1 is greatest
#if n1 > n2 and n1 > n3:
#    print(" A grade")
#elif n2 > n3 and n2 > n3:
#   print("B grade")
#else: 
#   print("C grade")

# using nested if else statement
  # either n1 or n3 is greatest
if n1 > n2:
    if n1 > n3:
     print("n1 is the greatest")
else:
   print("n3 is the greatest")
          