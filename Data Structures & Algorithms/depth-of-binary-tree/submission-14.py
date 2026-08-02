# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        depth = 0

        if root:
            queue.append(root)

        while len(queue) > 0:

            depth += 1

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
        return depth