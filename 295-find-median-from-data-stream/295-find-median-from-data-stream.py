class MedianFinder:

    def __init__(self):
        self.maxh=[]# a max queue that holds the lesser half
        self.minh=[]# a min queue that holds the bigger half
    def addNum(self, num: int) -> None:
        # implement max heap by inverting the value of num
        heapq.heappush(self.maxh, -1*num)
        # validate max at maxh < min at minh
        if self.maxh and self.minh and -1*self.maxh[0] > self.minh[0]:
            value=-1 * heapq.heappop(self.maxh)
            heapq.heappush(self.minh,value)
        # validate their size is approximately equal
        if len(self.maxh) > len(self.minh)+1:
            value=-1 * heapq.heappop(self.maxh)
            heapq.heappush(self.minh,value)
        if len(self.minh) > len(self.maxh)+1:
            value=heapq.heappop(self.minh)
            heapq.heappush(self.maxh,-1*value)
    def findMedian(self):
        if len(self.minh)> len(self.maxh):
            return self.minh[0]
        if len(self.maxh)> len(self.minh):
            return -1*self.maxh[0]
        else:
            return (self.minh[0]+(-1*self.maxh[0]))/2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()