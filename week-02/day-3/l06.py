# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def contain (ls):
    a = 0
    for n, i in enumerate(ls):
        if list_of_numbers[n] == 4 and list_of_numbers[n] == 8 and list_of_numbers[n] == 12 and list_of_numbers[n] == 16:
            a += 1
        else:
            a += 0
    if a == 0:
        return 'True'
    else:
        return 'False'
    
print(contain(list_of_numbers))
            