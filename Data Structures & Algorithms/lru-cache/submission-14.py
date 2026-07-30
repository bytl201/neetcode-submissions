class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_first(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def add_in_front(self, node):
        self.remove(node)
        self.add_first(node)

    def remove_last(self):
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.doublelinkedlist = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if(key in self.cache.keys()):
            n = self.cache[key]
            self.doublelinkedlist.add_in_front(n)
            return n.val
        else:
            return -1



    def put(self, key: int, value: int) -> None:
        if(key in self.cache.keys()):
            node = self.cache[key]
            node.val = value
            self.doublelinkedlist.add_in_front(node)
        
        else:
            if(len(self.cache) == self.cap):
                n = self.doublelinkedlist.remove_last()
                del self.cache[n.key]
            node = Node(key, value)
            self.cache[key] = node
            self.doublelinkedlist.add_first(node)