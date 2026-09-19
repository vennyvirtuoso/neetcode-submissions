class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cin= [0 for i in range(n+1)]
        cout = [0 for i in range(n+1)]
        for pair in trust:
            cin[pair[1]]+=1
            cout[pair[0]]+=1
        # print(cin)
        for i in range(n+1):
            if cin[i]==n-1 and cout[i]==0:
                return i
        return -1
