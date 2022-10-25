# divide and conquer
# time O(nlogn)
# space O(n)

# reference https://leetcode.com/problems/longest-nice-substring/discuss/1693408/Python3-From-O(N2)-to-O(N)

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(i: int, j: int):
		   # string length is less than 2 return empty string
		   # we return a tuple to indicate the start and end index of the string to avoid unncessary string copy operation
            if j - i + 1 < 2: return (0, -1)
            hashset = set()
			# scan the string once and save all char into a set
            for k in range(i, j + 1):
                hashset.add(s[k])
            
            for k in range(i, j + 1):
			   # if this char pairs with its other half, we are good
                if s[k].upper() in hashset and s[k].lower() in hashset:
                    continue
			  # we found `E` !
                slt = helper(i, k - 1)
                srt = helper(k + 1, j)
                return slt if (slt[1] - slt[0] + 1) >= (srt[1] - srt[0] + 1) else srt
            return (i, j)
        lt, rt = helper(0, len(s) - 1)
        return s[lt:(rt + 1)]
