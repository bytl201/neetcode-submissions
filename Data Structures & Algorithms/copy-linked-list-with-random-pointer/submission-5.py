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
        new_map = {None: None}

        walker = head
        while walker:
            new_map[walker] = Node(walker.val)
            walker = walker.next

        walker = head
        while walker:
            new_node = new_map[walker]
            new_node.next = new_map[walker.next]
            new_node.random = new_map[walker.random]
            walker = walker.next

        return new_map[head]