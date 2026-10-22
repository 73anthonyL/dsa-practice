# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def bstCreator(v, lo, hi):
            if hi == lo:
                return
            
            mid = (lo + hi) // 2

            if (lo <= mid-1):
                l = TreeNode(nums[((lo + mid - 1) // 2)])
                v.left = l
                bstCreator(l, lo, mid - 1)

            if (hi >= mid+1):
                r = TreeNode(nums[((mid + 1 + hi) // 2)])
                v.right = r
                bstCreator(r, mid + 1, hi)
        
        head = TreeNode(nums[(0 + len(nums) - 1) // 2])
        bstCreator(head, 0, len(nums) - 1)
        return head