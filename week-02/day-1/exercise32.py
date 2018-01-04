# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

a = int(input('Type a number: '))
b = a - 2
print ('%' * a)
for i in range(b):
   print ('%' +  ' ' * i + '%' + (a - i -2) * ' ' + '%')
print ('%' * a)


#training

a = int(input("enter an even number: "))
print('%'*a)
for i in range(a-2):
    print('%' + ' '*(i) + '%' + ' '*(a-3-i) + '%')
print('%'*a)