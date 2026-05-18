# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side = []
        level = 0


        def dfs(node, level, right_side):

            if not node:
                return
                
            if level == len(right_side):
                right_side.append(node.val)
                
            dfs(node.right, level + 1, right_side)
            dfs(node.left, level + 1, right_side)


        dfs(root, 0, right_side)

        return right_side