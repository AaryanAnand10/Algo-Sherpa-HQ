def factorial(n):
    if n==0 or n==1:
        return 1
    if n > 1:
        return n * factorial(n-1)
a=int(input("Enter the number whose factorial is needed: "))
print(factorial(a))