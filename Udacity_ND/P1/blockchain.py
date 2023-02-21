import hashlib
import sys
from pathlib import Path
script_path = Path(__file__).parent.parent
sys.path.append(f"{script_path}")

from my_datastructures.single_linked_list import SingleLinkedList, Node


  
  
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}, {self.data}, {self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return f"<Block (timestamp = {self.timestamp}, data = {self.data}, previous_hash, = {self.previous_hash}, hash = {self.hash})>"
    
# class BlockChain:
#     def __init
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3


def main():
    blockchain = SingleLinkedList()
    block = Block('ts1', 'data1', None)
    blockchain.append(block)
    block = Block('ts1', 'data1', blockchain.tail.value.hash)
    blockchain.append(block)

    print (f"result = {blockchain.pop()}")
    print (f"result = {blockchain.pop()}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass