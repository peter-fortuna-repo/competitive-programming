# Link to problem: https://leetcode.com/problems/search-suggestions-system/

# Solution:
# This approach uses a trie to store the products. The trie is then traversed 
# for each character in the search word. A dfs is used to find the top three
# products starting with the current prefix.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        for i in range(len(searchWord)):
            result.append(trie.topThreeStartingWith(searchWord[:i+1]))
        
        return result

        

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
    
    def topThreeStartingWith(self, prefix: str) -> List[str]:
        node = self.root
        for letter in prefix:
            letter = ord(letter) - 97
            if node.children[letter] == None:
                return []
            node = node.children[letter]      
        def dfs(node, current_word: str, result: List[str]):
            if node == None or len(result) == 3:
                return
            if node.end_of_word == True:
                result.append(current_word)
            for i in range(26):
                dfs(node.children[i], current_word + chr(97 + i), result)

        result = []
        dfs(node, prefix, result)          
        return result