class FreqStack:

    def __init__(self):
        self.fstack = [[]]
        self.freq=dict()


    def push(self, val: int) -> None:
        self.freq[val]=self.freq.get(val,0)+1
        if self.freq[val]!=len(self.fstack):
            self.fstack[self.freq[val]].append(val)
        else:
            self.fstack.append([val])

    def pop(self) -> int:
        # print(self.fstack)
        if len(self.fstack[-1])>0:
            self.freq[self.fstack[-1][-1]]-=1
        else:
            self.fstack.pop()
            self.freq[self.fstack[-1][-1]]-=1

        return self.fstack[-1].pop()



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()