# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    * space: 3 db, csillag: 1 db number: 7 
#   *** space: 2 db, csillag: 3 db number: 7
#  ***** space: 1 db, csillag: 5 db number: 7
# ******* space: 0 db, csillag: 7 db number: 7 <----- eddig
#  ***** space: 1 db,  csillag: 5 db number: 7
#   *** space: 2 db, csillag: 3 db number: 7
#    * space: 3 db, csillag: 1 db number: 7
#
# The diamond should have as many lines as the number was



number = int(input("Enter an odd number: "))
for i in range(number // 2 + 1): 
  print(" "*(number // 2 - i ), "*"*(i*2+1)) 
for i in range(number, 0, -1):
  print(" "*(number - i + 1), "*"*(((number // 2) - (number - i + 1))*2 + 1))
  
  
  
# _ _ _ *    --->number // 2 sp -0 = 3 ||  i = 0 || 2*i+1 = 1 csillag
# _ _ * * *  --->number // 2 sp -1 = 2 || i = 1 || 2*i+1 = 3 csillag 
# _ * * * * *
# * * * * * * *  ---------------------------------------------
# [_ * *] * * * ----->   sp: number - i + 1 = 1 || i = 7 || ((number // 2) - (number - i + 1))*2 + 1
# [_ _ *] * *    ---->   sp: number - i + 1 = 2 || i = 6 || (3 - 2)*2 + 1 = 3
# [_ _ _] *     																	 i = 5 || (3 - 3)*2 + 1 = 1 