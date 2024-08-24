#creating a set
names = {"sia", "mia", "tia"}

#print sets
print(names)

#check length of set
print(len(names))

#check data type of set
print(type(names))

#ascending items of sets
for x in names:
    print(x)

#check if an item exist in a set
if "sia" in names:
    print("sia is in set")

#add element in set
names.add("ria")
print(names)    

#add another sequence in set
names_list = ["ria","kia"]
names.update(names_list)
print(names)

#removing elements for sets
names.remove("ria")
names.discard("ria")#this function will not throw an error if value is not in set

print(names)

#join 2sets
s1 = {"a","b","c"}
s2 = {"d", "e", "a"}
#print(s1, s2)

#s3 = s1.union(s2) 
#print(s3)

#keep onlt duplicates while joining
#s1.intersection_update(s2)
#print(s1)

#how can we join to sets
s1.symmetric_difference_update(s2)
print(s1)