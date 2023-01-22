class MyCalendar:

    def __init__(self):
        self.pq=[]

    def book(self, start: int, end: int) -> bool:
        if not self.pq:
            self.pq.append(start)
            self.pq.append(end)
            return True
        
        index = bisect_right(self.pq,start)
        if index % 2 !=0 or (index < len(self.pq) and end > self.pq[index]):
            return False
        
        self.pq.insert(index,start)
        self.pq.insert(index+1,end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)