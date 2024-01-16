#Write a Python program to print the Fibonacci sequence up to a given number of terms.
def fibonacci(n):
    num=[0,1]
    while len(num)<n:
        num.append(num[-1]+num[-2])
    return num
a=int(input("Enter the number of series to be added in the fibonacci series: "))
print(fibonacci(a))