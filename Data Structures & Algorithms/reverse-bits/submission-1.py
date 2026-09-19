class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        # print(1<<32)
        for i in range(0,32):
            lastbit = (n>>i)&1
            # print(lastbit)
            if lastbit:
                rbit = 31-i
                # print(rbit)
                temp=1<<rbit
                # print(temp)
                ans|=temp
                print(ans)
        return ans
