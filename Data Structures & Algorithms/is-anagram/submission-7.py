class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force
        # s_array = list(s)
        # t_array = list(t)

        # s_dict = {}
        # t_dict = {}

        # if len(s) != len(t):
        #     return False


        # for i in range(len(s_array)):
        #     count = 0
        #     for j in range(len(s_array)):
        #         if (s_array[i] == s_array[j]):
        #             count += 1
                
        #     s_dict[s_array[i]] = count
        

        # for i in range(len(t_array)):
        #     count = 0
        #     for j in range(len(t_array)):
        #         if (t_array[i] == t_array[j]):
        #             count += 1
                
        #     t_dict[t_array[i]] = count
        

        # if (s_dict == t_dict):
        #     return True
        # else:
        #     return False

        if Counter(s) == Counter(t):
            return True
        return False

        #Better, TC = SC = O(n)

        smap = {}
        tmap = {}

        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i], 0)

            tmap[t[i]] = 1 + tmap.get(t[i], 0)

        if smap != tmap:
            return False

        return True 


        