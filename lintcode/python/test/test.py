#!/usr/bin/python -t

class trieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = trieNode()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = trieNode()
            cur = cur.children[w]

        cur.is_word = True

        return

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        if word == None:
            return False
        return self.find(word, self.root, 0)
        

    def find(self, word, node, index):
        if node == None:
            return False
        if index >= len(word):
            return node.is_word
            
        c = word[index]
        if c != ".":
            return self.find(word, node.children.get(c), index+1)
        
        for child in node.children:
            if self.find(word, node.children[child], index+1):
                return True

        return False

if __name__ == "__main__":
    s = WordDictionary()
    s.addWord("a")
    print(s.search("."))
    
