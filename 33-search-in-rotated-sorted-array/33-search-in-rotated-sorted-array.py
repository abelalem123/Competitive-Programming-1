class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        first=nums[0]
        while(l<=r):
            mid= l + (r-l)//2
            value=nums[mid]
            if value==target:
                return mid
            curr_arr=value>=first
            target_arr=target>=first
            if curr_arr==target_arr:
                if value>target:
                    r=mid-1
                elif value<target:
                    l=mid+1
            else:
                print('eh')
                if curr_arr:
                    l=mid+1
                else:
                    r=mid-1
        return -1                