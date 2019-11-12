#!/usr/bin/python -t

# dfs and bfs


from collections import defaultdict, deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        result = []
        distances = defaultdict(int) # a dict to store word(key) and distance from end
        mapping = defaultdict(list) # a dict to store word(key) and set of next words (value)
        dict.add(start) # add the start to dictionary (must-do)
        dict.add(end) # add the end to dictionary (must-do)

        self.bfs(start, end, dict, distances, mapping)
        self.dfs(start, end, [], distances, mapping, result)

        return result


    def dfs(self, current_word, end, path, distances, mapping, result):
        '''
        use DFS to traverse each word and next word recursively, following the distance
        '''
        if current_word == end:
            path.append(end)
            result.append([]+ path)
            path.pop()
            return

        for next_word in mapping[current_word]:
            if distances[current_word] == distances[next_word] + 1:
                path.append(current_word)
                self.dfs(next_word, end, path, distances, mapping, result)
                path.pop()


    def bfs(self, start, end, dictionary, distances, mapping):
        '''
        use BFS to traverse all word transformation from end to begin.
        store the distance (the step of transformation)
        for each word in Dictionary/Hash Map, called distances
        distances = {word: distance, ...}
        mapping = {word: [next_word1, next_word2,...]}
        '''

        queue = deque([end])
        visited = set([end])
        distance = 0

        while queue:
            size = len(queue)

            # traverse by level
            for i in range(size):
                word = queue.popleft()
                distances[word] = distance

                next_words = self.get_next_words(word, dictionary)
                mapping[word] = next_words

                for next_word in next_words:
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
            distance += 1

        return

    def get_next_words(self, word, dictionary):

        next_words = []
        for i in range(len(word)):
            for j in range(26):
                index = ord('a') + j
                if index != ord(word[i]):
                    new_char = chr(index)
                    new_word = self.replace_char(i,new_char, word)

                    if new_word in dictionary:
                        next_words.append(new_word)

        return next_words

    def replace_char(self, i, char, word):
        return word[:i] + char + word[i + 1:]
    



from collections import defaultdict, deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        ret = []
        
        dist = defaultdict(int)
        mapping = defaultdict(list)
        
        dict.add(start)
        dict.add(end)
        
        self.bfs(start, end, dict, dist, mapping)
        self.dfs(start, end, [], dist, mapping, ret)

        return ret
        
    def bfs(self, start, end, dict, dist, mapping):
        q = deque()
        q.append(end)
        v = set()
        v.add(end)
        distance = 0
        
        while len(q) > 0:
            l = len(q)
            
            for i in range(l):
                word = q.popleft()
                dist[word] = distance
                
                next_words = self.get_next_words(word, dict)
                mapping[word] = next_words
                
                for n_word in next_words:
                    if n_word not in v:
                        q.append(n_word)
                        v.add(n_word)
                    
            distance += 1
            
        return
    
    def get_next_words(self, word, dict):
        words = []
        
        for i in range(len(word)):
            for j in range(26):
                index = ord('a') + j
                if index != ord(word[i]):
                    new_char = chr(index)
                    new_word = self.replace_char(i, new_char, word)
                    
                    if new_word in dict:
                        words.append(new_word)
                        
        return words
        
    def replace_char(self, i, new_char, word):
        return word[:i] + new_char + word[i+1:]
        
        
    def dfs(self, cur, end, path, dist, mapping, ret):
        if cur == end:
            path.append(end)
            ret.append(list(path))
            path.pop()
            
            return
        
        for next_word in mapping[cur]:
            if dist[cur] == dist[next_word] + 1:
                path.append(cur)
                self.dfs(next_word, end, path, dist, mapping, ret)
                path.pop()
                
        return
            
