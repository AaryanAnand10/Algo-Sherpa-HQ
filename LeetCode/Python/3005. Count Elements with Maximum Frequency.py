class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count ={}
        max=0
        for i in nums:
            if max < nums.count(i):
                max=nums.count(i)
            count[i]=nums.count(i)
        res = 0
        print(count)
        for i in count.values():
            if i == max:
                res+=max
        return res
