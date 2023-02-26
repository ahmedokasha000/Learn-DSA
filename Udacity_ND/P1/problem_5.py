import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        """
        A class that represents a block in a blockchain.

        :param timestamp: The timestamp of the block creation.
        :type timestamp: str
        :param data: The data that the block contains.
        :type data: Any
        :param previous_hash: The hash of the previous block in the chain.
        :type previous_hash: Block or None
        """
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        """
        Calculate the hash value of the block using the SHA-256 algorithm.

        :return: The hash value of the block.
        :rtype: str
        """
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp} {self.data}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    # def __repr__(self):
    #     return f"<Block (timestamp = {self.timestamp}, data = {self.data}, hash = {self.hash})>"


class BlockChain:
    """
    A class that represents a blockchain.
    """
    def __init__(self):
        self.tail = None

    def append(self, data):
        """
        Append a block to the end of the blockchain.

        :param data: The data to be added to the block.
        :type data: Any
        """
        node = Block(datetime.now().strftime("%H:%M %m/%d/%Y"), data)

        if self.tail is None:
            self.tail = node
        else:
            temp = self.tail
            node.previous = temp
            node.previous_hash = temp.hash
            self.tail = node

    def is_empty(self):
        res = (self.tail is None)
        return res

    def len(self):
        llen = 0
        node = self.tail
        while node is not None:
            llen += 1
            node = node.previous
        return llen

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        node = self.tail
        if node is None:
            raise IndexError(" pop from empty blockchain")
        elif node.previous is None:
            self.tail = None
            return node
        else:
            node = self.tail
            self.tail = self.tail.previous
            return node

    def __repr__(self):
        res = ""
        node = self.tail
        while node is not None:
            res = f"< Block (ts = {node.timestamp}, data = {node.data}, hash = {node.hash}, previous_hash = {node.previous_hash})>" + "\n" + res
            node = node.previous
        return res


def test_cases():
    # Test Case 1, general
    blockchain = BlockChain()
    blockchain.append("first")
    blockchain.append("second")
    blockchain.append("third")
    assert blockchain.pop().data == "third" and blockchain.pop().data == "second" and blockchain.pop().data == "first", "Test 1 failed."
    print("Test 1 passed.")
    # Test Case 2, test that block chain is now empty
    assert blockchain.is_empty(), "Test 2 failed."
    print("Test 2 passed.")
    # Test Case 3, test the previous hash
    blockchain.append("first")
    blockchain.append("second")
    assert blockchain.pop().previous.data == "first", "Test 3 failed."
    print("Test 3 passed.")


def main():
    blockchain = BlockChain()
    blockchain.append("hi, this is first block")
    blockchain.append("hi, this is second block")
    blockchain.append("hi, this is third block")
    print(blockchain)
    test_cases()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
