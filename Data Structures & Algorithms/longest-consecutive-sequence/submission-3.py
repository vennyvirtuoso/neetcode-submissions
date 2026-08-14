class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])

        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x==root_y:
            return
        if self.size[root_x]<self.size[root_y]:
            root_x,root_y = root_y, root_x
        self.parent[root_y]=root_x
        self.size[root_x]+=self.size[root_y]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listunique = list(set(nums))
        mapp = dict()
        for i in range(len(listunique)):
            mapp[listunique[i]]=i
        
        LCS = UnionFind(len(nums))
        for num in listunique:
            if num-1 in mapp:
                LCS.union(mapp[num], mapp[num-1])
        if len(nums)==0:
            return 0
        ans = max(LCS.size)
        return ans
