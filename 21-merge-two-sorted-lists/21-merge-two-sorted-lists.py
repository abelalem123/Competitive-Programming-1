# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
                
            