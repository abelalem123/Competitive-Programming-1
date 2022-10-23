class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        merge=[[]]
        for i in nums:
            merge=self.con(merge,i)
        return merge
                
    def con(self,arr,b):
        new_list=list()
        for i in arr:
            temp=i+[b]
            new_list.append(list(temp))
        return arr+new_list
#         res=[]
#         def search(i,sub):
#             # last element
            
#             if i>len(nums):
#                 return
#             if i==(len(nums)):
#                 res.append(sub.copy())
#                 return
#             sub.append(nums[i])
#             search(i+1,sub)
#             sub.pop()
#             search(i+1,sub)
#         search(0,[])
#         return res