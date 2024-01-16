def largest_number(a, b):
    max_num = 0
    for i in range(b):
        if a[i] > max_num:
            max_num = a[i]
    return max_num

a = []
b = int(input("Enter the number of elements: "))

for i in range(b):
    num = int(input("Enter number: "))
    a.append(num)

result = largest_number(a, b)
print("The largest number is:", result)
