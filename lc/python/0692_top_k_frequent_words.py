
# heap and hashmap
# time O(nlogk)
# space O(k)

import collections
import heapq
import functools

@functools.total_ordering
class FreqWord:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap).word for _ in range(k)][::-1]
