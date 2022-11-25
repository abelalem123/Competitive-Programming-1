# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        current=head
        temp=[]
        while current:
            temp.append(current.val)
            current=current.next
        #monotonic decreasing stack
        stack=[]
        result=[0]*len(temp)
        for idx,num in enumerate(temp):
            while stack and temp[stack[-1]]<num:
                result[stack.pop()]=num
            stack.append(idx)
        return result