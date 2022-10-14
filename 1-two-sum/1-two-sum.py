class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new=sorted(nums)
        l,r=0,len(nums)-1
        while l<r:
            if new[l]+new[r]==target:
                l=new[l]
                r=new[r]
                break
            elif new[l]+new[r]>target:
                r-=1
            else:
                l+=1
        left=nums.index(l)
        nums[left]=math.inf
        right=nums.index(r)
        return [left,right]
        