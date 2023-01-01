
# hash map

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in map_index:
                map_index[char_key] = i
            
            if char_word not in map_index:
                map_index[char_word] = i 
            
            if map_index[char_key] != map_index[char_word]:
                return False
        
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_char = {}
        map_word = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = collections.defaultdict(list)
        pi = collections.defaultdict()
        for i, pa in enumerate(pattern):
            p[pa].append(i)
            pi[i] = pa

        np = collections.defaultdict(list)
        npi = collections.defaultdict()
        s_list = s.split(" ")
        for i, ele in enumerate(s_list):
            np[ele].append(i)
            npi[i] = ele

        if len(p) != len(np):
            return False

        for key in npi:
            ele = npi[key]
            el = pi[key]
            if np[ele] != p[el]:
                return False

        return True
