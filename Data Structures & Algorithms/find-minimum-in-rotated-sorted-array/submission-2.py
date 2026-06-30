class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute force
        min = float('inf')
        for a in nums:
            if a < min:
                min = a
        return min
        