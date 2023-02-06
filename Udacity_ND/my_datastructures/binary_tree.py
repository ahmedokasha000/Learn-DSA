
import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")

from my_datastructures.stack import StackPy


class TreeNode:
    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None

    def has_left(self):
        return True if self._left is not None else False

    def has_right(self):
        return True if self._right is not None else False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if isinstance(node, TreeNode) or node is None:
            self._left = node
        else:
            raise ValueError("Tree nodes must be of type TreeNode")

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if isinstance(node, TreeNode) or node is None:
            self._right = node
        else:
            raise ValueError("Tree nodes must be of type TreeNode")

    def __repr__(self):
        return f"Node({self.value})"
    
    def __str__(self):
        return f"Node({self.value})"


class BinaryTree:
    def __init__(self, root: TreeNode = None):
        self._root = root
        pass

    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, node):
        self._root = node

    def traverse_dfs(self, order="preorder"):
        node = self._root
        if node is not None:
            return self._traverse_dfs(node, order)
        else:
            return []

    def _traverse_dfs(self, node, order="preorder"):
        left_values, right_values = [], []

        if node.has_left():
            left_values = self._traverse_dfs(node.left, order=order)
        if node.has_right():
            right_values = self._traverse_dfs(node.right, order=order)

        if order == "preorder":
            return [node.value] + left_values + right_values
        elif order == "inorder":
            return left_values + [node.value] + right_values
        elif order == "postorder":
            return left_values + right_values + [node.value]

    def traverse_bfs(self):
        node = self._root
        if node is not None:
            return self._traverse_bfs([node])
        else:
            return []

    def _traverse_bfs(self, cur_level_nodes):
        cur_level_values, next_level_nodes = [], []
        for node in cur_level_nodes:
            cur_level_values.append(node.value)
            if node.has_left():
                next_level_nodes.append(node.left)
            if node.has_right():
                next_level_nodes.append(node.right)

        if len(next_level_nodes) > 0:
            return cur_level_values + self._traverse_bfs(next_level_nodes)
        else:
            return cur_level_values

    def __repr__(self):
        node = self._root
        if node is not None:
            return self._traverse_bfs_repr([node], [str(node.value)])
        else:
            return print([])

    def _traverse_bfs_repr(self, cur_level_nodes, cur_level_values):
        next_level_nodes, next_level_values = [], []
        for node in cur_level_nodes:
            if node.has_left():
                next_level_nodes.append(node.left)
                next_level_values.append(str(node.left.value))
            else:
                next_level_values.append(str("<empty>"))
            if node.has_right():
                next_level_nodes.append(node.right)
                next_level_values.append(str(node.right.value))
            else:
                next_level_values.append(str("<empty>"))

        if len(next_level_nodes) > 0:
            return "\t|\t".join(cur_level_values) + '\n' + self._traverse_bfs_repr(next_level_nodes, next_level_values)
        else:
            return "\t|\t".join(cur_level_values)
def main():
    node = TreeNode("apple")
    node.left = TreeNode("banana")
    node.right = TreeNode("cherry")
    node.left.left = TreeNode("dates")
    node.left.right = TreeNode("kiwi")
    node.right.left = TreeNode("orange")
    node.left.left.left = TreeNode("grapes")

    binary_tree = BinaryTree(node)
    binary_tree2 = BinaryTree()

    print("Pre-order: ", binary_tree.traverse_dfs("preorder"))
    print("In-order: ",binary_tree.traverse_dfs("inorder"))
    print("Post-order: ",binary_tree.traverse_dfs("postorder"))
    print("DFS: ",binary_tree.traverse_bfs())
    print("DFS: ",binary_tree2.traverse_bfs())
    print(binary_tree)

if __name__ == '__main__':
    main()