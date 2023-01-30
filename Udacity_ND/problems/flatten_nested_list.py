import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")

from my_datastructures.single_linked_list import SingleLinkedList, Node


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(SingleLinkedList):
    """
    a nested linked list is a list which node values can be either integers
    or another linked list.
    """

    def flatten(self):
        """
        flatten a nested linked list in a sorted order and convert to one linked list.
        """
        res_linked_list = SingleLinkedList(None)
        node = self.head
        while node is not None:
            if isinstance(node.value, int):
                res_linked_list.insert_ordered(node.value)
            elif isinstance(node.value, SingleLinkedList):
                self.__flatten(res_linked_list, node.value)
            node = node.next
        return res_linked_list

    def __flatten(self, dest, node):
        node = node.head
        while node is not None:
            if isinstance(node.value, int):
                dest.insert_ordered(node.value)
            elif isinstance(node.value, SingleLinkedList):
                self.__flatten(dest, node.value)
            node = node.next
