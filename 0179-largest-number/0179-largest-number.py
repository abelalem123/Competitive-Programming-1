class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        comp=lambda x, y: (x+y) > (y+x)
        largest_num = sorted((str(i) for i in nums),key=LargerNumKey)
        return '0' if largest_num[0] == '0' else ''.join(largest_num) 