num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))

operator = input("enter the operator")

match operator:
    case"+":
        print("sum is", num1 + num2)
    case"-":
        print("difference is", num1 - num2) 
    case"*":
        print("product is", num1 * num2)
    case"/":
        print("quotient is", num1 / num2)
    
    
    case"%":
        print("remainder is ", num1 % num2)
    case"//":
        print("floor division", num1 // num2)
    case"**":
        print("exponentational is", num1 ** num2)
    
    