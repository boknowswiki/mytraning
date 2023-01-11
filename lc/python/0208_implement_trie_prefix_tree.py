# hash map and trie

class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]

        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
