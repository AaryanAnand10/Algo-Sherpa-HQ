class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s=list(map(int,s))
        while len(s)>k:
            temp=[]
            #run looping from 0 to len with steps to k
            for i in range(0,len(s),k):
                digitsum=sum(s[i:i+k])
                for digit in str(digitsum):
                    temp.append(int(digit))
            s=temp
        return "".join(map(str,s))
