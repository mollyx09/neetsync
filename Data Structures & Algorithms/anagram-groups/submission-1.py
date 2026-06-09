class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hdict = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort in hdict:
                hdict[sort].append(strs[i])
            else:
                hdict[sort] = [strs[i]]
        return list(hdict.values())

        
        # hdict = {}
        # for i in range(len(strs)):
        #     sort = "".join(sorted(strs[i]))
        #     if sort in hdict:
        #         hdict[sort].append(strs[i])
        #     else:
        #         hdict[sort] = [strs[i]]

        # return list(hdict.values())