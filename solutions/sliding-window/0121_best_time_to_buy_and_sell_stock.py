class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        min_so_far = prices[0]

        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])
        
        return ans
        