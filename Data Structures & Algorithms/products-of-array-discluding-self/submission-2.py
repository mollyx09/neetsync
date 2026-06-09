class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Brute force solution, TC = O(n*n), SC = O(n)
        # res = [i for i in range(len(nums))]
        # for i in range(len(nums)):
        #     n = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             n = n * nums[j]

        #     res[i] = n

        # return res

        #Better aproach
        # prefix = [1 for i in range(len(nums))]
        # postfix = [1 for i in range(len(nums))]

        # for i in range(len(nums)):
        #     if i == 0:
        #         prefix[i] = 1
        #     else:
        #         prefix[i] = prefix[i - 1] * nums[i - 1]
        # for j in range(len(nums) - 1, -1, -1):
        #     if j == len(nums) - 1:
        #         postfix[j] = 1
        #     else:
        #         postfix[j] = postfix[j + 1] * nums[j + 1]

        # res = [1 for i in range(len(nums))]
        # for i in range(len(postfix)):
        #     res[i] = prefix[i] * postfix[i]

        # return res
        
        #Optimal appraoch
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
            
        return res
