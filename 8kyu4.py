def find_average(numbers):
    # your code here
    length = len(numbers)
    if length == 0:
        return 0
    total = 0
    for i in numbers:
        total = total+i
        i=i+1
    result = total/length
    print(result)