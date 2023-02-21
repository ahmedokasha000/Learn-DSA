import sys


class HTNode:
    def __init__(self, value=0, char='', left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.char = char

    def __repr__(self):
        return f"<HTNode( value={self.value}, char={self.char}, left={self.left}, right={self.right})>"

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._size = 0

    @property
    def size(self):
        return self._size

    def _parent_ind(self, ind):
        return (ind - 1) // 2

    def _left_child_ind(self, ind):
        return 2 * ind + 1

    def _right_child_ind(self, ind):
        return 2 * ind + 2

    def get_min(self):
        if self._size == 0:
            raise Exception("Priority queue is empty.")
        return self._heap[0]

    def insert(self, x):
        self._heap.append(x)
        self._size += 1
        self._percolate_up(self._size - 1)

    def _percolate_up(self, ind):
        while ind > 0 and self._heap[ind].value < self._heap[self._parent_ind(ind)].value:
            self._heap[ind], self._heap[self._parent_ind(ind)] = self._heap[self._parent_ind(ind)], self._heap[ind]
            ind = self._parent_ind(ind)

    def extract_min(self):
        if self._size == 0:
            raise Exception("Priority queue is empty.")
        min_val = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self._heap.pop()
        self._percolate_down(0)
        return min_val

    def _percolate_down(self, ind):
        min_index = ind
        lchild_ind = self._left_child_ind(ind)
        if lchild_ind < self._size and self._heap[lchild_ind].value < self._heap[min_index].value:
            min_index = lchild_ind
        rchild_ind = self._right_child_ind(ind)
        if rchild_ind < self._size and self._heap[rchild_ind].value < self._heap[min_index].value:
            min_index = rchild_ind
        if ind != min_index:
            self._heap[ind], self._heap[min_index] = self._heap[min_index], self._heap[ind]
            self._percolate_down(min_index)


def huffman_encoding(data):
    letter_occurrences = {}
    priority_queue = PriorityQueue()
    for letter in data:
        if letter in letter_occurrences:
            letter_occurrences[letter] +=1
        else:
            letter_occurrences[letter] = 1
    for key, val in letter_occurrences.items():
        priority_queue.insert(HTNode(value=val, char=key))

    root = None
    while priority_queue.size > 1:
        left = priority_queue.extract_min()
        right = priority_queue.extract_min()
        root = HTNode(value=left.value + right.value, left=left, right=right)
        priority_queue.insert(root)
    root = priority_queue.extract_min()
    if root.left is None and root.right is None:
        huffman_code = {root.char: '0'}
    else:
        huffman_code = dict(traverse_dfs(root))
    print(huffman_code)
    encoded_data = encode_data(data, huffman_code)
    ## get first two keys with min value
    return encoded_data, root, huffman_code

def encode_data(data, huffman_code):
    encoded_string = ''
    for char in data:
        encoded_string += huffman_code.get(char)
    return encoded_string
        

def traverse_dfs(node, code=''):
    codes = []
    left_codes, right_codes = [], []
    if node.left is None and node.right is None:
        return [(node.char, code)]
    if node.left is not None:
        left_codes = traverse_dfs(node.left, code=code + '0')
    if node.right is not None:
        right_codes = traverse_dfs(node.right, code=code + '1')
    codes.extend(left_codes)
    codes.extend(right_codes)
    return codes

def get_min_kv_pair(d):
    min_key = min(d, key=d.get)
    min_val = d[min_key]
    return min_key, min_val
    
def huffman_decoding(data, tree, huffman_code):
    huffman_to_char = {val: key for key, val in huffman_code.items()}
    decoded_string = ''
    cur_prefix = ''
    for char in data:
        cur_prefix += char
        if huffman_to_char.get(cur_prefix) is not None:
            decoded_string += huffman_to_char[cur_prefix]
            cur_prefix = ''
    return decoded_string


def main():
    encoded_data, huff_tree, huff_code = huffman_encoding("b")
    print(huff_code)
    decoded_msg = huffman_decoding(encoded_data, huff_tree, huff_code)
    print(decoded_msg)
    # min_heap = PriorityQueue()
    # min_heap.insert(HTNode(9))
    # min_heap.insert(HTNode(7))
    # min_heap.insert(HTNode(8))
    # min_heap.insert(HTNode(1))


    # while min_heap.size > 0:
    #     print(min_heap.extract_min())



if __name__ == '__main__':
    main() 





# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))
