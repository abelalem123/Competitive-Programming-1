class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            p=nums.pop(0)
            prev=self.permute(nums)
            for i in prev:
                i.append(p)
            res.extend(prev)
            nums.append(p)
        return res
            