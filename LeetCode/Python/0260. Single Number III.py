class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        else:
            let=[]
            for i in nums:
                if i in let:
                    let.remove(i)
                else:
                    let.append(i)
        return let
