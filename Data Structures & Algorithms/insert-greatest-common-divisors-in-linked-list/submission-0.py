# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcdn(a,b):
            if b>a:
                a,b=b,a
            while b:
                a,b=b,a%b
            return a

        curr=head
        nextp=curr.next
        while nextp!=None:
            gcd = gcdn(curr.val, nextp.val)
            temp = ListNode(gcd)
            temp.next=nextp
            curr.next=temp
            curr=nextp
            nextp=curr.next

        return head