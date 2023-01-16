from single_linked_list import SingleLinkedList, Node

# Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

# Example:

# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    head = head
    last_odd_node = None
    last_odd_node_found = False
    node = None
    prev_node = None
    replace_happened = True
    node = head
    while node is not None:
        replace_happened = False
        print(f"node value  = {node.value}")
        if is_even(node.value) and not last_odd_node_found:
            last_odd_node = prev_node
            last_odd_node_found = True
            # print(f"Last odd found {last_odd_node} {last_odd_node.value}")

        elif not is_even(node.value) and last_odd_node_found: # move odd node after last odd node 
            print(f"moving node")
            prev_node.next = node.next
            # odd_node = Node(node.value)
            next_ref = node.next
            if last_odd_node is None:
                node.next = head
                head = node
            else:
                node.next = last_odd_node.next
                last_odd_node.next = node
            last_odd_node = node
            node = next_ref
            replace_happened = True
        if not replace_happened:
            prev_node = node
            node = node.next
        # if count>5:
        #     break
    return head


def is_even(value):
    return value % 2 == 0

def main():
    sll = SingleLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(6)
    sll.head = even_after_odd(sll.head)
    print(sll.to_list())
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
        