class StockSpanner:

    def __init__(self):
        self.span = [[float('inf'),0]]
        # self.ans=[]
        self.i=1
    def next(self, price: int) -> int:
        # if not self.span:
        #     span.append([[price,i]])
        #     self.i+=1
        day = self.i
        self.i+=1
        if self.span[-1][0]<=price:
            while self.span and self.span[-1][0]<=price:
                self.span.pop()
            ans=day-self.span[-1][1]
            self.span.append([price,day])
            return  ans
        else:
            # print(self.i)
            topday = self.span[-1][1]
            self.span.append([price,day])
            # print(day)
            # if topday==0:
            #     return day-topday
            return 1
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)