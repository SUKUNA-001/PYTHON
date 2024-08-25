#pass by value
def addone(x):
    x = x+2
    print("inside the function:", x)

x=5
addone(x)
print("outside the function:", x)

#pass by reference
def modifylist(lst):
    lst.append(4)
    print("inside function:", lst)

lst = [1,2,3]
modifylist(lst)
print("outside functon:", lst)