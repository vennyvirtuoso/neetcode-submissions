class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)


        for i in range(len(row)):
            r=row[i]
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        for i in range(len(col)):
            c=col[i]
            for j in range(len(matrix)):
                matrix[j][c]=0

        # return matrix