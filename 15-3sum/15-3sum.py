class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new=sorted(nums)
        res=[]
        for i,v in enumerate(new):
            if i>0 and v==new[i-1]:
                continue
            target=-1*v
            temp=self.twosum(new,target,i+1,len(new)-1)
            if len(temp):
                res.extend(temp)


        return res
    
    def twosum(self,arr,target,l,r):
        res=[]
        while l<r:
            if arr[l]+arr[r]==target:
                res.append([arr[l],arr[r],-1*target])
                l+=1
                while arr[l]==arr[l-1] and l<r: 
                    l+=1
            elif arr[l]+arr[r]>target:
                r-=1
            else:
                l+=1
        return res