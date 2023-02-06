import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")



from my_datastructures.binary_tree import BinaryTree, TreeNode
from my_datastructures.binary_search_tree import BinarySearchTree


def binary_tree_diameter(node: TreeNode):
    cur_diamenter, cur_height = 0, 0
    left_diameter, right_diameter, left_height, right_height = 0, 0, 0, 0
    if node.has_left():
        left_diameter, left_height = binary_tree_diameter(node.left)
        left_height += 1
    if node.has_right():
        right_diameter, right_height = binary_tree_diameter(node.right)
        right_height += 1
    cur_height = max(left_height, right_height)
    cur_diamenter = max(right_height + left_height, cur_height)
    max_diameter = max(cur_diamenter, left_diameter, right_diameter)
    return max_diameter, cur_height
        

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
    print(binary_tree_diameter(bst_test.root))
if __name__ == '__main__':
    try :
        main()
    except KeyboardInterrupt:
        pass