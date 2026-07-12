# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head==None:
            return False
        loop=False
        while fast.next!=slow:
            loop=True
            if fast.next!=None:
                if fast.next.next!=None:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    break
            else:
                break

        if slow==fast.next:

            return True
        else:
            return False
