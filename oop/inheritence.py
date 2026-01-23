# Inheritance in Python
# A class can inherit properties and methods from another class

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child class inherits from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)  # Call parent constructor
        self.course = course

    def display_student(self):
        self.display_person()  # Using parent method
        print(f"Course: {self.course}")

# Creating object of child class
student1 = Student("Abhay", 20, "BCA")
student1.display_student()

# Another example: Adding methods
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}")

teacher1 = Teacher("Mr. Sharma", 35, "Math")
teacher1.display_teacher()
