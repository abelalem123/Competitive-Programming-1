class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        k=len(nums)-k
        def partition(left,right,pivot):
            pivotvalue=nums[pivot]
            nums[pivot],nums[right]=nums[right],nums[pivot] #move pivot to end
            store=left
            for i in range(left,right):
                if nums[i]<pivotvalue:
                    nums[store],nums[i]=nums[i],nums[store]
                    store+=1
            nums[store],nums[right]=nums[right],nums[store]
            return store

        while l<=r:
            if l==r:
                return nums[l]
            pivot=l+(r-l)//2
            pivot=partition(l,r,pivot)
            if k==pivot:
                return nums[k]
            elif k<pivot:
                r=pivot-1
            else:
                l=pivot+1
                
            