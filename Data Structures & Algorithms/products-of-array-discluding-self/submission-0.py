class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [i for i in range(len(nums))]
        for i in range(len(nums)):
            n = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    n = n * nums[j]

            res[i] = n

        return res
        