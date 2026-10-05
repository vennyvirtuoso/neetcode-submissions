# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next

        n=size-n
        temp=head
        if n==0:
            return head.next
        while n-1>0:
            temp=temp.next
            n-=1

        temp.next=temp.next.next
        return head