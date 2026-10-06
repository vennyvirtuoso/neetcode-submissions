class MyCircularQueue:

    def __init__(self, k: int):
        self.cirk=[-1]*k
        self.front=0
        self.back=0
        self.k=k
        self.size=0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cirk[self.back]=value
        self.back=(self.back+1)%self.k
        self.size+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        print(self.cirk)
        self.front=(self.front+1)%self.k
        self.size-=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        temp=self.cirk[self.front]
        return temp


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        temp=self.cirk[self.back-1]
        return temp

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