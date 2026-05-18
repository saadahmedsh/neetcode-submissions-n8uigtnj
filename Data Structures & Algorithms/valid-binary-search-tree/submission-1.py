# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev_val = [float("-inf")]

        def dfs(node, prev_val):
            if not node:
                return True

            if not dfs(node.left, prev_val):
                return False

            if node.val <= prev_val[0]:
                return False
            prev_val[0] = node.val

            return dfs(node.right, prev_val)

        


        return dfs(root, prev_val)
        