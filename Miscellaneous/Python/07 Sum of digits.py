#Write a python program to find the sum of digits
def sumofdigits(n):
    return sum(int(digit) for digit in str(n))
n=int(input("Enter the digit: "))
print(sumofdigits(n))