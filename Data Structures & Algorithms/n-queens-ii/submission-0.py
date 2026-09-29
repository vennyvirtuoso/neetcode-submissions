class Solution:
    def totalNQueens(self, n: int) -> int:
        row=set()
        col=set()
        diag1=set()
        diag2=set()
        ans=0
        def dfs(index):

            if index==n:
                nonlocal ans
                ans+=1
            else:
                for i in range(n):
                    if not (index in row or i in col or (index-i) in diag1 or (index+i) in diag2):
                        row.add(index)
                        col.add(i)
                        diag1.add(index-i)
                        diag2.add(index+i)

                        dfs(index+1)

                        row.remove(index)
                        col.remove(i)
                        diag1.remove(index-i)
                        diag2.remove(index+i)
        dfs(0)

        return ans
