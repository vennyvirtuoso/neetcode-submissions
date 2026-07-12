# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        prev = None
        curr = head
        while curr.next!=None:
            # print("yes")
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        if curr!=None:
            curr.next = prev
        return curr