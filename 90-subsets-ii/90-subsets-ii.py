class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def search(i,sub):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            search(i+1,sub)
            x=sub.pop()
            while i+1<len(nums) and x==nums[i+1]:
                i+=1
            search(i+1,sub)
        search(0,[])
        return res
                
        