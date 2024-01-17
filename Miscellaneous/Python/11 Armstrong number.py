n = int(input("Enter a number "))
string = str(n)
a=0
for i in range (len(str(n))):
    a+=int(string[i])**3
print("armstrong number ",a)
