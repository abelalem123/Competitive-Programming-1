class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i=len(nums)
        res=nums[:]
        while(i>1):
            res=self.fill(res)
            i=i/2
        return res[0]
    def fill(self,root):
        arr=[]
        x=int(len(root)/2)
        flip=True
        for i in range(x):
            if flip:#even
                arr.append(min(root[2*i],root[2*i+1]))
            else:
                arr.append(max(root[2*i],root[2*i+1]))
            flip=not(flip)
        return arr
            