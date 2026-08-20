class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0, 0)
        self.cache = {}
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next, right.prev = node, node
        node.prev, node.next = prev, right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            val = self.cache[key]
            self.remove(val)
            self.insert(val)
            return val.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)

        

