class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda i:i[1])
        count=0
        min_heap = []
        heapq.heapify(min_heap)
        for p,f,t in trips:
            count += p
            while min_heap and min_heap[0][0] <= f:
                count -= min_heap[0][1]
                heapq.heappop(min_heap)
            if count > capacity:
                return False
            heapq.heappush(min_heap,(t,p))
        return count <= capacity
        
        