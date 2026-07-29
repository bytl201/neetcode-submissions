class Node():
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev, node.nxt = prev, nxt
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, right.prev = right, node

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.remove(self.map[key])

        node = Node(key, value)
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.map.pop(lru.key, None)