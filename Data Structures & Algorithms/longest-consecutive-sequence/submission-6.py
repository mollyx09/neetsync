class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute Force solution, TC = O(n^3), SC = O(1)
        # if not nums:
        #     return 0
        
        # longest = 1
        # for i in range(len(nums)):
        #     current = nums[i] + 1
        #     count = 1
        #     while True:
        #         found = False
        #         for j in range(len(nums)):
        #             if current == nums[j]:
        #                 count += 1
        #                 current += 1
        #                 found = True
        #                 break

        #         if not found:
        #             break

            
        #     longest = max(longest,count)

        # return longest

        # #better Approach, TC = O(n), SC = O(1)
        # if not nums:
        #     return 0

        # nums.sort()
        # longest = 1
        # count = 0
        # lastSmallest = float('-inf')

        # for i in range(len(nums)):
        #     if (nums[i] - 1 == lastSmallest):
        #         count += 1
        #         lastSmallest = nums[i]
        #     elif (nums[i] != lastSmallest):
        #         count = 1
        #         lastSmallest = nums[i]

        #     longest = max(longest, count)

        # return longest

        #Optimal
        if not nums:
            return 0
        numsset = set(nums)
        longest = 1
        count = 0

        for item in numsset:
            if (item - 1) not in numsset:
                count = 1
                while (item + count) in numsset:
                    count += 1
                    
                longest = max(longest, count)

        return longest




