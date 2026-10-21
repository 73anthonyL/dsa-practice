# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def dfs(u, v):
            if (u and not v) or (v and not u):
                return False

            if u:
                if u.val != v.val:
                    return False
                return dfs(u.left, v.left) and dfs(u.right, v.right)
            else:
                return True

        return dfs(p, q)