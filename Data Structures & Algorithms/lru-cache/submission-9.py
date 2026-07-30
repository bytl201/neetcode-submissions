class ListNode():
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = right.prev = node
        node.prev, node.next = prev, right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.remove(self.map[key])

        node = ListNode(key, value)
        self.map[key] = node
        self.insert(node)

        if len(self.map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.map.pop(lru.key, None)

