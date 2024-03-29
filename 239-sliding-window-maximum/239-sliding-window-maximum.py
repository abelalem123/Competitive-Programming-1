class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        sub_max = [] #final result array
        #win = {}
        #max_num=-math.inf
        #first window
        for r in range(k):
            num=nums[r]
            max_heap.append(-num)
        heapq.heapify(max_heap)
        
        sub_max.append(-1*max_heap[0])
        left = 0 #left pointer
        to_be_removed ={}

        for right in range(k,len(nums)):
            num_right=nums[right]
            num_left=nums[left]
            
            to_be_removed[num_left]=1 + to_be_removed.get(num_left,0)
            left+=1
            heapq.heappush(max_heap,-num_right)
            while max_heap and -1*max_heap[0] in to_be_removed:
                
                temp=-1*heapq.heappop(max_heap)
                to_be_removed[temp]-=1
                if to_be_removed[temp] == 0:
                    del to_be_removed[temp]
            sub_max.append(-1*max_heap[0])
        return sub_max
            