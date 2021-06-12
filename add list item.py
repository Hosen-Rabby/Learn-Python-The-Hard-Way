print("Add List Items")

print("\nThree methods- append(), insert() and extend()")
print("\nappend()- To add an item to the end of the list.")

thislist = ["Mobile", "Cha", "Mouse"]
thislist.append("Lego")
print(thislist)

print("\ninsert()- To insert a list item at a specified index.")
thislist.insert(2, "Tape")
print(thislist)

print("\nextend()- To append elements from another list to the current list.")
newlist = ["Table", "Laptop", "Ban"]
thislist.extend(newlist)
print(thislist)

newlist.extend(thislist)
print(newlist)

print("\nextend()- method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).")

thislist = ["Mobile", "Cha", "Mouse"]
thistuple = ("Book", "Online")
thislist.extend(thistuple)
print(thislist)


