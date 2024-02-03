class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        reverseString=""
        for i in s:
            if('z'>=i>='a' or 'Z'>=i>='A' or '9'>=i>='0'):
                reverseString+=i
        return reverseString==reverseString[::-1]
