# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [1, 2, 9]
# output = [1, 3, 0]
# Example 3:

# input = [9, 9, 9]
# output = [1, 0, 0, 0]
# Challenge: One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

# But can you solve it in some other way?

# Exercise - Write your function definition here.
# Note - Try proposing a non-recursive solution. We will see a recursive solution in the next lesson "Recursion".

from single_linked_list import SingleLinkedList, Node

def add_one(arr):
    sll = SingleLinkedList()
    for val in arr[::-1]:
        sll.append(val)
    add_and_traverse(sll.head)
    return sll.to_list()[::-1]
    
def add_and_traverse(node):
    node.value += 1
    if node.value < 10:
        return
    else:
        node.value = 0
        if node.next is None:
            node.next = Node(0)
        add_and_traverse(node.next)



def main():
    arr = [9,9,9,9,9]
    print(add_one(arr))
    
main()