#!/usr/bin/python -t

class Solution:
    """
    @param names: the name
    @param grades: the grade
    @return: the maximum average score
    """
    def maximumAverageScore(self, names, grades):
        # Write your code here
        strmap = {};
        for i in range(0, len(names)):
            cur = names[i];
            if strmap.has_key(cur):
                k = strmap[cur];
                k[0] = k[0] + 1;
                k[1] = k[1] + grades[i];
                strmap[cur] = k;
            else:
                k = [1, grades[i]];
                strmap[cur] = k;
        ans = 0;
        for key in strmap.keys():
            k = strmap[key];
            if k[1] * 1.0 / k[0] > ans :
                ans = k[1] * 1.0 / k[0];
        return ans;
