# Functions in Python
# Simple function to add two numbers
def add(a, b):                              #function created
    return a + b                            #return value added
num1 = int(input("Enter first number: "))   #taking input from the user outside of the function definition for frist number
num2 = int(input("Enter second number: "))  #taking input from the user outside of the function definition for second number
result = add(num1, num2)                    #function calling and storing output in new variable named result
print(f"The sum is: {result}")              #printing the output
