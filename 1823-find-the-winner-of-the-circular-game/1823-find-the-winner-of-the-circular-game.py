class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # arr=[i for i in range(1,n+1)]
        # pop_index=0
        # k-=1
        # while len(arr)>1:
        #     pop_index=(pop_index+k)%len(arr)
        #     arr.pop(pop_index)
        # return arr[0]
        if n==1:
            return 1
        else:
            return ((self.findTheWinner(n-1,k)+k-1)%n)+1