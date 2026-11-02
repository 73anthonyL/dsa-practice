# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(v):
            if not v:
                return (1, True)

            if (not v.left) and (not v.right):
                return (1, True)
            elif (not v.left):
                a, b = dfs(v.right)
                return (1 + a, a == 1 and b)
            elif (not v.right):
                a, b = dfs(v.left)
                return (1 + a, a == 1 and b)

            a, b = dfs(v.left)
            c, d = dfs(v.right)

            return (1 + max(a, c), (abs(a - c) <= 1) and b and d)
        
        a, b = dfs(root)
        return b