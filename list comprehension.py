print("List Comprehension\n")
print("a shorter syntax when you want to create a new list based on the values of an existing list.")

fruits = ["amm", "Kathal", "Lichu", "amraa", "angur","Jaam"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print("New list-",newlist)

print("With list comprehension you can do all that with only one line of code:")

newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits2 = ["apple","orange"]
new2 = [x for x in fruits2 if x != "apple"]
print(new2)

print("\nWith no if statement:")
new3 = [x for x in fruits2]
print(new3)
new4 = [x for x in range(11)]
print(new4)
new5 = [x for x in range(11) if x<5]
print(new5)
new6 = [x for x in range(20) if x%2 == 0]
print(new6)

print("\nSet the values in the new list to upper case.")
new7 = [x.upper() for x in fruits]

new8 = ["hello" for x in fruits]
print(new8)

fruits3 = ["banana", "kola", "tui"]
new9 = [x if x!= "banana" else "orange" for x in fruits3]
print(new9)

