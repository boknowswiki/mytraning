
# hash map
# time O(nk)
# space O(nk)

class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
# hash map
# time O(n*nlog(len(word)))
# space O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        d = {}
        ret = []
        
        for st in strs:
            st_con = self.convert(st)
            if st_con not in d:
                d[st_con] = []
                
            d[st_con].append(st)
            
        for k, v in d.items():
            ret.append(v)
            
        return ret
    
    def convert(self, s):
        return "".join(sorted(s.lower()))
