class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        min_sum = 0
        stack = []

        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]]>=arr[i]): # we want a strictly increasing stack
                mid = stack.pop()
                if not stack:
                    lb = -1
                else:
                    lb = stack[-1] #left boundary or prev smaller index
                rb = i #right boundary or next smaller number index
                
                count = (mid - lb) * (rb - mid) #number of sub arrays before and after including mid
                
                min_sum += (arr[mid] * count)
            stack.append(i)
        return min_sum % 1_000_000_007