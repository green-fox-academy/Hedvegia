# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum (list):
    num = 0
    for i in range(1, list + 1):
        num += i
    return num

print(sum(4))

#training

def sum_new(b):
    osszeg = 0
    mehet = True
    while(mehet):
        a = int(input("Adjon meg hozzáadandó számot: "))
        if a != b:
          osszeg += a
        else:
          mehet = False
    return osszeg

inp = int(input("Adjon meg paramétert: "))
print(sum_new(inp))