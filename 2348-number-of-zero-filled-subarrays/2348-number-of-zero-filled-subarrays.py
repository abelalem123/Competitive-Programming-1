class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        result=0
        for i in nums:
            if not i:
                count+=1
            else:
                count =0
            result+=count
        return result