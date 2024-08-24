#creating a tuple
color = ("red", "blue", "green")

#creating atuple with one item
fruit = ("apple",) #fruit = tuple(("apple"))

#type of tuple
print(type(fruit))

#checking length of tuple
print(len(color))

#accending item in tuple
print(color[0]) #positive indexing
print(color[-1]) #negative
print(color[1:3]) #range indexing
print(color[-2:])

#check if item exist in tuple 
if "green" in color:
    print("green is apart of color")

   #traverse the tuple 
for i in color:
    print(i)

#concatenate 2 tuple
more_color = ("yellow","brown")
color = color + more_color
print(color)

#unpacking atuple
color1, color2, color3 = color
print(color1, color2, color3)
