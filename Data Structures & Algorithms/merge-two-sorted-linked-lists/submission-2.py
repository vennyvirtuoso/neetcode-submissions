# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(list1,list2):
    if list1==None:
        return list2
    if list2==None:
        return list1
    if list1.val<=list2.val:
        list1.next = merge(list1.next,list2)
        return list1
    else:
        list2.next = merge(list1,list2.next)
        return list2
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1==None:
        #     return list2
        # if list2==None:
        #     return list1
        
        return merge(list1,list2)




            
        