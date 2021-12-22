#!/usr/bin/python -t

# dfs and trie

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: return the maximum nunber
    """
    def wordSearchIII(self, board, words):
        trie = Trie()
        for w in words:
            trie.insert(w)

        return self.dfs(board, trie, set(), 0, -1)

    def dfs(self, board, trie, visited, start_i, start_j):
        n, m = len(board), len(board[0])
        word_count = 0
        for i in range(start_i, n):
            _j = start_j + 1 if i == start_i else 0
            for j in range(_j, m):
                if (i, j) in visited:
                    continue
                c = board[i][j]
                if c not in trie.root.children:
                    continue
                visited.add((i, j))
                word_count = max(
                    word_count,
                    self.search_word(board, i, j, trie, trie.root.children[c], visited, i, j),
                )
                visited.remove((i, j))
        return word_count

    def search_word(self, board, x, y, trie, node, visited, start_i, start_j):
        n, m = len(board), len(board[0])
        word_count = 0
        if node.is_word:
            node.is_word = False
            word_count = self.dfs(board, trie, visited, start_i, start_j) + 1
            node.is_word = True
        for dx, dy in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            i = x + dx
            j = y + dy
            if i < 0 or i >= n or j < 0 or j >= m:
                continue
            if (i, j) in visited:
                continue
            c = board[i][j]
            if c not in node.children:
                continue
            visited.add((i, j))
            word_count = max(
                word_count,
                self.search_word(board, i, j, trie, node.children[c], visited, start_i, start_j),
            )
            visited.remove((i, j))
        return word_count
