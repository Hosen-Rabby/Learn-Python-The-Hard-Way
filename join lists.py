print("Join Two Lists")
print("There are several ways to join, or concatenate, two or more lists in Python - '+', looping, extend()")
list1 = ["a","b","f"]
list2 = [1,2,5]
list3 = list1+list2
print(list3)


for x in list1: 
    list2.append(x)
print(list2)

list3.extend(list2)
print(list3)