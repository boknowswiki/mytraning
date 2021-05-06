class Solution:
    """
    @param aString: letter string
    @return: the Minimum times
    """
    def Kstart(self, aString):
        # write your code here
        if not aString:
            return 0
        
        d = {}

        for i in range(len(aString)):
            d[aString[i]] = d.get(aString[i], 0) + 1

        char_count = sorted(d.values())

        index = len(char_count) - 1
        prev = char_count[index]
        index -= 1
        ret = 0

        while index >= 0:
            if char_count[index] >= prev:
                ret += char_count[index] - prev + (1 if prev else 0)
                prev -= (1 if prev else 0)
            else:
                prev = char_count[index]
            index -= 1

        return ret
