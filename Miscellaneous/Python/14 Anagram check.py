class Anagram:
    def __init__(self):
        self.string1 = input("Give first input: ")
        self.string2 = input("Give second input: ")
        self.anagramcheck(self.string1,self.string2)
    def anagramcheck(self,a,b):
        if sorted(a) == sorted(b):
            print("Anagram")
        else:
            print("Not Anagram")
Anagram()