# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans=[]
        temp=head
        u=0
        while temp!=None:
            ans.append(temp)
            temp=temp.next
            u+=1
        i,j=0,len(ans)-1

        while i<j:
            ans[i].next=ans[j]
            i+=1
            if i>=j:
                break
            ans[j].next=ans[i]
            j-=1
        ans[i].next=None