# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
a = int(7)
number = int(input('type a number: '))
while a != number:
    if number > a:
        print('lower')
        number = int(input('type a number: '))
    elif number < a:
        print('higher')
        number = int(input('type a number: '))
    
    else:
        number = int(input('type a number: '))

print('Yes, the number was 7')
