# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.
number = int(input('Type a number: '))
getnumber = number % 2
if  getnumber == 0:
    print('Even')
else:
    print('Odd')