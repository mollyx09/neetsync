class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for i in range(len(height))]
        prefix[0] = height[0]
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i])

        n = len(height)

        suffix = [0 for i in range(len(height))]
        suffix[n - 1] = height[n - 1]
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        total = 0
        for i in range(len(height)):
            leftMax = prefix[i]
            rightMax = suffix[i]

            if (height[i] < leftMax and height[i] < rightMax):
                total += min(leftMax, rightMax) - height[i]

        
        return total
        