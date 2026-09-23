class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        for i in range(m):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(m):
            for j in range(m//2):
                matrix[i][j],matrix[i][m-j-1]=matrix[i][m-j-1],matrix[i][j]