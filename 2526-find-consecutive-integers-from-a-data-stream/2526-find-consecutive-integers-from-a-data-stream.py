class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.size=0
        self.holder=value

    def consec(self, num: int) -> bool:
        if self.holder!=num:
            #self.holder=num
            self.size=0
            return False
        else:
            self.size+=1
            return self.k<=self.size
        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)