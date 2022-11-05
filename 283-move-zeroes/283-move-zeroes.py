class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res=[]
        # zeros=0
        # for i in nums:
        #     if i:
        #         res.append(i)
        #     else:
        #         zeros+=1
        # for i in range(zeros):
        #     res.append(0)
        # nums[:]=res[:]
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l]=nums[r]
                l+=1
        for i in range(l,len(nums)):
            nums[i]=0
                