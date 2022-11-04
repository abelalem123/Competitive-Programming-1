# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        current=head
        ln=1
        while current.next:
            current=current.next
            ln+=1
        t=ln-n
        i=1
        prior=head
        
        #if at end
        if t==1 and prior.next==None:
            return prior
        #if to be deleted is head(at beginning)
        if t==0:
            return prior.next
        #at the middle
        while (i<t) and prior.next:
            prior=prior.next
            i+=1
        prior.next=prior.next.next
        return head
            
            
            