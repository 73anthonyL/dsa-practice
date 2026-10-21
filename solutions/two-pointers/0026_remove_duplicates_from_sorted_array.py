class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        unique_numbers, prev = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[unique_numbers] = nums[i]
                unique_numbers += 1
                prev = nums[i]
        return unique_numbers
