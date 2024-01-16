def maxandmin(a):
    return max(a), min(a)
a=list(map(int,input("Enter the elements: ").split()))
maxnum, minnum = maxandmin(a)
print("Maximum: ",maxnum)
print("Minimum: ",minnum)