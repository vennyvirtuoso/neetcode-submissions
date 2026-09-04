class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1
        ans= (right-left)*min(heights[left],heights[right])
        while left<right:
            # print(left)
            # print(right)
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>=heights[right]:
                right-=1
            ans = max(ans,(right-left)*min(heights[left],heights[right]))

        return ans