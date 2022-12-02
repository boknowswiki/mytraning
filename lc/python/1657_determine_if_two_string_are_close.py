# hash map and sort
# time O(n)
# space O(n)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not word1 or not word2:
            return word1 == word2
        
        word1_map = dict()
        word1_set = set()
        word1_freq = list()
        
        word2_map = dict()
        word2_set = set()
        word2_freq = list()
        
        for w in word1:
            word1_map[w] = word1_map.get(w, 0) + 1
            word1_set.add(w)
            
        for w in word2:
            word2_map[w] = word2_map.get(w, 0) + 1
            word2_set.add(w)
            
        if len(word1_set) != len(word2_set):
            return False
        for w in word1_set:
            if w not in word2_set:
                return False
            
        for _, freq in word1_map.items():
            word1_freq.append(freq)
            
        for _, freq in word2_map.items():
            word2_freq.append(freq)
            
        return sorted(word1_freq) == sorted(word2_freq)
