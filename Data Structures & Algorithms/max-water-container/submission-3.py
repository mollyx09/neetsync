class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Optimal code
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
        #Brute Force
        # distance = 0
        # totalMax = 0
        # maxHeight = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         if heights[i] < heights[j]:
        #             distance = j - i
        #             maxHeight = heights[i] * distance
        #         elif heights[i] > heights[j]:
        #             distance = j - i
        #             maxHeight = heights[j] * distance
        #         else:
        #             distance = j - i
        #             maxHeight = heights[j] * distance
                
        #         totalMax = max(totalMax, maxHeight)
                
            

        # return totalMax

        #Approach 2, T.C. = O(n*2)
        # res = 0

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        #         res = max(area, res)

        # return res
        