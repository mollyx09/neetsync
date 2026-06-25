class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        i = 0
        j = 1
        while i < j and j < len(temperatures) + 1:
            if j == len(temperatures):
                res.append(0)
                i += 1
                j = i + 1
            elif i == len(temperatures) - 1:
                res.append(0)

            elif j != len(temperatures):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    i += 1
                    j = i + 1

                elif temperatures[i] >= temperatures[j]:
                    j += 1
        return res
        