class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force solution - TC = O(n*n), SC = O(n)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] == nums[j]):
        #             return True
        # return False

        # #Better solution - used hashmap - what is the different b/w hash set and hash map and when should each be used
        # numsDict = {}
        # for i in range(len(nums)):
        #     if nums[i] in numsDict:
        #         return True
        #     else:
        #         numsDict[nums[i]] = i
            
        # return False

        #Hashset approach
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])

        return False

                
