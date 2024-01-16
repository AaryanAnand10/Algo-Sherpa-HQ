#Write a Python program that takes two numbers as input, performs addition, subtraction, multiplication, and division on them, and then prints the results
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition: ",addition(a,b))
print("Subtraction: ",subtraction(a,b))
print("Multiplication: ",multiplication(a,b))
print("Division: ",division(a,b))