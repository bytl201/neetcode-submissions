
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
            
        # Use BST property: if p and q are on different sides of root, root is LCA
        # If both are smaller, LCA is in the left subtree
        # If both are larger, LCA is in the right subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # This is the split point (or root is p or q), making root the LCA
            return root