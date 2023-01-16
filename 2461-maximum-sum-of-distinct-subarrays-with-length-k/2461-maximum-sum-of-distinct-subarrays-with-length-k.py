class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_dict = {}
        length=0
        ans=0
        l=0
        sub_total=0
        for r,n in enumerate(nums):
            num_dict[n]=num_dict.get(n,0) + 1
            length+=1
            sub_total +=n
            
            while length>k or length > len(num_dict):
                num_dict[nums[l]]-=1
                if num_dict[nums[l]]==0:
                    del num_dict[nums[l]]
                length-=1
                sub_total -= nums[l]
                l+=1
            
            if length==k:
                ans=max(ans,sub_total)
        return ans
                