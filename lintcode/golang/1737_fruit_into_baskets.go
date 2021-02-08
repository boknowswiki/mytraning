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
