# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was


number = int(input("Enter a number: "))
for i in range(number):
  print(" "*(number-i-1), "*"*(i*2+1)) 
  
#space = _
#number = 4
# _ _ _ * 
# _ _ * * * 
# _ * * * * * 
# * * * * * * * 