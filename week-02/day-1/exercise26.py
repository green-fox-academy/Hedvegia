# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
a = int(input('Type a number: '))
b = int(input('Type an other number: '))

if a > b:
    print('The second number should be bigger')

for i in range(a, b):
    print(i)

#Training

def b_is_bigger (a, b):
    for i in range(1, b-a):
        print(a + i)

def game ():
    a = int(input("enter a number: "))
    b = int(input("enter a second number: "))
    if a < b:
        b_is_bigger(a, b)
    else:
        print("b sholud be bigger than a!")
        game()
        
game()