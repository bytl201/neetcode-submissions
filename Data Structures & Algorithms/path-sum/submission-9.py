class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root, total):
            if not root.left and not root.right and total+root.val == targetSum:
                return True
            if root.left and dfs(root.left, total+root.val):
                return True
            if root.right and dfs(root.right, total+root.val):
                return True
            return False

        return dfs(root, 0)