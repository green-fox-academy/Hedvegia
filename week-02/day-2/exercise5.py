# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio (n):
    if n == 0:
        return 1
    else:
        return n * factorio(n-1)

print(factorio(5))

number = int(input("Enter a number: "))

def factorio (n):
    if n == 1:
        print("Megtaláltam 1 faktoriálisát")
        return 1 
    else:
        print("keresem " + str(n) + " factoriálisát")
        return n*factorio(n-1)

print(factorio(number))