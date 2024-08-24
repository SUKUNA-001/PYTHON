#arthematic operator
print("sum:", 7 + 2)
print("subtract:", 7 + 2)
print("product:", 7 + 2)
print("divisio:", 7 / 2)
print("floor division:", 7 // 2)
print("remainder:", 7 % 2)
print("exponentaition:", 7 ** 2)      


# assignment operator
n1 = 5
n2 = n1
print(n1,n2)
n2 += n1
print(n1, n2)

#comparision operator
n1 = 4
n2 = 3
print(n1>n2)

n1 = 4
n2 = 8
print(n1>n2)

#logical operator
exp1 = 2 > 1
exp2 = 5 < 4
print(" exp1 and exp2:", exp1 and exp2)
print(" exp1 or exp2:", exp1 or exp2)
print(" not exp1:", not(exp1))

#identity op[erator]
x = 3
y = 3
print("if x is y:", x is y)
print("if x is not y:", x is not y)

#membership operator
sports = ["cricket", "football", "pubg"]
print("if cricket is present in sports:", "cricket" in sports)
print("if pubg is not present in sports:", "pubg" not in sports)

#bitwise operator 
a = 5
b = 3
print("a and b;", a & b)
print("a or b:", a | b)
print("a xor b:", a ^ b)