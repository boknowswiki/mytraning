
# sliding windows
# time O(maxUnque * n)
# space O(1)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for n_c in range(1, len(Counter(s))+1):
          
            found = 0
            dct = defaultdict(int)
            start = 0
            for end in range(len(s)):
            
                c = s[end]
                dct[c] += 1
                if dct[c] == k:
                    found += 1

                while len(dct) > n_c:
                    c = s[start]
                    start += 1
                    dct[c] -= 1
                    if dct[c] == k-1:
                        found -= 1
                    if dct[c] == 0:
                        del dct[c]

                if len(dct) == n_c and found == n_c:
                    res = max(res, end-start+1)
                        
        return res
      
# divide and conquer
# time O(n^2)
# space O(n)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if s == [] or k > len(s):
            return 0
        freq = collections.Counter(s)
        for i, char in enumerate(s):
            if freq[char] < k:
                return max(self.longestSubstring(s[:i], k),  self.longestSubstring(s[i+1:], k))
        return len(s)
