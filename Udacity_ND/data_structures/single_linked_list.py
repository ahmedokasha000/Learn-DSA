class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """ Append a value to the end of the list. """  
        node = Node(value)

        if self.head is None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.head.next is None:
            self.tail = self.head

    def to_list(self):
        node = self.head
        res = []
        while node is not None:
            res.append(node.value)
            node = node.next
        return res

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.head
        if node is None:
            raise IndexError(" pop from empty list")
        elif node.next is None:
            self.head = None
            self.tail = None
            return node.value
        else:
            while node.next != self.tail:
                node = node.next
            node.next = None
            res = self.tail.value
            self.tail = node
            return res

    def is_empty(self):
        res = (self.head is None and self.tail is None)
        return  res

    def len(self):
        llen = 0
        node = self.head
        while node is not None:
            llen += 1
            node = node.next
        return llen

    def insert(self, value, index):
        list_len = self.len()
        if index > list_len:
            raise IndexError(" trying to insert in a non existing index")

        node_to_insert = Node(value)

        if index == 0:
            self.prepend(value)
            return
        if index == list_len:
            self.append(value)
            return

        node_before_insert = None
        for ind in range(index):
            if node_before_insert is None:
                node_before_insert = self.head
            else:
                node_before_insert = node_before_insert.next

        node_to_insert.next = node_before_insert.next
        node_before_insert.next = node_to_insert
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next
        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """ Remove first occurrence of value. """
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == value:
                if node == self.head:
                    self.head = self.head.next
                if node == self.tail:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next = node.next
                del node
                return 
            prev_node = node
            node = node.next
        raise ValueError("Value not found in the list.")

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def insert_ordered(self, value):
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head
        prev = None
        # Iterate till the end of the currrent LinkedList
        new_node = Node(value)
        while node is not None:
            if (value < node.value):
                if prev is None:
                    new_node.next = self.head
                    self.head = new_node
                    return
                else:
                    new_node.next = node
                    prev.next = new_node
                    return
            prev = node
            node = node.next
        prev.next = new_node

def reverse( ip_sll):
    new_reversed_sll = SingleLinkedList()
    ip_list = ip_sll.to_list()
    for val in ip_list[::-1]:
        new_reversed_sll.append(val)
    return new_reversed_sll

# def main():
#     sll = SingleLinkedList()
#     sll.append(3)
#     sll.append(2)
#     sll.append(-1)
#     sll.append(0.2)
#     sll.prepend(22)
#     print("Pass" if (sll.to_list() == [22, 3, 2, -1, 0.2]) else "Fail")
#     sll2 = SingleLinkedList()
#     sll2.insert(4, index=0)
#     sll2.insert(5, index=0)
#     sll2.insert(2, index=1)
#     # sll2.insert(2, index=2)

#     sll2_reversed = reverse(sll2)
#     print(f" Sll2 list = {sll2.to_list()}")
#     print(f" Sll2 list = {sll2.len()}")
#     print(f" reversed sll2 list = {sll2_reversed.to_list()}")
# # if __name__ == '__main__':
# #     main();