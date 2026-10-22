# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        stk = deque()
        stk.append(root)

        ans = []
        if not root:
            return ans

        while stk:
            # if the top doesnt have any children then print and pop
            top = stk[-1]
            if top.left:
                stk.append(top.left)
                top.left = None
            else:
                ans.append(stk.pop().val)
                if top.right:
                    stk.append(top.right)
                    top.right = None
        return ans