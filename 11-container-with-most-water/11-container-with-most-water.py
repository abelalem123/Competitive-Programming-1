class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxim=0
        def water_cap(l,r):
            return min(height[l],height[r])*(r-l)
        left=0
        right=len(height)-1
        
        while left<right:    
            maxim=max(water_cap(left,right),maxim)
            if height[left]>height[right]:
                right-=1
            elif height[right]>=height[left]:
                left+=1
        return maxim