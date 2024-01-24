class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in set(t):
            if t.count(i) != s.count(i):
                return i
                break
