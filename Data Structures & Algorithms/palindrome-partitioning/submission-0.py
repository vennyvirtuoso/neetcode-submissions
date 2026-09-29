class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)

        def palindrome(temp):
            n=len(temp)
            for i in range(n//2):
                if not temp[i]==temp[n-i-1]:
                    return False
            return True


        def dfs(start,curr):
            if start==n and len(curr)>0:
                # print(start)
                # print(curr)
                ans.append(curr.copy())
                return 
            else:
                for i in range(start,n):
                    temp=s[start:i+1]
                    if palindrome(temp):
                        curr.append(temp)
                        dfs(i+1,curr)
                        curr.pop()
                    # else:
                    #     dfs(i+1,curr)


        


        dfs(0,[])
        return ans