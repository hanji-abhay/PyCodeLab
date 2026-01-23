# If-Else example in Python
marks = int(input("Enter your marks: "))  #taking input from user
if marks >= 90:  
    print("Grade A")  #if condition is true It prints Grade A on the output screen
elif marks >= 75:
    print("Grade B")  #if first condition is false the this contons is run and Grade B is displayed on output screen
elif marks >= 50:
    print("Grade C")  # if the both above conditions are false then Grade C is printed
else:
    print("Grade D") # if all the condtions are false then else condtion executes and prints Grade D on the output screen
