class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root, total):
            total += root.val
            if not root.left and not root.right:
                return total == targetSum
            if root.left and dfs(root.left, total):
                return True
            if root.right and dfs(root.right, total):
                return True
            return False

        return dfs(root, 0)