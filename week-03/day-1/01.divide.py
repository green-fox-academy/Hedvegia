# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number = int(input("Enter a number: "))

def takes_a_number(a):
    try:
        result = 10 / number
    except ZeroDivisionError:
        print("Fail")
        
takes_a_number(number)

