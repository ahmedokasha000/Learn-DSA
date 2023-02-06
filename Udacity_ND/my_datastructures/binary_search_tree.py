
from binary_tree import TreeNode, BinaryTree

class BinarySearchTree(BinaryTree):
    def __init__(self, root: TreeNode = None):
        super().__init__(root)

    # def insert_no_rec(self, value):
    #     cur_node = self.root
    #     if cur_node is None:
    #         self.root = TreeNode(value)
    #         return
    #     while cur_node is not None:
    #         if value > cur_node.value:
    #             if cur_node.right is not None:
    #                 cur_node = cur_node.right
    #             else:
    #                 cur_node.right = TreeNode(value)
    #                 return
    #         elif value < cur_node.value:
    #             if cur_node.left is not None:
    #                 cur_node = cur_node.left
    #             else:
    #                 cur_node.left = TreeNode(value)
    #                 return
    #         else:
    #             return

    def insert(self, value):
        cur_node = self.root
        if cur_node is None:
            self.root = TreeNode(value)
        else:
            self._insert(cur_node, value)

    def _insert(self, node, value):
        if value > node.value:
            if node.has_right():
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

        elif value < node.value:
            if node.has_left():
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(self.root, value)

    def _search(self, node, value):
        if value == node.value:
            return True
        elif value > node.value:
            if not node.has_right():
                return False
            else:
                return self._search(node.right, value)
        elif value < node.value:
            if not node.has_left():
                return False
            else:
                return self._search(node.left, value)
    def find_node(self, value):
        """
        find the node with the provided value and its parent node
        @return (node, parent) if found else None
        """
        if self.root is None:
            return None, None
        else:
            return self._find_node(None, self.root, value)

    def _find_node(self, parent, node, value):
        if value == node.value:
            return parent, node
        elif value > node.value:
            if not node.has_right():
                return None, None
            else:
                return self._find_node(node, node.right, value)
        elif value < node.value:
            if not node.has_left():
                return None, None
            else:
                return self._find_node(node, node.left, value)
            
    def delete(self, value):
        parent, node = self.find_node(value)
        if node is None:
            return
        if not node.has_left() and not node.has_right():
            if parent is None:  # we have only the root node
                self.root = None
            elif parent.has_left() and parent.left is node:  # child node
                parent.left = None
            else:
                parent.right = None
        elif node.has_left() and node.has_right():
            ## find smallest node in right subtree, set node value to its value, delete it
            parent_temp = node
            inorder_successor = node.right
            while inorder_successor.has_left():
                parent_temp = inorder_successor
                inorder_successor = inorder_successor.left
            node.value = inorder_successor.value
            if parent.left is inorder_successor:
                parent_temp.left = None
            else:
                parent_temp.right = None
        else:
            if node.has_left():
                node.value = node.left.value
                node.left = None
            else:
                node.value = node.right.value
                node.right = None

def main():
    bst_test = BinarySearchTree(TreeNode(5))
    bst_test.insert(15)
    bst_test.insert(5)
    bst_test.insert(2)
    bst_test.insert(3)
    bst_test.insert(1)
    bst_test.insert(-11)
    bst_test.insert(10)
    bst_test.insert(8)
    bst_test.insert(14)
    bst_test.insert(16)

    print(bst_test)
    print(" search for 6", bst_test.search(5))
    print(" find value 6", bst_test.find_node(6))
    bst_test.delete(2)

    print("Delete value 2, tree = \n", bst_test)
    bst_test.delete(10)

    print("Delete value 10, tree = \n", bst_test)
    

if __name__ == '__main__':
    main()