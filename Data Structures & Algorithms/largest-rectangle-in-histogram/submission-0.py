class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
            else:
                if heights[i] >= stack[-1][1]:
                    stack.append([i, heights[i]])
                else:
                    start = i

                    while stack and heights[i] < stack[-1][1]:
                        ind, h = stack.pop()
                        l = h
                        b = i - ind
                        area = l * b
                        maxArea = max(area,maxArea)
                        start = ind
                    stack.append([start, heights[i]])

        while stack:
            ind, h = stack.pop()
            l = h
            b = len(heights) - ind
            area = l * b
            maxArea = max(maxArea, area)
                
        return maxArea
        