"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping={None:None}
        temp=head
        while temp!=None:
            mapping[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp!=None:
            temp2=mapping[temp]
            if temp.next:
                temp2.next=mapping[temp.next]
            if temp.random:
                temp2.random=mapping[temp.random]
            temp=temp.next
        return mapping[head]
            



