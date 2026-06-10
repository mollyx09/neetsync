class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute Force solution, TC = 
        if not nums:
            return 0
        
        longest = 1
        for i in range(len(nums)):
            current = nums[i] + 1
            count = 1
            while True:
                found = False
                for j in range(len(nums)):
                    if current == nums[j]:
                        count += 1
                        current += 1
                        found = True
                        break

                if not found:
                    break

            
            longest = max(longest,count)

        return longest

