class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_vals = set()
    res_list = LinkedList()
    node = llist_1.head
    while node is not None:
        if node.value not in union_vals:
            res_list.append(node.value)
            union_vals.add(node.value)
        node = node.next
    node = llist_2.head
    while node is not None:
        if node.value not in union_vals:
            res_list.append(node.value)
            union_vals.add(node.value)
        node = node.next
    return res_list


def intersection(llist_1, llist_2):
    l1_values = set()
    res_list = LinkedList()
    node = llist_1.head
    while node is not None:
        l1_values.add(node.value)
        node = node.next
    node = llist_2.head
    intersec_vals = set()
    while node is not None:
        if node.value in l1_values and node.value not in intersec_vals:
            res_list.append(node.value)
            intersec_vals.add(node.value)
        node = node.next
    return res_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 3, 4, 5, 5, 5, 6]
element_2 = [5, 5, 6, 6, 6]
for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
assert str(union(linked_list_1, linked_list_2)) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> "
assert str(intersection(linked_list_1, linked_list_2)) == "5 -> 6 -> "
print("Test Case 1 passed.")

# Test Case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2]
element_2 = []
for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
assert str(union(linked_list_1, linked_list_2)) == "1 -> 2 -> "
assert str(intersection(linked_list_1, linked_list_2)) == ""
print("Test Case 2 passed.")

# Test Case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, None]
element_2 = [None, 3, 4]
for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
assert str(union(linked_list_1, linked_list_2)) == "1 -> 2 -> None -> 3 -> 4 -> "
assert str(intersection(linked_list_1, linked_list_2)) == "None -> "
print("Test Case 3 passed.")