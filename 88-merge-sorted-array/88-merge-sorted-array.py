class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i=0
        j=0
        new_arr=[]
        while i<m and j<n:
            if nums2[j]<nums1[i]:
                new_arr.append(nums2[j])
                #nums1.insert(k,nums2[j])
                j+=1
            else:
                new_arr.append(nums1[i])
                i+=1
        while i<m:
            new_arr.append(nums1[i])
            i+=1
        while j<n:
            new_arr.append(nums2[j])
            j+=1
        nums1[:]=new_arr[:]