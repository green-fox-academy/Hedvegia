# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

a = (str(input('operation: ')), int(input('operand: ')), int(input('operand: ')))

if a[0] == "+":
    print(a[1] + a[2])
elif a[0] == "-":
    print(a[1] - a[2])
elif a[0] == "*":
    print(a[1] * a[2])
elif a[0] == "/":
    print(a[1] / a[2])

#training

def calculator ():  
    a = input("Type your expression: ") 
    if a[0] == "+":
        print(int(a[2]) + int(a[4]))
    elif a[0] == "-":
        print(int(a[2]) - int(a[4]))
    elif a[0] == "*":
        print(int(a[2]) * int(a[4]))
    else:
        print(int(a[2]) / int(a[4]))

calculator()