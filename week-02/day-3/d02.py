students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def more_than_4 (clss):
    for i in students:
        if i['candies'] < 4:
            print(i['name'])
        
more_than_4(students)

def average (stud):
    av = 0
    for i in students:
        av += i['candies']
    return av / 4
    
print(average(students))