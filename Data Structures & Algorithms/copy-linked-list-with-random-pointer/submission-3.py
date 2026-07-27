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
        # holds orignal node: deep copy node
        mapping = {None: None}

        # create deep copy nodes and map
        walker = head
        while walker:
            mapping[walker] = Node(walker.val)
            walker = walker.next

        
        # add the other class attributes to deep copy node
        walker = head
        while walker:
            copy = mapping[walker]
            copy.random = mapping[walker.random]
            copy.next = mapping[walker.next]
            walker = walker.next

        return mapping[head]
        