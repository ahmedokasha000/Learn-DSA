import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")



from my_datastructures.binary_tree import BinaryTree, TreeNode
from my_datastructures.binary_search_tree import BinarySearchTree


def root_to_node_path(root, data):
    res_stack = []
    res_stack
    if root is not None:
        _root_to_node_path(root, data, res_stack)
    return res_stack[::-1]


def _root_to_node_path(node, data, res_stack):
    if node.value == data:
        res_stack.append(node)
        return True
    if node.left is not None:
        res_left = _root_to_node_path(node.left, data, res_stack)
        if res_left is True:
            res_stack.append(node)
            
            return True
    if node.right is not None:
        res_right = _root_to_node_path(node.right, data, res_stack)
        if res_right is True:
            res_stack.append(node)
            return True
    return False
        

def main():
    bst_test = BinarySearchTree(TreeNode(5))
    bst_test.insert(15)
    bst_test.insert(5)
    bst_test.insert(2)
    bst_test.insert(3)
    bst_test.insert(4)

    # bst_test.insert(1)
    # bst_test.insert(-11)
    # bst_test.insert(10)
    # bst_test.insert(8)
    # bst_test.insert(14)
    # bst_test.insert(16)
    print(bst_test)
    print(root_to_node_path(bst_test.root, 4))
if __name__ == '__main__':
    try :
        main()
    except KeyboardInterrupt:
        pass