class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])
        for i in range(m):
            for j in range(n):
                t_sum=0
                if i-1>=0:
                    t_sum+=self.matrix[i-1][j]
                if j-1>=0:
                    t_sum+=self.matrix[i][j-1]
                if i-1>=0 and j-1>=0:
                    t_sum-=self.matrix[i-1][j-1]
                t_sum+=self.matrix[i][j]
                self.matrix[i][j]=t_sum
        # print(self.matrix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.matrix[row1-1][col2])
        # print(self.matrix[row2][col1-1])
        ans=self.matrix[row2][col2]
        if row1-1>=0:
            ans=ans-self.matrix[row1-1][col2]
        if col1-1>=0:
            ans=ans-self.matrix[row2][col1-1]
        if col1-1>=0 and row1-1>=0:
            ans=ans+self.matrix[row1-1][col1-1]
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)