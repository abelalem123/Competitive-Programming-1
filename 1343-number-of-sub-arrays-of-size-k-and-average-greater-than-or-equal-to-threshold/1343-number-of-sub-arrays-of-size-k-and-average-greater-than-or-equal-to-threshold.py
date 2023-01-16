class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        2 2 2 3 4 5 6
        
        """
        soln=0
        
        #first window 0,k
        total=0
        for i in range(k):
            total+=arr[i]
        if total/k>=threshold:
            soln+=1
        
        #remaining window k,len(arr)
        left=0
        for right in range(k,len(arr)):
            total-=arr[left]
            left+=1
            total+=arr[right]
            if total/k>=threshold:
                soln+=1
        
        
        return soln