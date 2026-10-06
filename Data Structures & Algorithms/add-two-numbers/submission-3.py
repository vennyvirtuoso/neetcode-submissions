# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1=l1
        p2=l2
        carry=0
        prev=None
        while p1!=None and p2!=None:
            v1=p1.val
            v2=p2.val
            p1.val=(v1+v2+carry)%10
            carry=(v1+v2+carry)//10
            prev=p1
            p1=p1.next
            p2=p2.next
        while p1!=None:
            v1=p1.val
            p1.val=(v1+carry)%10
            carry=(v1+carry)//10
            prev=p1
            p1=p1.next

        while p2!=None:
            v2=p2.val
            temp=ListNode()
            temp.val=(v2+carry)%10
            prev.next=temp
            carry=(v2+carry)//10
            prev=temp
            p2=p2.next
        
        if carry:
            temp=ListNode()
            temp.val=carry
            prev.next=temp
            
        return l1

