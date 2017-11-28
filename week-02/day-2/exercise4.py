# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum (list):
    num = 0
    for i in range(1, list + 1):
        num += i
    return num

print(sum(4))