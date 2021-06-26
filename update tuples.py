print("Change Tuple Values")
print("Tuples are unchangeable, but there is a workaround. Convert the tuple into a list to be able to change it:")

thistuple = ["Alu", "Kola", "Amm", "Ruti"]
y = list(thistuple)
y[2] = "Dim"
thistuple = tuple(y)
print(thistuple)
print("Add items")
z = list(thistuple)
z.append("Orange")
thistuple = tuple(z)
print(thistuple)


print("Add items")
z = list(thistuple)
z.remove("Orange")
thistuple = tuple(z)
print(thistuple)

print("Delete the tuple completely")
del thistuple # will raise an error
print(thistuple)

