class vowelconsonants:
    def __init__(self):
        self.string = input("Enter the string : ")
        self.vowelcount = self.vowelcheck(self.string)
        self.consonant = len(self.string)-self.vowelcount
        print("Vowels = ",self.vowelcount)
        print("Consonants = ",self.consonant)

    def vowelcheck(self,a):
        vowels = "aeiouAEIOU"
        return sum(1 for char in a if char in vowels)
vowelconsonants()
