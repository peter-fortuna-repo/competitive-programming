# Link to problem: https://leetcode.com/problems/implement-trie-prefix-tree/

# Solution:
# This approach uses nodes with 26 children cointained in an array, where each 
# child represents a letter in the alphabet.

class Trie:
    class Node:
        def __init__(self) -> None:
            self.end_of_word = False
            self.children = [None] * 26

        def hasChild(self, letter) -> bool:
            return self.children[letter] != None

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            letter = ord(letter) - 97
            if node.children[letter] == None:
                node.children[letter] = self.Node()
            node = node.children[letter]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            letter = ord(letter) - 97
            if node.children[letter] == None:
                return False
            node = node.children[letter]
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            letter = ord(letter) - 97
            if node.children[letter] == None:
                return False
            node = node.children[letter]
        return True