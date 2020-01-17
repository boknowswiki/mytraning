#!/usr/bin/python -t

# two pointers

#分析归纳出 4种情况
#'R......R' => 'RRRRRRRR'
#'R......L' => 'RRRRLLLL' or 'RRRR.LLLL'
#'L......R' => 'L......R'
#'L......L' => 'LLLLLLLL'
#
#自己解题的时候，出现一个思维上的误区，就是一块骨牌最终的状态只取决于左右两边的情况，而非骨牌的数量。
#也就是说，一块骨牌左边有2块往右边倒， 右边有5块往左边倒，这块骨牌最终是站立的，而不是向左边倒。
#
#对于范围 [a, b]的骨牌的状态，是由 a-1,和 b+1这两块骨牌决定的，所以给原始的string左右分别加上一块辅助的骨牌。

class Solution:
    """
    @param dominoes: a string
    @return: a string representing the final state
    """
    def pushDominoes(self, dominoes):
        # Write your code here
        if not dominoes:
            return dominoes
            
        s = 'L' + dominoes + 'R'
        n = len(s)
        #print s
        ret = ''
        
        i = 0
        for j in range(1, n):
            c = s[j]
            if c == '.':
                continue
            if i > 0:
                ret += s[i]
                
            midlen = j-i-1
            if s[i] == s[j]:
                for k in range(midlen):
                    ret += c
            elif s[i] == 'L' and s[j] == 'R':
                for k in range(midlen):
                    ret += '.'
            else:
                for k in range(midlen/2):
                    ret += 'R'
                if midlen % 2 == 1:
                    ret += '.'
                for k in range(midlen/2):
                    ret += 'L'
                    
            i = j
            
        return ret
        
