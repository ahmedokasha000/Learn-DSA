
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
        if isinstance(node, TreeNode):
            self._left = node
        else:
            raise ValueError("Tree nodes must be of type TreeNode")

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if isinstance(node, TreeNode):
            self._right = node
        else:
            raise ValueError("Tree nodes must be of type TreeNode")


class BinaryTree:
    def __init__(self, root: TreeNode = None):
        self._root = root
        pass

    @property
    def root(self):
        return self._root


def main():
    node = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node.left = node1
    node.right = node2
    print(node.value)
    print(node.left.value)
    print(node.right.value)
    print(node.has_left())
    print(node.left.has_left())

if __name__ == '__main__':
    main()