# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def is_same_tree(main_tree, sub_tree):
            if not main_tree and not sub_tree:
                return True

            if not main_tree or not sub_tree:   # fix 1
                return False

            if main_tree.val == sub_tree.val:
                return is_same_tree(main_tree.left, sub_tree.left) and is_same_tree(main_tree.right, sub_tree.right)
            else:
                return False

        
        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val and is_same_tree(node, subRoot): 
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)