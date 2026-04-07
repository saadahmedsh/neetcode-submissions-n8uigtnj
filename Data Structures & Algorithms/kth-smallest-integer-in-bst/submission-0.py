# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = [0]
        res = [0]
        def dfs(curr_root):
            
            if not curr_root:                
                return
        
            dfs(curr_root.left)
            count[0] += 1
            
            if count[0] == k:
                res[0] = curr_root.val
                return

            dfs(curr_root.right)

        dfs(root)
        return res[0]