class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        waterlevel=0
        ml=[None for i in range(len(height))]
        mr=[None for i in range(len(height))]
        #find max left for each element
        for i in range(len(height)):
            if i==0:
                ml[0]=height[0]
                continue
            if height[i]>ml[i-1]:
                ml[i]=height[i]
            else:
                ml[i]=ml[i-1]
        #find max right for each element
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                mr[i]=height[-1]
                continue
            if height[i]>mr[i+1]:
                mr[i]=height[i]
            else:
                mr[i]=mr[i+1]
        # find water trapped by each block
        for idx,i in enumerate(height):
                left=ml[idx]
                right=mr[idx]
                waterlevel=min(left,right)
                h=waterlevel-i
                if h>0:
                    res+=h
        return res