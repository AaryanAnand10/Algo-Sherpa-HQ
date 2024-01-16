def square(n):
    for i in range(n):
        if i*i==n:
            return "perfect square"
        else:
            return "not perfect square"
a = int(input("Enter the number "))
print(square(a))