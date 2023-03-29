
from enum import IntEnum


class NodeColor(IntEnum):
    RED = 0
    BLACK = 1


class TreeNode:
    def __init__(self, value=None, parent=None, color=NodeColor.RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = parent


class RedBlackTree:
    
    NIL = TreeNode(color=NodeColor.BLACK)

    def __init__(self, root: TreeNode = None):
        self.root = root
        self.size = 0

    def insert(self, value):
        cur_node = self.root
        if cur_node is None:
            self.root = self.create_tree_node(value)
            inserted_node = self.root
            self.size += 1
        else:
            inserted_node = self._insert(cur_node, value)

        self.rebalance(inserted_node)

    def _insert(self, node, value):
        if value > node.value:
            if node.right != self.NIL:
                new_node = self._insert(node.right, value)
            else:
                new_node = self.create_tree_node(value, parent=node)
                node.right = new_node
                self.size += 1

        elif value < node.value:
            if node.left != self.NIL:
                new_node = self._insert(node.left, value)
            else:
                new_node = self.create_tree_node(value, parent=node)
                node.left = new_node
                self.size += 1
        else:
            # trying to insert existing value
            new_node = node
        return new_node
                
    def delete(self, value):
        pass

    def search(self, find_val):
        return False

    def rebalance(self, node):
        if node.parent is None:
            node.color = NodeColor.BLACK
            return
        if node.parent.color == NodeColor.BLACK:
            return
        parent = node.parent
        grandparent = node.parent.parent
        if grandparent.left == parent:
            uncle = grandparent.right
        else:
            uncle = grandparent.left
        
        if uncle
    # def __repr__(self):
    #     pass
    def rotate_left(self, node):
        right_child = node.right
        right_child_left_path = node.right.left

        right_child.parent = node.parent
        if node.parent == self.NIL:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        node.right = right_child_left_path
        if right_child_left_path != self.NIL:
            right_child_left_path.parent = node
        
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        left_child_right_path = node.left.right

        left_child.parent = node.parent
        if node.parent == self.NIL:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        node.left = left_child_right_path
        if left_child_right_path != self.NIL:
            left_child_right_path.parent = node
        
        left_child.right = node
        node.parent = left_child
    
    def create_tree_node(self, value, parent=None):
        node = TreeNode(value, parent)
        node.left = self.NIL
        node.right = self.NIL
        return node

def main():
    tree = RedBlackTree()
    values = list(range(10))
    for val in values:
        tree.insert(val)

    ## Test cases
    ## check for BST rules
    ## check for Red-Black trees rules
    print(tree.size)
    assert tree.size == len(values), "wrong tree size"
    assert tree.root.color == NodeColor.BLACK, "tree root node is not black"

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
