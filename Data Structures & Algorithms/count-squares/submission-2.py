class CountSquares:

    def __init__(self):
        self.points=dict(dict())

    def add(self, point: List[int]) -> None:
        if point[0] in self.points:
            temp=self.points[point[0]]
            if point[1] in temp:
                temp[point[1]]+=1
            else:
                temp[point[1]]=1
        else:
            temp=dict()
            temp[point[1]]=1
            self.points[point[0]]=temp
    
        

    def count(self, point: List[int]) -> int:
        # print(self.points)
        ans=0
        if point[0] in self.points:
            yps=self.points[point[0]]

            for y in yps:
                if y == point[1]:
                    continue
                diff=abs(point[1]-y)
                if point[0]-diff in self.points:
                    if point[1] in self.points[point[0]-diff] and y in self.points[point[0]-diff]:
                        ans+=(self.points[point[0]][y]*self.points[point[0]-diff][point[1]]*self.points[point[0]-diff][y])
                if point[0]+diff in self.points:
                    if point[1] in self.points[point[0]+diff] and y in self.points[point[0]+diff]:
                        ans+=(self.points[point[0]][y]*self.points[point[0]+diff][point[1]]*self.points[point[0]+diff][y])

        return ans
        
