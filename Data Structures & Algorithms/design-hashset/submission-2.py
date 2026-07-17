class MyHashSet:

    def __init__(self):
        self.arr_key = [False for i in range(1000001)]
    def add(self, key: int) -> None:
        self.arr_key[key] = True

    def remove(self, key: int) -> None:
        self.arr_key[key]=False

    def contains(self, key: int) -> bool:
        if self.arr_key[key]==True:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)