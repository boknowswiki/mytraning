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
        
        

# bfs, hit TLE, and got AC after replace line 92-95 to line 37-42


import collections

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if self.isOneoff(start, end):
            return 2
            
        q = collections.deque([start])
        cnt = 1
        v = set()
        v.add(start)
        
        while len(q) != 0:
            cnt += 1
            l = len(q)
            
            for _ in range(l):
                cur = q.popleft()
            
                if self.isOneoff(cur, end):
                    return cnt
                
                for w in dict:
                    if self.isOneoff(cur, w) and w not in v:
                        v.add(w)
                        q.append(w)
                    
        return 0
            
            
            
    def isOneoff(self, s1, s2):
        cnt = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 1:
                    return False
                    
        return True
