#!/usr/bin/python -t

# dfs, need to revisit

class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods 
    @param c: The capacity of goods
    @return: The answer
    """
    def getMaxValue(self, s, v, c):
        # Write your code here
        
        n = len(c)
        if not n:
            return 0
        index = [i for i in range(n)]
        index.sort(key=lambda x:c[x], reverse=True)
        pre_sum = [0] * n
        pre_sum[-1] = v[index[-1]]
        for i in range(n - 2, -1, -1):
            pre_sum[i] = pre_sum[i + 1] + v[index[i]]
        self.result = 0
        def helper(i, cv, cc):
            if cc > s:
                return
            self.result = max(self.result, cv)
            if i >= n or cv + pre_sum[i] <= self.result:
                return
            helper(i + 1, cv + v[index[i]], cc + c[index[i]])
            helper(i + 1, cv, cc)
        helper(0, 0, 0)
        return self.result

# binary search

class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods 
    @param c: The capacity of goods
    @return: The answer
    """
    def comp(self, A, B):
        if(A.x == B.x):
            return A.y - B.y
        else:
            return A.x - B.x
    def getCombination(self, u, i, v, c):
        p = Point(0, 0)
        while(u > 0):
            if(u & 1):
                p.y += v[i];
                p.x += c[i];
            i += 1
            u = u // 2
        return p
    def getMaxValue(self, s, v, c):
        # Write your code here
        n = len(v)
        mid = n // 2
        all = 1 << mid
        ans = 0
        temp, combination = [], []
        for i in range(all):
            t = self.getCombination(i, 0, v, c)
            temp.append(t)
        temp.sort(self.comp)
        maxv = -1
        for i in temp:
            if(i.y > maxv):
                combination.append(i)
                maxv = i.y
        all = 1 << (n - mid)
        m = len(combination)
        for i in range(all):
            t = self.getCombination(i, mid, v, c)
            cap = s - t.x
            if(cap > 0):
                l, r = 0, m - 1
                index = -1
                while(l <= r):
                    middle = (l + r) // 2
                    if(combination[middle].x <= cap):
                        l = middle + 1
                        index = middle
                    else :
                        r = middle -1
                
                if(index != -1):
                    t.y += combination[index].y
                ans = max(ans, t.y)
        return ans

# dfs, LTE

class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods 
    @param c: The capacity of goods
    @return: The answer
    """
    def getMaxValue(self, s, v, c):
        # Write your code here
        n = len(v)
        self.ret = 0
        
        for i in range(n):
            self.dfs(s, v, c, i, c[i], v[i])
            
        return self.ret
        
    def dfs(self, s, v, c, index, vol, val):
        if vol > s:
            return
        
        if val > self.ret:
            self.ret = val
            
        for i in range(index+1, len(v)):
            self.dfs(s, v, c, i, vol+c[i], val + v[i])

