class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result =[]
        for i in range(len(arr),1,-1):
            max_idx=self.max_idx(arr,i)
            self.flip(arr,max_idx)
            self.flip(arr,i-1)
            result.append(max_idx+1)
            result.append(i)
        return result
    def max_idx(self,arr,upto):
        cur_max = 0
        for i in range(1,upto):
            if arr[i] > arr[cur_max]:
                cur_max = i
        return cur_max
        
    def flip(self,arr,idx):
        left=0
        right = idx
        while left <right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right -=1