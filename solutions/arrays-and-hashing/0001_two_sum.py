class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(zip(nums, range(len(nums)))))
        l = 0
        r = len(nums)-1
        
        while True:
            if (nums[l][0] + nums[r][0]) < target:
                l += 1
            elif (nums[l][0] + nums[r][0] > target):
                r -= 1
            else:
                return [nums[l][1], nums[r][1]]