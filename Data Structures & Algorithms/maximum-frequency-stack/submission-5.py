class FreqStack:

    def __init__(self):
        self.fstack = [[]]
        self.freq = {}

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        if f == len(self.fstack):
            self.fstack.append([])

        self.fstack[f].append(val)

    def pop(self) -> int:
        if not self.fstack[-1]:
            self.fstack.pop()

        val = self.fstack[-1].pop()
        self.freq[val] -= 1

        return val