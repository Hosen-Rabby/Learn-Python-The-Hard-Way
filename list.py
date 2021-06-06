mylist = ["program", "prayer", "learning"]
print(mylist)
print("Lists are indxed and can have same value.")

# List length
print("To determine how many items a list has, use the len() function: ")
thislist = ["apple","mango","banann"]
print(len(thislist))

# list data types

print("List can be any of String, int and boolean data types:")

list_s = ["Rohim","Shorif", "Mib"]
list_i = [2, 5, 6,8, 0]
list_b = [True, False , True]

print(list_s)
print(list_i)
print(list_b)

print("It also can containn different data types")
list_c = ["ab", 55 , True]
print(list_c)

# type off

print("From Python's perspective, lists are defined as objects with the data type 'list': ")
print(type(list_i))

# The list() Constructor

print("It is also possible to use the list() constructor when creating a new list.")

list_cons = list(("bnb", "tr"))
print(list_cons)