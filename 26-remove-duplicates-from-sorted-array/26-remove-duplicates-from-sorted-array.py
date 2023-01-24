class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        
        [0,1,2,3,1,4,2,3,3,4]
    l       r
        prev=4
        """
        prev = -101
        left = 0
        for r,n in enumerate(nums):
            if prev!=n:
                nums[left]=n
                left+=1
                prev=n
        return left
                