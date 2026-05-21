# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbalanced = True

        def dfs(node):
            nonlocal isbalanced # Tells Python to use the outer variable
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Check absolute difference to catch right-heavy trees too
            if abs(left - right) > 1:
                isbalanced = False

            return 1 + max(left, right)

        dfs(root)
        return isbalanced





        