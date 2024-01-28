class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            NoD=len(str(i))
            res = list(map(int,str(i)))
            if NoD%2==0 and sum(res[0:NoD//2])==sum(res[NoD//2:NoD]):
                count+=1
                print(res)
        return count
