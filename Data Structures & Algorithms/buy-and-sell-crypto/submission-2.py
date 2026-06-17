class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float('inf')

        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)

        return maxPro 

        #Brute Force approach, TC = O(n*2), SC = O(1)
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         profit = max (profit, diff)

        # if profit < 0:
        #     return 0
        # else:
        #     return profit
        