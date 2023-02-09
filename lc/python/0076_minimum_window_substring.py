# hash map, sliding window


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [1] obtain letter frequencies
        freq = Counter(t)
        
        # [2] in this solution, we use a two-pointer sliding window 
        #    approach while keeping track of a number of unique 
        #    characters from 't' that are missing on each iteration 
        miss  = len(set(t))
        l, r  = 0, 0
        wl, wr = -1, len(s)
        
        while True:
            # [3] move right pointer while we're still 
            #    missing any of the characters from 't' 
            if r < len(s) and miss > 0:
                freq[s[r]] -= 1
                if freq[s[r]] == 0: miss -= 1
                r += 1
                
            # [4] move left pointer while we're still
            #    having a surplus of characters from 't' 
            elif l < len(s) and miss <= 0:
                # [5] the update of minimal substring happens only when
                #    we move the left pointer, i.e., when we already 
                #    have no characters from 't' missing 
                if r-l < wr-wl: wr, wl = r, l
                    
                if freq[s[l]] == 0: miss += 1
                freq[s[l]] += 1
                l += 1
                
            else:
                break
        
        return s[wl:wr] if wl >= 0 else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
