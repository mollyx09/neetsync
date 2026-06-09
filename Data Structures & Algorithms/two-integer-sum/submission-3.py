class Solution:
    #Brute Force Solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Solution - TC ~ Slightly less than O(n*2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i,j]

        #Better solution - TC, SC = O(n)

        myDict = {}
        for i in range(len(nums)):
            ele = target - nums[i]

            if ele in myDict:
                return [myDict[ele], i]

            myDict[nums[i]] = i

        # # Slightly better approach than brute force - if hashmap not allowed, using Two pointers instead - greedy approach
        # # Assumption - Array is already sorted; TC = O(n)
        # left = 0
        # right = len(nums) - 1

        # while(left < right):
        #     if(nums[left] + nums[right] > target):
        #         right = right - 1
        #     elif(nums[left] + nums[right] < target):
        #         left = left + 1
        #     else:
        #         return [left, right] 



