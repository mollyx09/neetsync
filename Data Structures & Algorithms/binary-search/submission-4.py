class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) // 2
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[n] == target:
                return n
            elif nums[n] > target:
                right = n - 1
                n = (left + right) // 2
            else:
                left = n + 1
                n = (left + right) // 2

        return -1

        