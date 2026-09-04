class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[]
        rightmax = [0 for _ in range(len(height))]
        maxx=float('-inf')
        for i in range(len(height)):
            maxx=max(maxx, height[i])
            leftmax.append(maxx)
        maxx= float('-inf')
        for i in range(len(height)-1,-1,-1):
            maxx=max(maxx,height[i])
            rightmax[i]=maxx
        # print(leftmax)
        # print(rightmax)
        ans =0
        for i in range(len(height)):
            ans+=(max((min(leftmax[i],rightmax[i])-height[i],0)))
        return ans