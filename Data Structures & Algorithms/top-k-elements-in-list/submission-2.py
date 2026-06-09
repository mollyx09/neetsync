class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        ntimes = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            ntimes[c].append(n)
        
        res = []

        for i in range(len(ntimes) - 1, 0, -1):
            for n in ntimes[i]:
                res.append(n)
                if len(res) == k:
                    return res
        