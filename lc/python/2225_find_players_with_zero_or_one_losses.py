# hash map and sort
# time O(nlgn)
# space O(n)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winers = set()
        losers = {}
        
        for w, l in matches:
            winers.add(w)
            if l not in losers:
                losers[l] = 0
            losers[l] += 1
            
        w_ret = []
        for w in winers:
            if w not in losers:
                w_ret.append(w)
        l_ret = []
        for l in losers:
            if losers[l] == 1:
                l_ret.append(l)
        w_ret.sort()
        l_ret.sort()
        return [w_ret, l_ret]
