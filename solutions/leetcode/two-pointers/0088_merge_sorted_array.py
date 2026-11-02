class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r, insertion_index = m - 1, n - 1, m + n - 1
        while insertion_index >= 0:
            insertion = -1
            if l == -1:
                nums1[insertion_index] = nums2[r]
                r -= 1
            elif r == -1:
                nums1[insertion_index] = nums1[l]
                l -= 1
            else:
                if nums1[l] >= nums2[r]:
                    nums1[insertion_index] = nums1[l]
                    l -= 1
                else:
                    nums1[insertion_index] = nums2[r]
                    r -= 1
            insertion_index -= 1
