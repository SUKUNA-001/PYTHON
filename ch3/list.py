fruits = ["apple", "banana", "cherry"]
#print(fruits)#print a list
#print(type(fruits))#check type of list
#print(len(fruits))#check length of list

#checking banana is part of alist
#if "banana" in fruits:
 #   print("banana is a part of list")

#if "kiwi" is not fruits:
#    print("kiwi is not a part of alist")

#print(fruits[1])  #ASCENDING ELEMENTS
#print(fruits[-3])
#print(fruits[1:3])#[apple,cherry]
#print(fruits[-2:-1])

#fruits.insert(2,"kiwi") #ADDING elements
#print(fruits)
#fruits.extend(more_fruits)
#print(fruits)

#fruits.remove("apple") #REMOVING ELEMENTS
#print(fruits)
#fruits.pop()
#print(fruits)

#CHANGING/UPDATING ITEMS IN LIST
#fruits[1] = "kiwi"
#print(fruits)

#fruits[1:2] = ["papaya"]

#print(fruits)
#fruits.sort()#ascending way
#print(fruits)

#fruits.reverse()
#print(fruits)

#COMPREHENSION LIST
#new_fruit = [fruits for fruits in fruits if "a" in fruits]
#print(new_fruit)

#new_fruit = fruits + new_fruit
#print(new_fruit)

#NESTED LIST
fruits.insert(2, ["kiwi", "mango"])
print(fruits)
print(fruits[2][0])