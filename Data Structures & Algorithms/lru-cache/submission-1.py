class Node():
    def __init__(self, key, val):
        self.key, self.val = key,val
        self.prev, self.next = None,None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapping = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next, node.next = node, right
        node.prev, right.prev = prev, node

    def get(self, key: int) -> int:
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
        
        new_node = Node(key, value)
        self.mapping[key] = new_node
        self.insert(new_node)
        
        if len(self.mapping) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.mapping.pop(lru.key,None)
        
