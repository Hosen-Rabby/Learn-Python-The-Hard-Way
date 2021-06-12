print("Loop Through a List\n")
print("You can loop through the list items by using a for loop.\n")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("\nLoop Through the Index Numbers.")
print("range() and len() functions to create a suitable iterable.")

for i in range(len(thislist)):
    print(i)

print("Using a While Loop\n")
print("You can loop through the list items by using a while loop.\n")

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


print("\nLooping Using List Comprehension\n")
print("List Comprehension offers the shortest syntax for looping through lists:\n")
print("A short hand for loop that will print all items in a list:")


[print(x) for x in thislist] 

