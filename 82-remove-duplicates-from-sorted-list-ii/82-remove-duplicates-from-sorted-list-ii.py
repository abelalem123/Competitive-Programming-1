# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #have sentinel
        #make a predicisor start from the sentinel
        dummy=ListNode(0,next=head)
        pred=dummy # one step before head
        while head:
            if head.next and head.next.val==head.val:
                # iterate untill nomore duplicates
                while head.next and head.next.val==head.val:
                    head=head.next
                #assign predicisor to next of head i.e eliminate all duplicates
                pred.next=head.next
                
            else:
                pred=pred.next
            head=head.next
        return dummy.next