from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        n=len(self.queue)
        while n!=1:
            self.queue.append(self.queue.popleft())
            n-=1
        intt=self.queue.popleft()
        return intt

    def top(self) -> int:
        n=len(self.queue)
        while n!=1:
            self.queue.append(self.queue.popleft())
            n-=1
        intt= self.queue.popleft()
        self.queue.append(intt)
        return intt
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()