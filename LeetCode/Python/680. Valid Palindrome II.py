class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        for i in range(length//2):
            if s[i]!=s[length-i-1]:
                return True if (s[i+1:length-i]==s[i+1:length-1][::-1]) or (s[i:length-i-1]==s[i:length-i-1][::-1]) else False
        return True


