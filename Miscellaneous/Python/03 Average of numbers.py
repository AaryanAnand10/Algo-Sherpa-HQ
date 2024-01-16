#Write a Python program to calculate the average of a given list of numbers.
def average(number):
    return sum(number)/len(number)
numbers=list(map(int,input("Enter the numbers to find the average: ").split()))
print(average(numbers))