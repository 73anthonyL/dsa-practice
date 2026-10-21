class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while (lo <= hi):
            center = (lo + hi) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                lo = center + 1
            else:
                hi = center - 1
        return lo