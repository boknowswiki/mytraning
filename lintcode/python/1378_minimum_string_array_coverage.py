class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """
    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        mp1, mp2 = {}, {}
        for i in tagList:
            mp1[i] = 1
            mp2[i] = 0
        l , r = 0, -1
        n = len(allTags)
        m = len(tagList)
        cnt = 0
        ans = n + 1
        while(r < n):
            if(cnt < m):
                r += 1
                if(r == n):
                    break
                if(allTags[r]  in mp1):
                    mp2[allTags[r]] += 1
                    if(mp2[allTags[r]] == 1):
                        cnt += 1
            else:
                if(allTags[l] in mp1):
                    mp2[allTags[l]] -= 1
                    if(mp2[allTags[l]] == 0):
                        cnt -= 1
                l += 1
            if(cnt == m):
                ans = min(ans, r - l + 1)
        if(ans == n + 1):
            ans = -1
        return ans
