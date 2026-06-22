class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        map2 = {}
        for ch in s1:
            map1[ch] = 1 + map1.get(ch, 0)

        l = 0
        windowsize = len(s1)

        for r in range(len(s2)):
            map2.clear()

            if (r - l + 1) == windowsize:
                substr = s2[l:r + 1]
                l += 1

                for ch in substr:
                    map2[ch] = 1 + map2.get(ch, 0)

            if map2 == map1:
                    return True
        
        return False
