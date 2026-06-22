class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = {}
        map2 = {}
        windowSize = len(s1)


        if (len(s1) > len(s2)):
            return False

        for ch in s1:
            target[ch] = 1 + target.get(ch, 0)

        l = 0
        for r in range(len(s2)):
            map2[s2[r]] = 1 + map2.get(s2[r], 0)

            if r - l + 1 > windowSize:
                map2[s2[l]] -= 1
                

                if map2[s2[l]] == 0:
                    del map2[s2[l]]

                l += 1
            
            if map2 == target:
                return True

        return False

        
        # map1 = {}
        # map2 = {}
        # for ch in s1:
        #     map1[ch] = 1 + map1.get(ch, 0)

        # l = 0
        # windowsize = len(s1)

        # for r in range(len(s2)):
        #     map2.clear()

        #     if (r - l + 1) == windowsize:
        #         substr = s2[l:r + 1]
        #         l += 1

        #         for ch in substr:
        #             map2[ch] = 1 + map2.get(ch, 0)

        #     if map2 == map1:
        #             return True
        
        # return False
