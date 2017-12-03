# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]
a = 0
for n,i in enumerate(numbers):
    if numbers[n] == 7:
        a += 1
    else:
        a += 0

if a == 1:
    print('Hoorray')
else:
    print('Nooooo')

#Training

numbers = [1, 2, 3, 4, 5, 6, 8, 7, 7, 7]

num = 0

for i in numbers:
    if i == 7:
        num += 1  

if num >= 1:
    print("Hoorray")
else:
    print("Noooooo")