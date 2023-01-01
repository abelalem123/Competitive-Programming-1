class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail=0,0
        self.capacity=k
        self.size=0
        self.q=[-1]*k
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if not self.isEmpty(): #if empty no need to modify head position
            self.head=(self.head-1)%self.capacity
        
        self.q[self.head]=value
        self.size+=1
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if not self.isEmpty():
            self.tail=(self.tail+1)%self.capacity

        self.q[self.tail]=value
        self.size+=1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head]=-1
        self.head=(self.head+1)%self.capacity
        self.size-=1
        if self.isEmpty():
            self.tail=self.head
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.tail]=-1
        self.tail=(self.tail-1)%self.capacity
        self.size-=1
        if self.isEmpty():
            self.tail=self.head
        return True
        
    def getFront(self) -> int:
        if not self.isEmpty():
            return self.q[self.head]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.q[self.tail]
        return -1

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size==self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()