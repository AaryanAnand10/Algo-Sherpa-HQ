class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


# ##############################################################################################################

# Alter approach, usually faster

class Solution:
    def toLowerCase(self, s: str) -> str:
        answer = ""
        for i in s:
            if 'A' <= i <= 'Z':
                answer += chr(ord(i)+32)
            else:
                answer += i
        return answer
