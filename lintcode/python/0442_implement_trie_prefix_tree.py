#!/usr/bin/python -t

# Trie
# build O(n), search O(1)

class trieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = trieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = trieNode()

            cur = cur.children[i]
                
        cur.is_word = True
        
        return

    def find(self, word):
        cur = self.root
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return None
                
        return cur
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.find(word)
        return node != None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        return self.find(prefix) is not None
        

