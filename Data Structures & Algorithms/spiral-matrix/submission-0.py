class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        L=0
        R=n-1
        T=0
        B=m-1

        while L<=R and T<=B:
            # print(ans)
            if L<=R and T<=B:
                for i in range(L,R+1):
                    ans.append(matrix[T][i])
                T+=1

            if L<=R and T<=B:
                for i in range(T,B+1):
                    ans.append(matrix[i][R])
                R-=1

            if L<=R and T<=B:
                for i in range(R,L-1,-1):
                    ans.append(matrix[B][i])
                B=B-1

            if L<=R and T<=B:
                for i in range(B,T-1,-1):
                    ans.append(matrix[i][L])
                L+=1
        return ans
            

