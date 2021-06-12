print("Python - Access List Items")

print("The first item has index 0.")
thislist = ["Banana", "Apple", "Watermelon","Guyava","Carrot","Grape"]
print(thislist[1])

print("===Negative Indexing===")

print("Negative indexing means start from the end.")

print(thislist[-1])

print("===Range of Indexes.===")
print(thislist[2:5])
print(thislist[2:])
print(thislist[:5])

print("===Range of Negative Indexes===")
print(thislist[-4:-1])

print("===Check if Item Exists===")

if 'Apple' in thislist:
    print("yes")
