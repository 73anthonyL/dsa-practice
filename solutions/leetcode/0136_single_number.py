class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n

        return ans
