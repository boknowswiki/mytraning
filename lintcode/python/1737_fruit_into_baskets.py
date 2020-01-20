#!/usr/bin/python -t

# two pointers
# similar as 0386

class Solution:
    """
    @param tree: The type of fruit
    @return: The total amount of fruit you can collect.
    """
    def totalFruit(self, tree):
        # write your code here
        ret = cnt_cur = type_a = type_b = cnt_a = cnt_b = 0
        
        for t in tree:
            if t in (type_a, type_b):
                cnt_cur += 1
            else:
                cnt_cur = cnt_b + 1
                
            if t == type_b:
                cnt_b += 1
            else:
                cnt_b = 1
                
            if t != type_b:
                type_a, type_b = type_b, t
            
            ret = max(ret, cnt_cur)
            
        return ret
        
        

class Solution:
    """
    @param tree: The type of fruit
    @return: The total amount of fruit you can collect.
    """
    def totalFruit(self, tree):
        # write your code here
        l = r = 0
        n = len(tree)
        cnt = {}
        ret = 0
        
        for r in range(n):
            cnt[tree[r]] = cnt.get(tree[r], 0) + 1
            
            while l <= r and len(cnt) > 2:
                cnt[tree[l]] -= 1
                if cnt[tree[l]] == 0:
                    del cnt[tree[l]]
                l += 1
                
            ret = max(ret, r - l + 1)
            
        return ret
        
