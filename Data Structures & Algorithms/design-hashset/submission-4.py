class ListNode():
    def __init__(self,value=0):
        self.value = value
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr_s= [None for _ in range(1001)]

    def add(self, key: int) -> None:
        index = key%1000
        start = self.arr_s[index]
        if start==None:
            temp = ListNode(key)
            self.arr_s[index]=temp
        else:
            while(start.next!=None):
                if start.value == key:
                    break
                start=start.next
            temp = ListNode(key)
            start.next=temp


    def remove(self, key: int) -> None:
        index = key%1000
        start = self.arr_s[index]
        if start == None:
            return 
        if start.value == key:
            self.arr_s[index]=None
        else:
            while(start.next!=None and start.next.value!=key):
                start = start.next
            start.next = start.next.next

    def contains(self, key: int) -> bool:
        index = key%1000
        start = self.arr_s[index]
        if start==None:
            return False
        while(start!= None):    
            if start.value == key:
                return True
            start =start.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)