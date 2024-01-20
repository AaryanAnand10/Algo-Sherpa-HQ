#Write a function to determine if a given string is a palindrome
class Pallindrome:
    def __init__(self):
        self.string=input("Give your input: ")
        string = self.string.lower().replace(" ","")
        string_r = string[::-1]
        self.maincheck(string,string_r)
    def maincheck(self,string, string_r):
        if string_r == string:
            print("Pallindrome")
        else:
            print("Not Pallindrome")
Pallindrome()