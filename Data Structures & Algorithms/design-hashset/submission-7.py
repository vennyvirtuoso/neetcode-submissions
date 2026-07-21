class BST:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
class MyHashSet:

    def __init__(self):
        self.arr_bst = [None for _ in range(1001)]

    def add(self, key: int) -> None:
        index = key%1000
        node = self.arr_bst[index]
        if node == None:
            temp = BST(key)
            self.arr_bst[index]=temp
        else:
            while(node.left!=None or node.right!=None):
                if node.val == key:
                    break
                elif key<node.val:
                    node=node.left
                elif key>node.val:
                    node = node.right
            temp = BST(key)
            if key<node.val:
                node.left = temp
            else:
                node.right= temp
    def removenode(self,node,key):
        if node is None:
            return None
        if key<node.val:
            node.left = removenode(node.left,key)
        elif key>node.val:
            node.right = removenode(node.right,key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = node.right
            while(succ.left!=None):
                succ= succ.left
            
            node.val = succ.val
            node.right = removenode(node.right, succ.val)


    def remove(self, key: int) -> None:
        index = key%1000
        node = self.arr_bst[index]
        if node == None:
            return
        elif node.val==key:
            self.arr_bst[index]=None
        self.removenode(node,key)


    def contains(self, key: int) -> bool:

        index = key%1000
        node = self.arr_bst[index]
        # print(node.val)
        if node==None:
            return False
        if node.val == key:
            return True
        else:
            while(node.left!=None or node.right!=None):
                # print(node.val)
                if node.val == key:
                    return True
                elif key<node.val:
                    node=node.left
                elif key>node.val:
                    node = node.right
            if node.val == key:
                return True
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)