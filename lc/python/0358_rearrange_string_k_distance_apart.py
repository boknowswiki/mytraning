# heapq, counting

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        heap = [(-freq, char) for char, freq in collections.Counter(s).items()]
        heapq.heapify(heap)
        res = []
        while len(res) < len(s):
            if not heap: return ""
            freq, char = heapq.heappop(heap)
            stack = []
            res.append(char)
            for j in range(k - 1):
                if len(res) == len(s): return "".join(res)
                if not heap: return ""
                fre, nex = heapq.heappop(heap)
                res.append(nex)
                if fre < -1: 
                    stack.append((fre+1, nex))
            while stack:
                heapq.heappush(heap, stack.pop())
            heapq.heappush(heap, (freq+1, char))
        return "".join(res)
