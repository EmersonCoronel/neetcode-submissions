class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        i = 0
        while i < len(prices) - 1:
            diff = max(prices[i+1:]) - prices[i]
            if diff > max_diff:
                max_diff = diff
            i += 1
        return max_diff