# bfs

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque([beginWord])
        cnt = 0
        wl = set(wordList)
        
        while q:
            cnt += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return cnt
                ws = self.next_word(cur)
                for w in ws:
                    if w in wl:
                        wl.remove(w)
                        q.append(w)
                        
        return 0
    
    def next_word(self, a):
        ret = []
        for i in range(len(a)):
            for j in range(26):
                c = chr(ord("a") + j)
                new_a = a[:i] + c + a[i+1:]
                ret.append(new_a)
                    
        return ret

      
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
