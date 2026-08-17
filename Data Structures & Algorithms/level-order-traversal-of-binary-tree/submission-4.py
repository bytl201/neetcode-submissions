# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []

        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            sub_arr = []

            for _ in range(len(queue)):
                curr = queue.popleft()
                sub_arr.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            arr.append(sub_arr)
        return arr