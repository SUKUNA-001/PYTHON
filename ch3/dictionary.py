phone = {
    "john" : 564986,
    "ria" : 646541,
    "joy" : 3548641
}
print(phone) 

#checking type of dict
print(type(phone))

#check length of dict
print(len(phone))

#access item of dict
print(phone["john"])

#acess items of dict
print(phone.get("john"))
print(phone.keys())

#update value in dict
print["john"] : 514865
print(phone)

#add elements in dict
phone["kia"] = 168532
print(phone)

#add
more_phones = {
    "roy" : 456355
}
phone.update(more_phones)
print(phone)

#remove elements in dict
phone.pop("john")
print(phone)

phone.popitem() #this will remove the last added item
print(phone)
phone.clear()
print(phone)
#printing values of adict
for x,y in phone.items():
    print(x,y)

#nested dictionary
    phone = {
        "area1" : {
            "x": 0,
            "y": 1,
            "z": 2
        },
        "area2": {
            "a": 3,
            "b": 4,
            "c": 5
        }
    }    
    print(phone["area1"]["y"])    