num = int(input("enter the list:"))

list = []
for i in range(num):
    num = int(input())
    list.append(num)

idx1 = int(input("enter index1:"))    
idx2 = int(input("enter index2:"))
print(list)

#SWAPPING LSIT
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)