# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        maxDepth = 0
        res = []

        def dfs(root, depth):
            if not root:
                return
            
            nonlocal maxDepth
            if depth > maxDepth or maxDepth == 0:
                res.append(root.val)

            maxDepth = max(maxDepth, depth)

            dfs(root.right, 1 + depth)
            dfs(root.left, 1 + depth)

            return
        dfs(root, 0)

        return res
