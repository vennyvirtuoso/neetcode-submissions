class ListNode:
    def __init__(self,val=0,next=None,back=None):
        self.val=val
        self.next=next
        self.back=back
        self.key=0
class LRUCache:

    def __init__(self, capacity: int):
        self.mapp=dict()
        self.size=0
        self.head=None
        self.tail=None
        self.k=capacity


    def update(self,node):
        # print(f'update called{node.val}')
        if node!=self.tail:
            print(node.val)
            if node.back!=None:
                node.back.next=node.next
            node.next.back=node.back
            self.tail.next=node
            node.back=self.tail
            if node==self.head:
                self.head=self.head.next
                node.next=None
            self.tail=node


    def get(self, key: int) -> int:
        # print(f'get called{key}')
        if key in self.mapp:
            node=self.mapp[key]
            self.update(node)
            return node.val
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        # print(f'put called{key}')
        if key in self.mapp:
            self.mapp[key].val=value
            node=self.mapp[key]
            self.update(node)

        else:
            temp=ListNode()
            temp.val=value
            temp.key=key
            if self.size==0:
                self.head=temp
                self.tail=temp
            else:
                self.tail.next=temp
                temp.back=self.tail
                self.tail=temp
            #mapping
            self.mapp[key]=temp
            self.size+=1
            if self.size>self.k:
                self.mapp.pop(self.head.key)
                self.head=self.head.next
                self.head.back=None

