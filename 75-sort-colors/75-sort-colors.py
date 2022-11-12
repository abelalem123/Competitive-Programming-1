class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for i in nums:
            count[i]+=1
        holder=0
        for i in range(3):
            count[i]=holder+count[i]
            holder=count[i]
        holder=0
        for i in range(3):
            temp=count[i]
            count[i]=holder
            holder=temp
        output=[0]*len(nums)
        for i in nums:
            output[count[i]]=i
            count[i]+=1
        nums[:]=output[:]