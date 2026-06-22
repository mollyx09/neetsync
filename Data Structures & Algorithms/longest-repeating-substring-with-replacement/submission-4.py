class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute Force Approach/Inefficient sliding window approach
        # l,r = 0,0
        # counter = {}
        # res = 0

        # while r < len(s):
        #     counter.clear()
        #     substr = s [l:r + 1]
        #     for ch in substr:
        #         counter[ch] = 1 + counter.get(ch, 0)

        #     max_key, max_value = max(counter.items(), key=lambda item: item[1])

        #     if (len(substr) - max_value) <= k:
        #         res = max((len(substr)), res)
        #         r += 1
        #     else:
        #         l += 1
            
        # return res
        #Optimal appraoch
        l = 0
        res = 0
        counter = {}

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)

            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res