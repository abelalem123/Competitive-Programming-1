# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
             return None
        if len(lists)<=1:
            return lists[0]
        mid=len(lists)//2
        left=self.mergeKLists(lists[:mid])
        right=self.mergeKLists(lists[mid:])
        return self.merge2(left,right)
    def merge2(self,list1,list2):
        left=list1
        right=list2
        head=ListNode()
        merge=head
        while left and right:
            if left.val<right.val:
                merge.next=left
                left=left.next
            else:
                merge.next=right
                right=right.next
            merge=merge.next
        if left:
            merge.next=left
        if right:
            merge.next=right
        return head.next