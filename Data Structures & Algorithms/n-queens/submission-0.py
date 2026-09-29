class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        row = set()
        col= set()
        diag1=set()
        diag2=set()
        def dfs(index,curr):
            if index==n:
                ans.append(curr.copy())
            else:
                for i in range(n):
                    if not (index in row or i in col  or index-i in diag1 or index+i in diag2):

                        curr.append(i)
                        row.add(index)
                        col.add(i)
                        diag1.add(index-i)
                        diag2.add(index+i)

                        dfs(index+1,curr)

                        curr.pop()
                        row.remove(index)
                        col.remove(i)
                        diag1.remove(index-i)
                        diag2.remove(index+i)


    
        dfs(0,[])
        # print(ans)
        final_ans=[]
        for i in range(len(ans)):
            sub_ans=[]
            for j in range(n):
                temp=[]
                for k in range(n):
                    if ans[i][j]==k:
                        temp.append("Q")
                    else:
                        temp.append(".")
                row="".join(temp)
                sub_ans.append(row)
            final_ans.append(sub_ans)
            

        
        # print(final_ans)
        return final_ans



        # return [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]


        