#!/usr/bin/python -t

# bfs


class Solution:
    """
    @param generator: Generating set of rules.
    @param startSymbol: Start symbol.
    @param symbolString: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, generator, startSymbol, symbolString):
        # Write  your code here.
        dq = collections.deque([list(startSymbol)])
        d = {}
        target = list(symbolString)
        for gen in generator:
            fr, to = gen.split(' -> ')
            d[fr] = d.get(fr, []) + [to]
        while dq:
            s = dq.popleft()
            if s == target: return True
            for i in range(len(s)):
                c = s[i]
                if c in d:
                    for val in d[c]:
                        if c in val:
                            val = val.replace(c, d[c][-1])
                        s[i] = val
                        dq.append(list(''.join(s)))
        return False

# dfs

class Solution:
    """
    @param generator: Generating set of rules.
    @param startSymbol: Start symbol.
    @param symbolString: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, generator, startSymbol, symbolString):
        # Write  your code here.
        sym = [[] for i in range(26)]
        for i in generator:
            sym[self.getIdx(i[0])].append(i[5:])
        idx = self.getIdx(startSymbol)
        for i in sym[idx]:
            if self.isMatched(symbolString, 0, i, sym):
                return True
        return False
        
    def getIdx(self, c):
        return ord(c) - ord('A')
        
        
    def nonTerminal(self, c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')
        
        
    def isMatched(self, s, pos, gen, sym):
        if pos == len(s):
            if len(gen) == 0:
                return True
            else:
                return False
        else:
            if len(gen) == 0:
                return False
            elif self.nonTerminal(gen[0]):
                idx = self.getIdx(gen[0])
                for i in sym[idx]:
                    if self.isMatched(s, pos, i + gen[1:], sym):
                        return True
            elif gen[0] == s[pos]:
                if self.isMatched(s, pos + 1, gen[1:], sym):
                    return True
            else:
                return False
        return False
        
        

