"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {None: None}

        walker = head
        while walker:
            mapping[walker] = Node(walker.val)
            walker = walker.next

        walker = head
        while walker:
            new_node = mapping[walker]
            new_node.next = mapping[walker.next]
            new_node.random = mapping[walker.random]
            walker = walker.next

        return mapping[head]