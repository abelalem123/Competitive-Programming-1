#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        idx = i
        for p in range(i+1,len(arr)):
            if arr[p] < arr[idx]:
                idx=p
        return idx
    
    def selectionSort(self, arr,n):
        #code here
        for current in range(n):
            min_idx=self.select(arr,current)
            arr[current],arr[min_idx]=arr[min_idx],arr[current]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
