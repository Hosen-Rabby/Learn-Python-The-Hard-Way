print("Copy a List")
print("Two built-in methods to copy list- copy(), lists()")
thislist = ["chocolate","badam","jaam",55,67,89]
mylist = thislist.copy()
print("By copy() method - ",mylist)
nlist = list(thislist)
print("By list() method - ",nlist)