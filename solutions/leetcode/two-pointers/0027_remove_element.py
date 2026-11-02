class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        removals, dq = 0, deque()
        for i in range(len(nums)):
            if nums[i] == val:
                removals += 1
                dq.append(i)
            else:
                if dq:
                    nums[dq.popleft()] = nums[i]
                    dq.append(i)
        return len(nums)-removals