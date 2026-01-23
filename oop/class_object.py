# Classes and Objects in Python
# Class: blueprint for objects
# Object: instance of a class

# Creating a class
class Student:
    # Constructor to initialize object
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

# Creating objects of the class
student1 = Student("Abhay", 20, "BCA")
student2 = Student("Bharti", 19, "BCA")

# Accessing methods
print("Student 1 details:")
student1.display()

print("\nStudent 2 details:")
student2.display()

# Accessing attributes directly
print("\nDirect access:")
print("Student 1 Name:", student1.name)

# Updating attributes
student1.age = 21
print("Updated Student 1 Age:", student1.age)
