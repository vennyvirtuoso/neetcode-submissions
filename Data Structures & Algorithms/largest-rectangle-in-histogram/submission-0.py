class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = height * width
                maxArea = max(maxArea, area)

            stack.append(i)

        return maxArea