print("Sort List Alphanumerically")
print("List objects have a sort() method that will sort the list alphanumerically, ascending, by default")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [9,5,2,1,57,0]
numlist.sort()
print(numlist)

print("Sort Descending")

print("To sort descending, use the keyword argument reverse = True")
thislist.sort(reverse = True)
print(thislist)
numlist.sort(reverse = True)
print(numlist)

print("Customize Sort Function")
print("can also customize function by using the keyword argument key = function")

def myfunc(n):
    return abs(n - 10)

funclist = [2,11,4,66,77,20,41,10]
funclist.sort(key = myfunc)
print("Sort the list based on how close the number is to 50 -",funclist)
print("\nCase Insensitive Sort\n")
print("By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters-")

thisfruitlist = ["banana", "Orange", "Kiwi", "cherry"]
thisfruitlist.sort()
print(thisfruitlist)

print("We can use.")

thisfruitlist.sort(key = str.lower)
print(thisfruitlist)

print("Reverse Order")
print("The reverse() method reverses the current sorting order of the elements.\n")
thisfruitlist.reverse()
print(thisfruitlist)
