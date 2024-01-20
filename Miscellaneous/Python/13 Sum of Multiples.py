#Write a Python function to find the sum of all multiples of 3 or 5 below a given number n.
class multiples:
    def __init__(self):
        self.n=int(input("Enter a number: "))
        print("Sum of multiples of 3 and 5 below ",self.n, 'is:', self.multiple())
    def multiple(self):
        return sum(i for i in range(self.n) if i%3==0 or i%5==0)
multiples()