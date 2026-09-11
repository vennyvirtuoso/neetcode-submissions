class FreqStack:

    def __init__(self):
        self.fstack = [[]]
        self.freq=dict()


    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val]+=1
        else:
            self.freq[val]=1
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
        # return 3


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()