class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for l in range(len(prices)):
            r = len(prices) - 1
            while r > l:
                if prices[r] > prices[l]:
                    price = prices[r] - prices[l]
                    max_profit = max(max_profit, price)
                r -= 1
            
        return max_profit