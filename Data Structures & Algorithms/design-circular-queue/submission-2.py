class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=ListNode

class MyCircularQueue:

    def __init__(self, k: int):
        self.left=ListNode(-1)
        self.right=self.left
        self.size=0
        self.k=k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp=ListNode(value)
        if self.size==0:
            self.left.next=temp
            self.right=temp
        else:
            self.right.next=temp
            self.right=temp
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next=self.left.next.next
        if self.left.next is None:
            self.right=self.left
        self.size-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.val

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()