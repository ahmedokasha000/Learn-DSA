from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        cur_node = self.root
        for letter in word:
            cur_node = cur_node.children[letter]
        
        cur_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.children:
                return False
            else:
                cur_node = cur_node.children[letter]
        return cur_node.is_word

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
        """
        cur_node = self.root
        for letter in prefix:
            if letter not in cur_node.children:
                return False
            else:
                cur_node = cur_node.children[letter]
        return True


def main():
    pass


if __name__ == '__main__':
    main()
