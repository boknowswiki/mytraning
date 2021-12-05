#!/usr/bin/python -t

class Solution:
    """
    @param sx: x for starting point
    @param sy: y for starting point
    @param tx: x for target point 
    @param ty: y for target point
    @return: if a sequence of moves exists to transform the point (sx, sy) to (tx, ty)
    """
    def reachingPoints(self, sx, sy, tx, ty):
        # write your code here
        while tx > 0 and ty > 0 and tx != ty and (tx > sx or ty > sy):
            if tx > ty:
                k = (tx-sx)//ty
                tx -= k * ty
            else:
                k = (ty-sy)//tx
                ty -= k*tx
            if k < 1:
                return False

        if tx == sx and ty == sy:
            return True
        if tx == ty and ((sx == 0 and sy == 0) or (sy == 0 and sx == tx)):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    a = 1
    b = 1
    c = 3
    d = 5
    print(s.reachingPoints(a, b,c,d))


# bfs

import collections

class Solution:
    """
    @param sx: x for starting point
    @param sy: y for starting point
    @param tx: x for target point 
    @param ty: y for target point
    @return: if a sequence of moves exists to transform the point (sx, sy) to (tx, ty)
    """
    def reachingPoints(self, sx, sy, tx, ty):
        # write your code here
        if tx < sx or ty < sy:
            return False
        
        v = set()
        q = collections.deque([(tx, ty)])

        while q:
            x, y = q.popleft()

            if (x, y) == (sx, sy):
                return True
            if x == sx and y%sx == 0:
                return True
            if y == sy and x %sy == 0:
                return True
            tmp = x-y
            if tmp >= sx and not(tmp, y) in v:
                q.append((tmp, y))
                v.add((tmp, y))
            tmp = y-x
            if tmp >= sy and not (x, tmp) in v:
                q.append((x, tmp))
                v.add((x, tmp))

        return False

