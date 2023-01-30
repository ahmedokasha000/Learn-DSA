class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = self.head
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = self.tail.next
