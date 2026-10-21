# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def leftAndRight(u, v):
            if (not u) and (not v):
                return True

            if not (u and v):
                return False
            
            if u.val != v.val:
                return False
            
            return leftAndRight(u.left, v.right) and leftAndRight(u.right, v.left)
        
        if not root:
            return True
        return leftAndRight(root.left, root.right)
            