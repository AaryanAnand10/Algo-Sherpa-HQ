class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        countOfElements = Counter(nums) #Counter is a dictionary function which takes the input as an iterable object, and counts and creates a dictionary with elements as keys and their occurences as values
        for i in nums:
            if countOfElements[i]==1:
                return i
