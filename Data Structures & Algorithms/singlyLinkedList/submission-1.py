class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        iterator = self.head
        counter = 0
        while iterator:
            if counter == index:
                return iterator.val
            counter += 1
            iterator = iterator.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head)
        self.head = newNode
        if not self.tail:          # list was empty
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:          # list was empty
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:             # removing head
            self.head = self.head.next
            if not self.head:      # list became empty
                self.tail = None
            return True

        node = self.head
        counter = 0
        while node.next:
            if counter + 1 == index:
                if node.next == self.tail:   # removing tail
                    self.tail = node
                node.next = node.next.next
                return True
            counter += 1
            node = node.next       # <-- you forgot to advance the pointer
        return False

    def getValues(self) -> List[int]:
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next
        return arr