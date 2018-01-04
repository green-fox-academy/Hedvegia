students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def name_candies (clss):
    for i in students:
        print(i['name'], i['age'])

name_candies(students)

def lass_than_5 (candy):
    ages = 0
    for i in students:
        if i['candies'] < 5:
            ages += i['age']
        elif i['candies'] > 5:
            ages += 0
    return(ages)

print(lass_than_5(students))

#Practise

def owned_candies(students):
    for i in students:
        print(i['name'], i['candies'])
owned_candies(students)

def owned_candies_sum(students):
    summa = []
    for i in students:
       summa.append(i['candies'])  
    print(sum(summa))
owned_candies_sum(students)

def ages(students):
    a = 0
    for i in students:
        if i['candies'] >= 5:
            a += i['age']
    print(a)
ages(students)