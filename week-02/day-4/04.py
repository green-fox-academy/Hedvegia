#Create a function that takes a number and a list of numbers as a parameter
#Returns the indeces of the numbers in the list where the first number is part of
#Returns an empty list if the number is not part any of the numbers in the list
#Example

#input: [1, 11, 34, 52, 61], 1
#output: [0, 1, 4]

#input 2 45365464
#output False

# a number_is_ in fügvényben ellenőrizzük, hogy a szám benne van e egy másik számban. 

def number_is_in(number, base_number):
    while 0 != base_number:
        if base_number % 10 == number:
            return True
        else:
            base_number /= 10
    return False

# ebben a függvényben a listám számaiban keresem a megadott számot.

def find_number(lst, number):
    output = []
    for i in range(len(lst)):
        if number_is_in(number, lst[i]) == True:
            output.append(i)
    return output

inp = [1, 11, 34, 52, 61]
number = 4       
print(find_number(inp, number))
