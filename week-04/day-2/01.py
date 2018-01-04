class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("My name is ", self.name, ", a ", self.age, " year old ", self.gender)

    def get_goal(self):
        print("My goal is: Live for the moment!")


class Student(Person):
    def __init__(self, name, age, gender, previous_organization, skipped_days=0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
    
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

    def introduce(self):
        print("Hi, I'm ", self.name, ", a ", self.age, " year old ", self.gender, " from ", self.previous_organization, " who skipped ", self.skipped_days, " days from the course already")


class Mentor(Person):
    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.level = level

    def introduce(self):
        print("Hi, I'm", self.name, " a ", self.age, " year old ", self.gender, self.level, "mentor.")

    def get_goal(self):
        print("Educate brilliant junior software developers.")
    

class Sponsor(Person):
    def __init__(self, name, age, gender, company, hired_students=0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students
    
    def hire(self):
        self.hired_students += 1
    
    def introduce(self):
        print("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender, " who represents ", self.company, " and hired ", self.hired_students, " students soar.")
    
    def get_goal(self):
        print("Hire brilliant junior software developers.")


class PallidaClass(object):
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, student):
        self.students.append(student)

    def add_mentor(self, mentor):
        self.mentors.append(mentor)

    def info(self):
        print( "Pallida ", self.class_name, " class has ", len(self.students), " students and ", len(self.mentors), " mentors.")


people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person("Jane Doe", 30, "female")
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student("Jane Doe", 30, "female", "The School of Life", 0)
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor("Jane Doe", 30, "female", "intermediate", )
people.append(mentor)
sponsor = Sponsor("Jane Doe", 30, "female", "Google", 0)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = PallidaClass('BADA55')
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)
badass.info()