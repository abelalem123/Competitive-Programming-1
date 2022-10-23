class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable=0
        for idx,i in enumerate(nums):
            if idx>reachable:
                return False
            reachable=max(reachable,idx+i)
            if reachable>=len(nums)-1:
                return True
        return reachable>=(len(nums)-1)