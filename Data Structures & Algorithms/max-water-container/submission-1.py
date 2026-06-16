class Solution:
    def maxArea(self, heights: List[int]) -> int:
        distance = 0
        totalMax = 0
        maxHeight = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] < heights[j]:
                    distance = j - i
                    maxHeight = heights[i] * distance
                elif heights[i] > heights[j]:
                    distance = j - i
                    maxHeight = heights[j] * distance
                else:
                    distance = j - i
                    maxHeight = heights[j] * distance
                
                totalMax = max(totalMax, maxHeight)
                
            

        return totalMax
        