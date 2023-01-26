class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for s,e in zip(l,r):
            arr=sorted(nums[s:e+1])
            dist=arr[1] - arr[0]
            for i in range(1,len(arr)):
                temp=arr[i]-arr[i-1]
                flag=True
                if temp!=dist:
                    flag=False
                    break   
            result.append(flag)

        return result