import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"<Block (timestamp = {self.timestamp}, data = {self.data}, hash = {self.hash})>"


class BlockChain:
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the list. """
        node = Block(datetime.now().strftime("%H:%M %m/%d/%Y"), data)

        if self.tail is None:
            self.tail = node
        else:
            temp = self.tail
            node.previous_hash = temp
            self.tail = node

    def is_empty(self):
        res = (self.tail is None)
        return res

    def len(self):
        llen = 0
        node = self.tail
        while node is not None:
            llen += 1
            node = node.previous_hash
        return llen

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.tail
        if node is None:
            raise IndexError(" pop from empty blockchain")
        elif node.previous_hash is None:
            self.tail = None
            return node
        else:
            node = self.tail
            self.tail = self.tail.previous_hash
            return node

    def __repr__(self):
        res = ""
        node = self.tail
        while node is not None:
            res += f"< Block (ts = {node.timestamp}, data = {node.data}, hash = {node.hash})>" + "\n"
            node = node.previous_hash
        return res
# class BlockChain:
#     def __init
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3


def main():
    blockchain = BlockChain()
    blockchain.append("hi, this is first block")
    blockchain.append("hi, this is second block")
    print(f"blockchain  = {blockchain}")

    print(f"result = {blockchain.pop()}")
    print(f"result = {blockchain.pop()}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
