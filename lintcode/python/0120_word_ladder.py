#!/usr/bin/python -t

# bfs


from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1
            
        dict.add(end)
        q = deque()
        q.append(start)
        v = set()
        v.add(start)
        ret = 0
        
        while len(q) > 0:
            ret += 1
            l = len(q)
            
            for _ in range(l):
                word = q.popleft()
                
                if word == end:
                    return ret
                
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in v:
                        continue
                    
                    q.append(next_word)
                    v.add(next_word)
                    
        return 0
        
    def get_next_words(self, word):
        words = []
        
        for i in range(len(word)):
            l, r = word[:i], word[i+1:]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:
                    continue
                words.append(l+c+r)
                
        return words
        
        
