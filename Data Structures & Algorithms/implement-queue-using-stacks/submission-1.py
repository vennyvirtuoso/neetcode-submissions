class MyQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if self.queue2:
            return self.queue2.pop()
        else:
            n = len(self.queue1)
            while n!=0:
                self.queue2.append(self.queue1.pop())
                n-=1
            return self.queue2.pop()
        

    def peek(self) -> int:
        if self.queue2:
            return self.queue2[-1]
        else:
            n = len(self.queue1)
            while n!=0:
                self.queue2.append(self.queue1.pop())
                n-=1
            return self.queue2[-1]

    def empty(self) -> bool:
        if not self.queue1 and  not self.queue2:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()