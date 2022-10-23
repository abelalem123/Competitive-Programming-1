# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left=head
        current=head
        rev=None
        i=0
        dummy=ListNode()
        left=dummy
        while current:
            i+=1
            temp=current.next
            left.next=ListNode(current.val,current.next)
            left=left.next
            current.next=rev
            rev=current
            current=temp
        a=dummy.next
        pointe=head
        cycle=True
        a=a.next
        while i>1:
            if cycle:
                pointe.next=ListNode(val=rev.val)
                pointe=pointe.next
                rev=rev.next
            else:
                pointe.next=ListNode(val=a.val)
                pointe=pointe.next
                a=a.next
            cycle= not cycle
            i-=1

            
