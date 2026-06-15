class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Optimal solution
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            
            k = len(nums) - 1
            while j < k :
                sum = nums[i] + nums[j] + nums[k] 
                if ( sum > 0):
                    k = k - 1
                
                elif (sum < 0):
                    j = j + 1
                
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k = k - 1
                    j = j + 1
                    while (j < k and nums[j] == nums[j - 1]):
                        j = j + 1
                    while (j < k and nums[k] == nums[k + 1]):
                        k = k - 1
                
            
        
        return res
                #Brute Force appraoch - Too inefficient as O(n*3) TC
        # res = []

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])

        #                 if triplet not in res:
        #                     res.append(triplet)
        
        # return list(res)
        