class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        for i,n in enumerate(nums):
            if not i:
                self.prefix.append(n)
            else:
                x=self.prefix[i-1]+n
                self.prefix.append(x)
            
    def sumRange(self, left: int, right: int) -> int:
        lbound=0 if not left else self.prefix[left-1]
        slice_sum=self.prefix[right]-lbound
        return slice_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)