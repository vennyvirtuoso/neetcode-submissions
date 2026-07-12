# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        head = None
        curr = None
        while list1!=None and list2!=None:
            temp = ListNode()
            if list1.val<=list2.val:
                # print(list1.val)
                temp.val = list1.val
                if head == None:
                    # print("RF")
                    head = temp
                    curr = temp
                else:
                    curr.next = temp
                    curr = temp
                list1 = list1.next
            else:
                # print(list2.val)
                temp.val = list2.val
                if head == None:
                    # print("RF")
                    head = temp
                    curr = temp
                else:
                    curr.next = temp
                    curr=temp
                list2 = list2.next
            
        if list1!=None:
            curr.next = list1
        
        if list2!=None:
            curr.next = list2
        return head




            
        