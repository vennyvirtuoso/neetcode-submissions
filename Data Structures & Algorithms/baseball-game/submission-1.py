class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        ans=0
        for ch in operations:
            if ch=="C":
                ans-=scores[-1]
                scores.pop()
                
            elif ch =="D":
                ans+=(2*scores[-1])
                scores.append(2*scores[-1])
                
            elif ch == "+":
                ans+=(scores[-1]+scores[-2])
                scores.append(scores[-1]+scores[-2])
                
            else:
                scores.append(int(ch))
                ans+=(int(ch))
        # ans=0
        # for intt in scores:
        #     ans+=intt
        return ans