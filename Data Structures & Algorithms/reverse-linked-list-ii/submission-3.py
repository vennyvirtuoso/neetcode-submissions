class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prevl = dummy


        for _ in range(left - 1):
            prevl = prevl.next

        curr = prevl.next

        for _ in range(right - left):
            temp = curr.next

            curr.next = temp.next
            temp.next = prevl.next
            prevl.next = temp

        return dummy.next