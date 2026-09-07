class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack = []
        ans = [0 for _ in range(len(temperatures))]
        for i,temp in enumerate(temperatures):
            if not tempstack:
                tempstack.append([temp,i+1])

            else:
                if tempstack[-1][0]>=temp:
                    tempstack.append([temp,i+1])
                else:
                    while tempstack and tempstack[-1][0]<temp:
                        ans[tempstack[-1][1]-1]=(i+1)-tempstack[-1][1]
                        tempstack.pop()
                    if not tempstack or tempstack[-1][0]>=temp:
                        tempstack.append([temp,i+1])
        return ans

        
# 30 38 30 36 35 40 28
# 30 38 38 38 38 40 40