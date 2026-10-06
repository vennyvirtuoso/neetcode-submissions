# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=head
        dummyl=None
        if left==1:
            dummyl=ListNode(0)
            dummyl.next=head
            head=dummyl
            prevl=dummyl
        left=left-1
        lp=temp
        rp=temp

        i=0
        while i<right:
            if i<=left-1:
                prevl=temp
            if i<=left:
                lp=temp

            if temp!=None:
                temp=temp.next
                rp=temp
            i+=1
        # if temp==None:
        #     dummyr=ListNode(0)
        #     rp.next=dummyr
        #     rp=dummyr
        print(prevl.val)
        print(lp.val)
        # print(rp.val)
        curr=lp.next
        # print(curr.val)
        while curr!=rp:
            temp=curr.next
            curr.next=prevl.next
            prevl.next=curr
            lp.next=temp
            curr=temp
        if dummyl!=None:
            return dummyl.next
        return head


        

        




