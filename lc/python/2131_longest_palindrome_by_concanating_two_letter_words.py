# hash map
# reference https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solution/
# Let N be the number of words in the input array and ∣Σ∣ be the size of the English alphabet (∣Σ∣=26)
# Time complexity: O(N+min(N,∣Σ∣^2))
# Space complexity: O(min(N,∣Σ∣^2)).

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ret = 0
        central = False
        
        for word, cnt_of_word in cnt.items():
            if word[0] == word[1]:
                if cnt_of_word % 2 == 0:
                    ret += cnt_of_word
                else:
                    ret += cnt_of_word-1
                    central = True
            elif word[0] < word[1]:
                ret += 2 * min(cnt_of_word, cnt[word[1]+word[0]])
                
        if central:
            ret += 1
            
        return ret*2
