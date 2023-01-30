
import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")

from my_datastructures.single_linked_list import SingleLinkedList, Node


class SortedLinkedList(SingleLinkedList):
    def sort(self):
        pass

    def append(self, value):
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
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


def main():
    sorted_ll = SortedLinkedList()
    sorted_ll.append(5)
    sorted_ll.append(6)
    sorted_ll.append(2)
    sorted_ll.append(1)
    print(f" sorted linked list elements  = {sorted_ll.to_list()}")


main()
