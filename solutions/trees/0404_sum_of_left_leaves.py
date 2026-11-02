# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        ret = 0
        if root.left:
            if not (root.left.left or root.left.right):
                ret += root.left.val
            else:
                ret += self.sumOfLeftLeaves(root.left)

        if root.right:
            if (root.right.left or root.right.right):
                ret += self.sumOfLeftLeaves(root.right)
        
        return ret

