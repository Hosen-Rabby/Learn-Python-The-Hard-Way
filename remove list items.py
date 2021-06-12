print("Python - Remove List Items.\n\n")
print("Four methods - remove(), pop(), del(), clear()\n")

print("remove()- method removes the specified item.")

thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)
thisnumlist = [2,5,6,7,8]
thisnumlist.remove(5)
print(thisnumlist)

print("\npop()-removes the specified index.")
thislist.pop(1)
print(thislist)
thisnumlist.pop(2)
print(thisnumlist)


print("\nIf you do not specify the index, the pop() method removes the last item.")
thisnumlist.pop()
print(thisnumlist)

print("\ndel- its a keyword and removes the specified index.")
thisnumlist = [1,4,6,7,8,99]
del thisnumlist[4]
print(thisnumlist)


print("\nThe del keyword can also delete the list completely.")
del thislist
# print(thislist)

print("\nclear() - method empties the list.\n")
print("The list still remains, but it has no content.")
thisnumlist.clear()
print(thisnumlist)
