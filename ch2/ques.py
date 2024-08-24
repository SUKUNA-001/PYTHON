number1 = int(input(" enter the number1:"))
number2 = int(input(" enter the number2:"))
number3 = int(input(" enter the number3:"))

#if number1 is greatest
if number1 > number2 and number1 > number3:
    print(number1, "is the greatest number")
#isf number2 isgreatest
elif number2 > number1 and number2 > number3:
    print(number2, "the greatest number")
#if number3 is greatest
else:
    print(number3, "is the greatest number")
