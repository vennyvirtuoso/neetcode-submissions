class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.mine= float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mine = min(self.mine,val)
        self.minstack.append(self.mine)
        # print(self.minstack)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if self.minstack:
            self.mine = self.minstack[-1]
        else:
            self.mine = float('inf')
        # print(f'after pop{self.minstack}')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.minstack)
        return self.minstack[-1]
