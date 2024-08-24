input_string = input("enter string:")
n = int(input("enter the n:"))

#creating dict for mirror operation
alphabet = ("abcdefghijklmnopqrstuvwxyz")
reverse_alphabet = alphabet[::-1]
dict1 = dict(zip(alphabet, reverse_alphabet))

#finding the part of astring on which we will do mirror
perfix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1(suffix(i))
res = perfix + mirror
print("the result is:", res)