# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        list1=l1
        list2=l2
        head=ListNode()
        s=head
        while list1 and list2:
            s.next=ListNode((list1.val+list2.val+carry)%10)
            carry=(list1.val+list2.val+carry)//10
            list1=list1.next
            list2=list2.next
            s=s.next
        while list1:
            s.next=ListNode((list1.val+carry)%10)
            s=s.next
            carry=(list1.val+carry)//10
            list1=list1.next
        while list2:
            s.next=ListNode((list2.val+carry)%10)
            carry=(list2.val+carry)//10
            s=s.next
            list2=list2.next
        if carry:
            s.next=ListNode(carry)
        return head.next