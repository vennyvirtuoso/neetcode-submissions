class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(curr,open,close):
            if open==n and close==n:
                ans.append(curr)
            if open>=close and open<=n and close<=n:
                curr+="("
                generate(curr,open+1,close)
                curr=curr[:-1]
                curr+=")"
                generate(curr,open,close+1)
            else:
                return 





        generate("",0,0)
        return ans

