#write a function that print hello world

#def printhello():
#body of a function
#    print("HELLO WORLD!!")

# printhello()
    
#function which takes2 number as an input and return their sum
def add(n1,n2):
    sum = n1 +n2
    return sum
n1:2
n1:3
#x=2
#y=3
#postional argument
#print("he sum is",add(x,y))

#keyword argument (need argument)
#print("the sum is",add(n2=2,n1=3))

#default argument
#print("the sum is", add(3))# if n2=0

#arbitary
def addallnumber(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
#output = addallnumber(1,2,3,4,5)
#print("the sum is", output)

def studentinfo(**kwargs):
    for x,y in kwargs.item():
        print(x,"is",y)
studentinfo(name="urvi", age=22, city="delhi")
studentinfo(name="ria", age=20, city="banglore")